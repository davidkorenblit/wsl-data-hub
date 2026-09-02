"""
WSL Data Hub - Generic FotMob Ingestion & Analysis Engine
=========================================================
A standardized, robust client for extracting teams, squads, player traits,
advanced percentiles, league topstats, and transfer histories.

Includes predefined WSL team IDs and season mappings:
- Baseline / Completed Season: 2025/2026
- Active / Target Season: 2026/2027
"""

import json
import logging
import argparse
from pathlib import Path
from typing import Dict, Any, List, Optional
import requests

from paths import (
    FOTMOB_RAW_DIR,
    FOTMOB_TEAMS_DIR,
    FOTMOB_PLAYERS_DIR,
    FOTMOB_LEAGUES_DIR,
    SITE_DATA_DIR,
    SITE_SQUADS_DIR,
    ensure_all_directories
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("FotMobClient")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

# Standard Team ID Registry
WSL_TEAMS = {
    "tottenham": {"id": 628117, "name": "Tottenham Hotspur Women", "slug": "tottenham"},
    "arsenal": {"id": 258657, "name": "Arsenal Women", "slug": "arsenal"},
    "chelsea": {"id": 258661, "name": "Chelsea Women", "slug": "chelsea"},
    "manchester_city": {"id": 231488, "name": "Manchester City Women", "slug": "manchester-city"},
    "manchester_united": {"id": 954396, "name": "Manchester United Women", "slug": "manchester-utd"},
    "liverpool": {"id": 258665, "name": "Liverpool Women", "slug": "liverpool"},
    "brighton": {"id": 231505, "name": "Brighton Women", "slug": "brighton"},
    "aston_villa": {"id": 231494, "name": "Aston Villa Women", "slug": "aston-villa"},
    "everton": {"id": 258663, "name": "Everton Women", "slug": "everton"},
    "west_ham": {"id": 231497, "name": "West Ham United Women", "slug": "west-ham"},
    "crystal_palace": {"id": 614828, "name": "Crystal Palace Women", "slug": "crystal-palace"},
    "london_city": {"id": 1075419, "name": "London City Lionesses", "slug": "london-city-lionesses"},
    "barcelona": {"id": 401657, "name": "Barcelona Femení", "slug": "barcelona"},
    "lyon": {"id": 394119, "name": "Lyon Féminin", "slug": "lyon"}
}

# Standard League & Season ID Registry
LEAGUES = {
    "wsl": {
        "id": 9227,
        "name": "WSL",
        "seasons": {
            "2026/2027": 31000, # upcoming/active
            "2025/2026": 27506, # completed/baseline
            "2024/2025": 23925
        }
    },
    "uwcl": {
        "id": 9375,
        "name": "UWCL",
        "seasons": {
            "2025/2026": 28395,
            "2024/2025": 24233
        }
    }
}


class FotMobAPIClient:
    def __init__(self, timeout: int = 15):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.timeout = timeout
        ensure_all_directories()

    def _get(self, url: str) -> Optional[Dict[str, Any]]:
        try:
            res = self.session.get(url, timeout=self.timeout)
            res.raise_for_status()
            return res.json()
        except Exception as e:
            logger.error(f"Request failed for {url}: {e}")
            return None

    def fetch_team_raw(self, team_id: int) -> Optional[Dict[str, Any]]:
        url = f"https://www.fotmob.com/api/data/teams?id={team_id}"
        return self._get(url)

    def fetch_player_raw(self, player_id: int) -> Optional[Dict[str, Any]]:
        url = f"https://www.fotmob.com/api/data/playerData?id={player_id}"
        return self._get(url)

    def fetch_league_topstats(self, league_id: int, season_id: int) -> Optional[Dict[str, Any]]:
        url = f"https://data.fotmob.com/stats/{league_id}/season/{season_id}/topstats.json"
        return self._get(url)

    def parse_squad(self, raw_team_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        squad_list = []
        raw_squad = raw_team_data.get("squad", {}).get("squad", [])
        
        for section in raw_squad:
            role_title = section.get("title", "")
            if role_title.lower() == "coach":
                continue
            for m in section.get("members", []):
                role_info = m.get("role", {})
                pos_label = role_info.get("fallback") or role_title
                
                pos_short = "MF"
                if "keeper" in pos_label.lower():
                    pos_short = "GK"
                elif "defender" in pos_label.lower() or "back" in pos_label.lower():
                    pos_short = "DF"
                elif "forward" in pos_label.lower() or "striker" in pos_label.lower() or "winger" in pos_label.lower():
                    pos_short = "FW"
                elif "midfielder" in pos_label.lower():
                    pos_short = "MF"
                    
                squad_list.append({
                    "id": m.get("id"),
                    "player": m.get("name"),
                    "pos": pos_short,
                    "role_detailed": pos_label,
                    "age": str(m.get("age", "")),
                    "nation": f"{m.get('ccode', '').lower()} {m.get('cname', '')}",
                    "cname": m.get("cname", "")
                })
        return squad_list

    def parse_player_metrics(self, raw_player_data: Dict[str, Any]) -> Dict[str, Any]:
        traits = []
        for t in raw_player_data.get("traits", {}).get("items", []):
            traits.append({
                "title": t.get("title"),
                "percentile": int(round(t.get("value", 0) * 100))
            })
            
        stats_sections = []
        season_groups = raw_player_data.get("firstSeasonStats", {}).get("statsSection", {}).get("items", [])
        for group in season_groups:
            grp_title = group.get("title")
            items = []
            for stat in group.get("items", []):
                items.append({
                    "metric": stat.get("title"),
                    "stat_value": stat.get("statValue"),
                    "per_90": round(float(stat.get("per90", 0)), 2) if stat.get("per90") is not None else None,
                    "percentile_rank": round(float(stat.get("percentileRankPer90", 0)), 1) if stat.get("percentileRankPer90") is not None else None
                })
            stats_sections.append({
                "section": grp_title,
                "stats": items
            })
            
        return {
            "id": raw_player_data.get("id"),
            "name": raw_player_data.get("name"),
            "primary_position": raw_player_data.get("positionDescription", {}).get("primaryPosition", {}).get("label"),
            "traits": traits,
            "stats_sections": stats_sections
        }

    def save_json(self, data: Any, filepath: Path) -> bool:
        try:
            filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            logger.info(f"Saved: {filepath}")
            return True
        except Exception as e:
            logger.error(f"Error saving to {filepath}: {e}")
            return False


def main():
    parser = argparse.ArgumentParser(description="FotMob Generic WSL Data Pipeline")
    parser.add_argument("--team", type=str, help="Team slug (e.g. tottenham, arsenal, chelsea)")
    parser.add_argument("--player-id", type=int, help="FotMob player ID")
    parser.add_argument("--save-squad", action="store_true", help="Save squad to _data/squads/")
    args = parser.parse_args()

    client = FotMobAPIClient()

    if args.team:
        slug = args.team.lower().replace("-", "_")
        if slug in WSL_TEAMS:
            team_meta = WSL_TEAMS[slug]
            logger.info(f"Fetching team data for {team_meta['name']} (ID: {team_meta['id']})...")
            raw_team = client.fetch_team_raw(team_meta["id"])
            if raw_team:
                squad = client.parse_squad(raw_team)
                logger.info(f"Extracted {len(squad)} squad members.")
                if args.save_squad:
                    out_path = SITE_SQUADS_DIR / f"{team_meta['slug']}_2026_27.json"
                    client.save_json(squad, out_path)
        else:
            logger.error(f"Unknown team slug: {args.team}. Available: {list(WSL_TEAMS.keys())}")

    if args.player_id:
        logger.info(f"Fetching player data for ID: {args.player_id}...")
        raw_player = client.fetch_player_raw(args.player_id)
        if raw_player:
            metrics = client.parse_player_metrics(raw_player)
            logger.info(f"Player: {metrics['name']} | Role: {metrics['primary_position']}")
            for t in metrics["traits"]:
                logger.info(f"  Trait: {t['title']} -> {t['percentile']}%")


if __name__ == "__main__":
    main()
