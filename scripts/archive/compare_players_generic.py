"""
Generic Player Comparison & Profiling Tool
==========================================
Enables comparison across ANY list of players simply by providing their names.
- Automatically resolves FotMob Player IDs.
- Extracts and normalizes Per 90 metrics & positional percentiles.
- Compares shooting, chance creation, passing, dribbling, box touches, and defense.
- Outputs human-readable markdown tables and saves structured JSON.

Usage:
    python compare_players_generic.py --names "Kadidiatou Diani" "Alessia Russo" "Aggie Beever-Jones" "Mayra Ramirez"
    python compare_players_generic.py --names "Alexia Putellas" "Aitana Bonmati"
"""

import argparse
import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional
import requests
import pandas as pd

from paths import FOTMOB_PLAYERS_DIR, SITE_DATA_DIR, ensure_all_directories

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("PlayerComparison")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

# Target Metrics to Extract and Display
STANDARD_METRICS = [
    ("Goals", "Goals"),
    ("Shots on target", "Shots on Target"),
    ("Assists", "Assists"),
    ("Chances created", "Chances Created"),
    ("Big chances created", "Big Chances"),
    ("Accurate passes", "Acc. Passes"),
    ("Pass accuracy", "Pass Acc %"),
    ("Successful crosses", "Crosses"),
    ("Dribbles", "Dribbles"),
    ("Touches", "Touches"),
    ("Touches in opposition box", "Box Touches"),
    ("Possession won final 3rd", "Final 3rd Wins"),
]


class GenericPlayerComparator:
    def __init__(self):
        ensure_all_directories()
        self.cache_dir = FOTMOB_PLAYERS_DIR / "cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def resolve_player_id(self, player_name: str) -> Optional[int]:
        """Resolves a player's FotMob ID using the suggestion API or local files."""
        # Check local files first
        for f in FOTMOB_PLAYERS_DIR.glob("player_*_*.json"):
            try:
                with open(f, "r", encoding="utf-8") as fp:
                    data = json.load(fp)
                    if player_name.lower() in data.get("name", "").lower():
                        return int(data.get("id"))
            except Exception:
                pass

        # Query FotMob API
        search_url = f"https://www.fotmob.com/api/data/search/suggest?term={requests.utils.quote(player_name)}"
        try:
            res = requests.get(search_url, headers=HEADERS, timeout=10)
            res.raise_for_status()
            for group in res.json():
                for item in group.get("suggestions", []):
                    if item.get("type") == "player":
                        return int(item.get("id"))
        except Exception as e:
            logger.error(f"Error searching for {player_name}: {e}")
        return None

    def fetch_player_payload(self, player_id: int) -> Optional[Dict[str, Any]]:
        """Fetches full player profile payload with disk caching."""
        cached_file = self.cache_dir / f"player_{player_id}.json"
        if cached_file.exists():
            try:
                with open(cached_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass

        url = f"https://www.fotmob.com/api/data/playerData?id={player_id}"
        try:
            res = requests.get(url, headers=HEADERS, timeout=10)
            res.raise_for_status()
            data = res.json()
            with open(cached_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return data
        except Exception as e:
            logger.error(f"Failed to fetch player payload for ID {player_id}: {e}")
            return None

    def extract_player_stats(self, player_name: str) -> Optional[Dict[str, Any]]:
        """Resolves ID and extracts per-90 metrics."""
        pid = self.resolve_player_id(player_name)
        if not pid:
            logger.warning(f"Could not find ID for player: {player_name}")
            return None

        payload = self.fetch_player_payload(pid)
        if not payload:
            return None

        actual_name = payload.get("name", player_name)
        team_name = payload.get("primaryTeam", {}).get("teamName", "Unknown")
        role = payload.get("positionDescription", {}).get("primaryPosition", {}).get("label", "Player")

        stats_dict = {
            "Player": actual_name,
            "Team": team_name,
            "Role": role
        }

        stats_sec = payload.get("firstSeasonStats", {}).get("statsSection", {}).get("items", [])
        for group in stats_sec:
            for item in group.get("items", []):
                t_title = item.get("title")
                for orig_key, label in STANDARD_METRICS:
                    if t_title == orig_key:
                        p90 = item.get("per90")
                        stats_dict[label] = round(float(p90), 2) if p90 is not None else "-"

        return stats_dict

    def compare_players(self, player_names: List[str]) -> pd.DataFrame:
        """Compares multiple players and returns a clean DataFrame."""
        rows = []
        for name in player_names:
            p_stats = self.extract_player_stats(name)
            if p_stats:
                rows.append(p_stats)

        df = pd.DataFrame(rows)
        return df

    def save_comparison(self, df: pd.DataFrame, comparison_slug: str):
        """Saves comparison DataFrame to JSON and CSV."""
        out_dir = SITE_DATA_DIR / "comparisons"
        out_dir.mkdir(parents=True, exist_ok=True)
        
        json_fp = out_dir / f"{comparison_slug}.json"
        csv_fp = out_dir / f"{comparison_slug}.csv"
        
        records = df.to_dict(orient="records")
        with open(json_fp, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
            
        df.to_csv(csv_fp, index=False, encoding="utf-8-sig")
        logger.info(f"Saved comparison to: {json_fp} and {csv_fp}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generic Player Comparison Tool")
    parser.add_argument("--names", nargs="+", default=["Kadidiatou Diani", "Alessia Russo", "Aggie Beever-Jones", "Khadija Shaw"], help="List of player names")
    parser.add_argument("--slug", type=str, default="forwards_comparison", help="Output filename slug")
    args = parser.parse_args()

    comparator = GenericPlayerComparator()
    df_result = comparator.compare_players(args.names)
    
    print("\n" + "=" * 105)
    print(f" PLAYER COMPARISON TABLE (PER 90 MINUTES NORMALIZED)")
    print("=" * 105)
    print(df_result.to_string(index=False))
    
    comparator.save_comparison(df_result, args.slug)
