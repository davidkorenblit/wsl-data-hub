"""
FotMob Raw Data Ingestion Engine
================================
Automated ingestion pipeline for Women's Football data from FotMob:
- UWCL (Women's Champions League) League & Topstats
- WSL (Women's Super League) League & Topstats
- Elite Clubs: Barcelona (W), Lyon (W), London City Lionesses, and all WSL clubs
- Star Players: Mapi León, Alexia Putellas, Mary Earps

All raw JSON responses are persisted to `data/raw/fotmob/` with manifest logging.
"""

import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Optional
import requests

from paths import (
    FOTMOB_RAW_DIR,
    FOTMOB_LEAGUES_DIR,
    FOTMOB_TEAMS_DIR,
    FOTMOB_PLAYERS_DIR,
    ensure_all_directories
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("FotMobIngestion")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

# Configuration of Target Entities
LEAGUES_TO_FETCH = [
    {
        "id": 9227,
        "name": "WSL",
        "slug": "wsl",
        "topstats_seasons": [
            {"season": "2025/2026", "season_id": 27506},
            {"season": "2024/2025", "season_id": 23925}
        ]
    },
    {
        "id": 9375,
        "name": "UWCL",
        "slug": "uwcl",
        "topstats_seasons": [
            {"season": "2025/2026", "season_id": 28395},
            {"season": "2024/2025", "season_id": 24233},
            {"season": "2023/2024", "season_id": 21127}
        ]
    },
    {
        "id": 9134,
        "name": "NWSL",
        "slug": "nwsl",
        "topstats_seasons": []
    }
]

TEAMS_TO_FETCH = [
    # Key benchmark teams
    {"id": 401657, "name": "Barcelona (W)", "slug": "barcelona_women"},
    {"id": 394119, "name": "OL Lyonnes (W)", "slug": "lyon_women"},
    {"id": 1075419, "name": "London City Lionesses (W)", "slug": "london_city_lionesses"},
    # All WSL Teams
    {"id": 258657, "name": "Arsenal (W)", "slug": "arsenal_women"},
    {"id": 258661, "name": "Chelsea (W)", "slug": "chelsea_women"},
    {"id": 231488, "name": "Manchester City (W)", "slug": "manchester_city_women"},
    {"id": 954396, "name": "Manchester United (W)", "slug": "manchester_united_women"},
    {"id": 258665, "name": "Liverpool (W)", "slug": "liverpool_women"},
    {"id": 231505, "name": "Brighton (W)", "slug": "brighton_women"},
    {"id": 231494, "name": "Aston Villa (W)", "slug": "aston_villa_women"},
    {"id": 258663, "name": "Everton (W)", "slug": "everton_women"},
    {"id": 628117, "name": "Tottenham Hotspur (W)", "slug": "tottenham_women"},
    {"id": 231497, "name": "West Ham United (W)", "slug": "west_ham_women"},
    {"id": 614828, "name": "Crystal Palace (W)", "slug": "crystal_palace_women"}
]

PLAYERS_TO_FETCH = [
    {"id": 829862, "name": "Mapi León", "slug": "mapi_leon"},
    {"id": 462289, "name": "Alexia Putellas", "slug": "alexia_putellas"},
    {"id": 938153, "name": "Mary Earps", "slug": "mary_earps"}
]


class FotMobIngester:
    def __init__(self, session: Optional[requests.Session] = None):
        self.session = session or requests.Session()
        self.session.headers.update(HEADERS)
        self.manifest: Dict[str, Any] = {
            "ingested_at": datetime.now(timezone.utc).isoformat(),
            "leagues": [],
            "teams": [],
            "players": [],
            "topstats": []
        }

    def _get_json(self, url: str, retries: int = 3, delay: float = 1.0) -> Optional[Dict[str, Any]]:
        for attempt in range(1, retries + 1):
            try:
                response = self.session.get(url, timeout=12)
                response.raise_for_status()
                return response.json()
            except Exception as e:
                logger.warning(f"Attempt {attempt}/{retries} failed for {url}: {e}")
                if attempt < retries:
                    time.sleep(delay * attempt)
        logger.error(f"Failed to fetch data from: {url}")
        return None

    def _save_json(self, data: Dict[str, Any], filepath: Path) -> bool:
        try:
            filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            logger.info(f"Saved raw payload -> {filepath.name} ({len(json.dumps(data))} bytes)")
            return True
        except Exception as e:
            logger.error(f"Failed to save JSON to {filepath}: {e}")
            return False

    def ingest_leagues(self):
        logger.info("=== Ingesting Leagues & TopStats ===")
        for league in LEAGUES_TO_FETCH:
            lid = league["id"]
            slug = league["slug"]
            
            # 1. League Overview & Table
            url = f"https://www.fotmob.com/api/data/leagues?id={lid}"
            data = self._get_json(url)
            if data:
                fp = FOTMOB_LEAGUES_DIR / f"league_{lid}_{slug}_overview.json"
                if self._save_json(data, fp):
                    self.manifest["leagues"].append({"id": lid, "name": league["name"], "path": str(fp)})
            time.sleep(0.5)

            # 2. League TopStats per season
            for s_info in league.get("topstats_seasons", []):
                season_id = s_info["season_id"]
                season_label = s_info["season"].replace("/", "_")
                ts_url = f"https://data.fotmob.com/stats/{lid}/season/{season_id}/topstats.json"
                ts_data = self._get_json(ts_url)
                if ts_data:
                    ts_fp = FOTMOB_LEAGUES_DIR / f"topstats_{slug}_{season_label}_{season_id}.json"
                    if self._save_json(ts_data, ts_fp):
                        self.manifest["topstats"].append({
                            "league": league["name"],
                            "season": s_info["season"],
                            "path": str(ts_fp)
                        })
                time.sleep(0.5)

    def ingest_teams(self):
        logger.info("=== Ingesting Teams Data ===")
        for team in TEAMS_TO_FETCH:
            tid = team["id"]
            slug = team["slug"]
            url = f"https://www.fotmob.com/api/data/teams?id={tid}"
            data = self._get_json(url)
            if data:
                fp = FOTMOB_TEAMS_DIR / f"team_{tid}_{slug}.json"
                if self._save_json(data, fp):
                    self.manifest["teams"].append({"id": tid, "name": team["name"], "path": str(fp)})
            time.sleep(0.5)

    def ingest_players(self):
        logger.info("=== Ingesting Key Players Data ===")
        for player in PLAYERS_TO_FETCH:
            pid = player["id"]
            slug = player["slug"]
            url = f"https://www.fotmob.com/api/data/playerData?id={pid}"
            data = self._get_json(url)
            if data:
                fp = FOTMOB_PLAYERS_DIR / f"player_{pid}_{slug}.json"
                if self._save_json(data, fp):
                    self.manifest["players"].append({"id": pid, "name": player["name"], "path": str(fp)})
            time.sleep(0.5)

    def write_manifest(self):
        manifest_path = FOTMOB_RAW_DIR / "fotmob_ingestion_manifest.json"
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(self.manifest, f, ensure_ascii=False, indent=2)
        logger.info(f"Manifest written successfully to: {manifest_path}")

    def run_all(self):
        ensure_all_directories()
        start_time = time.time()
        self.ingest_leagues()
        self.ingest_teams()
        self.ingest_players()
        self.write_manifest()
        duration = round(time.time() - start_time, 2)
        logger.info(f"Ingestion complete in {duration}s! Total files: {len(self.manifest['leagues']) + len(self.manifest['topstats']) + len(self.manifest['teams']) + len(self.manifest['players'])}")


if __name__ == "__main__":
    ingester = FotMobIngester()
    ingester.run_all()
