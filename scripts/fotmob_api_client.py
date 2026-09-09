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
    ASSETS_DATA_DIR,
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

# Standard Team ID to Slug Mapping for Jekyll Routing
TEAM_ID_TO_SLUG = {
    258661: "chelsea",
    231488: "manchester-city",
    258657: "arsenal",
    258665: "liverpool",
    258658: "birmingham-city",
    258663: "everton",
    231497: "west-ham",
    231505: "brighton",
    628117: "tottenham",
    954396: "manchester-utd",
    614828: "crystal-palace",
    231494: "aston-villa",
    231502: "charlton-athletic",
    1075419: "london-city-lionesses",
    231508: "leicester-city",
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

    def fetch_league_raw(self, league_id: int = 9227, season: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """Fetch raw league overview including standings, tabs, and matches/fixtures."""
        url = f"https://www.fotmob.com/api/data/leagues?id={league_id}"
        if season:
            from urllib.parse import quote
            url += f"&season={quote(season)}"
        return self._get(url)

    def parse_league_table(self, raw_league_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract and normalize league table standings for WSL Data Hub."""
        table_list = []
        raw_tables = raw_league_data.get("table", [])
        if not raw_tables:
            return table_list
        
        all_rows = raw_tables[0].get("data", {}).get("table", {}).get("all", [])
        for row in all_rows:
            team_id = row.get("id")
            team_name = row.get("name", "")
            slug = TEAM_ID_TO_SLUG.get(team_id, team_name.lower().replace(" ", "-"))

            # Parse goals from scoresStr (e.g. "3-1") or fallback fields
            scores_str = row.get("scoresStr", "0-0")
            gf, ga = 0, 0
            if scores_str and "-" in scores_str:
                parts = scores_str.split("-")
                try:
                    gf = int(parts[0])
                    ga = int(parts[1])
                except (ValueError, IndexError):
                    pass
            elif "goalsScored" in row:
                gf = int(row.get("goalsScored", 0))
                ga = gf - int(row.get("goalConDiff", 0))

            table_list.append({
                "rk": row.get("idx"),
                "squad": team_name,
                "slug": slug,
                "mp": int(row.get("played", 0)),
                "w": int(row.get("wins", 0)),
                "d": int(row.get("draws", 0)),
                "l": int(row.get("losses", 0)),
                "gf": gf,
                "ga": ga,
                "gd": int(row.get("goalConDiff", 0)),
                "pts": int(row.get("pts", 0))
            })
        return table_list

    def parse_league_matches(self, raw_league_data: Dict[str, Any], only_finished: bool = False) -> List[Dict[str, Any]]:
        """Extract and normalize all matches and fixtures for WSL."""
        matches_list = []
        # FotMob API returns matches under 'fixtures.allMatches'
        fixtures = raw_league_data.get("fixtures", {})
        raw_matches = fixtures.get("allMatches", [])
        # Fallback: old structure used 'matches.allMatches'
        if not raw_matches:
            raw_matches = raw_league_data.get("matches", {}).get("allMatches", [])
        for m in raw_matches:
            status = m.get("status", {})
            finished = status.get("finished", False)
            if only_finished and not finished:
                continue

            home = m.get("home", {})
            away = m.get("away", {})
            score_str = status.get("scoreStr")
            home_score = None
            away_score = None
            if score_str and "-" in score_str:
                parts = score_str.split("-")
                try:
                    home_score = int(parts[0].strip())
                    away_score = int(parts[1].strip())
                except (ValueError, IndexError):
                    pass

            matches_list.append({
                "id": m.get("id"),
                "round": m.get("round"),
                "date": status.get("utcTime"),
                "home": home.get("name"),
                "home_id": home.get("id"),
                "home_score": home_score,
                "away": away.get("name"),
                "away_id": away.get("id"),
                "away_score": away_score,
                "score": score_str,
                "finished": finished,
                "started": status.get("started", False),
                "reason": status.get("reason", {}).get("short") if status.get("reason") else None
            })
        return matches_list

    def update_wsl_live_data(self, season: Optional[str] = None) -> Dict[str, Any]:
        """
        Pull latest WSL data from FotMob and update all Jekyll and Assets datasets:
        1. Saves raw payload to data/raw/fotmob/leagues/league_9227_wsl_overview.json
        2. Updates _data/league_table.json and assets/data/league_table.json
        3. Saves all fixtures/matches to _data/wsl_matches.json
        4. Saves completed match results to _data/wsl_recent_results.json
        """
        logger.info(f"Fetching latest WSL league data (Season: {season or 'current'})...")
        raw_data = self.fetch_league_raw(league_id=9227, season=season)
        if not raw_data:
            logger.error("Failed to fetch WSL league data from FotMob.")
            return {}

        # 1. Save Raw Payload
        raw_path = FOTMOB_LEAGUES_DIR / "league_9227_wsl_overview.json"
        self.save_json(raw_data, raw_path)

        # 2. Parse & Save Standings Table
        table = self.parse_league_table(raw_data)
        if table:
            self.save_json(table, SITE_DATA_DIR / "league_table.json")
            self.save_json(table, ASSETS_DATA_DIR / "league_table.json")
            logger.info(f"Updated league standings table: {len(table)} teams. Leader: {table[0]['squad']} ({table[0]['pts']} pts)")

        # 3. Parse & Save Matches
        all_matches = self.parse_league_matches(raw_data)
        finished_matches = [m for m in all_matches if m.get("finished")]
        if all_matches:
            self.save_json(all_matches, SITE_DATA_DIR / "wsl_matches.json")
            self.save_json(finished_matches, SITE_DATA_DIR / "wsl_recent_results.json")
            logger.info(f"Extracted {len(all_matches)} total matches ({len(finished_matches)} completed).")

        return {
            "teams_count": len(table),
            "total_matches": len(all_matches),
            "finished_matches": len(finished_matches),
            "leader": table[0]["squad"] if table else None
        }

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
        raw_traits = raw_player_data.get("traits") or {}
        for t in raw_traits.get("items", []):
            traits.append({
                "title": t.get("title"),
                "percentile": int(round(t.get("value", 0) * 100))
            })
            
        stats_sections = []
        first_season = raw_player_data.get("firstSeasonStats") or {}
        stats_sec = first_season.get("statsSection") or {}
        season_groups = stats_sec.get("items", [])
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
    parser.add_argument("--update-wsl", action="store_true", help="Sync latest WSL standings and match results")
    parser.add_argument("--season", type=str, help="Season string (e.g. 2026/2027)")
    args = parser.parse_args()

    client = FotMobAPIClient()

    if args.update_wsl:
        summary = client.update_wsl_live_data(season=args.season)
        logger.info(f"WSL live data sync finished: {summary}")
        return

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
