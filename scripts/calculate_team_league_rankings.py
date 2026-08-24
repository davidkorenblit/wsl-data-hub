"""
Generic League Team Ranking & Tactical Profiler
===============================================
Calculates full league rankings, values, percentiles, and gap-to-leader
across all key metrics (buildup, possession, passing, chance creation, defense)
for ANY team and season in the WSL or UWCL.

Saves structured outputs to:
- `data/teams/{team_slug}/{season_label}_league_rankings.json`
- `_data/{team_slug}_league_rankings.json`
"""

import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional
import requests

from paths import (
    FOTMOB_RAW_DIR,
    FOTMOB_LEAGUES_DIR,
    DATA_DIR,
    SITE_DATA_DIR,
    ensure_all_directories
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("TeamRankings")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

# The core tactical & statistical categories for team evaluation
CORE_TEAM_METRICS = {
    # Possession & Buildup
    "possession_percentage_team": {"title": "Average Possession (%)", "category": "Possession & Buildup", "higher_is_better": True},
    "accurate_pass_team": {"title": "Accurate Passes / Match", "category": "Possession & Buildup", "higher_is_better": True},
    "accurate_long_balls_team": {"title": "Accurate Long Balls / Match", "category": "Possession & Buildup", "higher_is_better": True},
    "accurate_cross_team": {"title": "Accurate Crosses / Match", "category": "Possession & Buildup", "higher_is_better": True},
    
    # Chance Creation & Attack
    "expected_goals_team": {"title": "Expected Goals (xG)", "category": "Chance Creation", "higher_is_better": True},
    "_xg_diff_team": {"title": "xG Difference", "category": "Chance Creation", "higher_is_better": True},
    "big_chance_team": {"title": "Big Chances Created", "category": "Chance Creation", "higher_is_better": True},
    "touches_in_opp_box_team": {"title": "Touches in Opp Box", "category": "Chance Creation", "higher_is_better": True},
    "ontarget_scoring_att_team": {"title": "Shots on Target / Match", "category": "Chance Creation", "higher_is_better": True},
    "goals_team_match": {"title": "Goals / Match", "category": "Chance Creation", "higher_is_better": True},
    "big_chance_missed_team": {"title": "Big Chances Missed", "category": "Chance Creation", "higher_is_better": False},

    # Defensive & Pressing Actions
    "poss_won_att_3rd_team": {"title": "Possession Won Final 3rd / Match", "category": "Pressing & Defense", "higher_is_better": True},
    "total_tackle_team": {"title": "Tackles / Match", "category": "Pressing & Defense", "higher_is_better": True},
    "interception_team": {"title": "Interceptions / Match", "category": "Pressing & Defense", "higher_is_better": True},
    "effective_clearance_team": {"title": "Clearances / Match", "category": "Pressing & Defense", "higher_is_better": True},
    "expected_goals_conceded_team": {"title": "xG Conceded", "category": "Pressing & Defense", "higher_is_better": False},
    "clean_sheet_team": {"title": "Clean Sheets", "category": "Pressing & Defense", "higher_is_better": True},
    "rating_team": {"title": "FotMob Team Rating", "category": "Overall Performance", "higher_is_better": True}
}


class TeamLeagueRankingsCalculator:
    def __init__(self, league_id: int = 9227, season_id: int = 27506, season_name: str = "2025/2026"):
        self.league_id = league_id
        self.season_id = season_id
        self.season_name = season_name
        self.stats_cache_dir = FOTMOB_LEAGUES_DIR / "stat_leaderboards"
        self.stats_cache_dir.mkdir(parents=True, exist_ok=True)

    def fetch_stat_leaderboard(self, stat_name: str) -> Optional[List[Dict[str, Any]]]:
        """
        Fetches or loads from cache the full 12-team leaderboard for a specific metric.
        """
        cached_file = self.stats_cache_dir / f"{self.league_id}_{self.season_id}_{stat_name}.json"
        
        # Check local cache first
        if cached_file.exists():
            try:
                with open(cached_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("TopLists", [])[0].get("StatList", [])
            except Exception as e:
                logger.warning(f"Cache read error for {cached_file}: {e}")

        # Fetch from FotMob API
        url = f"https://data.fotmob.com/stats/{self.league_id}/season/{self.season_id}/{stat_name}.json"
        try:
            res = requests.get(url, headers=HEADERS, timeout=10)
            res.raise_for_status()
            data = res.json()
            with open(cached_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return data.get("TopLists", [])[0].get("StatList", [])
        except Exception as e:
            logger.error(f"Failed to fetch leaderboard for {stat_name}: {e}")
            return None

    def calculate_team_profile(self, target_team_name: str = "London City Lionesses") -> Dict[str, Any]:
        """
        Calculates all ranks, values, percentiles, and benchmarks for the target team.
        """
        team_profile: Dict[str, Any] = {
            "team_name": target_team_name,
            "league_id": self.league_id,
            "season": self.season_name,
            "season_id": self.season_id,
            "metrics": []
        }

        for stat_key, meta in CORE_TEAM_METRICS.items():
            leaderboard = self.fetch_stat_leaderboard(stat_key)
            if not leaderboard:
                continue

            total_teams = len(leaderboard)
            values = [float(row.get("StatValue", 0)) for row in leaderboard if row.get("StatValue") is not None]
            
            # Find target team
            target_entry = None
            for row in leaderboard:
                p_name = row.get("ParticipantName", "")
                if target_team_name.lower() in p_name.lower() or p_name.lower() in target_team_name.lower():
                    target_entry = row
                    break

            if not target_entry:
                logger.warning(f"Team '{target_team_name}' not found in leaderboard '{stat_key}'")
                continue

            rank = int(target_entry.get("Rank", 0))
            team_val = float(target_entry.get("StatValue", 0))
            leader_val = float(leaderboard[0].get("StatValue", 0))
            leader_team = leaderboard[0].get("ParticipantName")

            avg_val = round(sum(values) / len(values), 2) if values else 0
            
            # Percentile rank (100% = top rank)
            if meta["higher_is_better"]:
                percentile = round(((total_teams - rank + 1) / total_teams) * 100, 1)
                gap_to_leader = round(team_val - leader_val, 2)
            else:
                percentile = round(((rank) / total_teams) * 100, 1)
                gap_to_leader = round(leader_val - team_val, 2)

            team_profile["metrics"].append({
                "stat_key": stat_key,
                "title": meta["title"],
                "category": meta["category"],
                "rank": rank,
                "total_teams": total_teams,
                "team_value": team_val,
                "league_average": avg_val,
                "league_leader": {
                    "team": leader_team,
                    "value": leader_val
                },
                "gap_to_leader": gap_to_leader,
                "percentile": percentile
            })

        return team_profile

    def save_and_export(self, profile: Dict[str, Any], team_slug: str = "london_city_lionesses"):
        ensure_all_directories()
        
        # Save to team folder
        team_out_dir = DATA_DIR / "teams" / team_slug
        team_out_dir.mkdir(parents=True, exist_ok=True)
        season_clean = self.season_name.replace("/", "_")
        team_file = team_out_dir / f"{season_clean}_fotmob_rankings.json"
        
        with open(team_file, "w", encoding="utf-8") as f:
            json.dump(profile, f, ensure_ascii=False, indent=2)
        logger.info(f"Saved team profile to: {team_file}")

        # Also save to site _data
        site_file = SITE_DATA_DIR / f"{team_slug}_fotmob_rankings.json"
        with open(site_file, "w", encoding="utf-8") as f:
            json.dump(profile, f, ensure_ascii=False, indent=2)
        logger.info(f"Saved site data to: {site_file}")


def print_formatted_profile(profile: Dict[str, Any]):
    print("\n" + "=" * 90)
    print(f" TACTICAL RANKING & PERFORMANCE PROFILE: {profile['team_name'].upper()}")
    print(f" Season: {profile['season']} | League: WSL (ID: {profile['league_id']})")
    print("=" * 90)

    current_cat = ""
    for m in profile["metrics"]:
        if m["category"] != current_cat:
            current_cat = m["category"]
            print(f"\n--- {current_cat} ---")
            print(f"{'Metric':<34} | {'Value':<7} | {'Rank':<8} | {'Percentile':<11} | {'League Avg':<10} | {'Leader':<18}")
            print("-" * 90)

        rank_str = f"#{m['rank']} / {m['total_teams']}"
        pct_str = f"{m['percentile']}%"
        leader_str = f"{m['league_leader']['team'][:12]} ({m['league_leader']['value']})"
        print(f"{m['title']:<34} | {m['team_value']:<7} | {rank_str:<8} | {pct_str:<11} | {m['league_average']:<10} | {leader_str}")


if __name__ == "__main__":
    calculator = TeamLeagueRankingsCalculator(league_id=9227, season_id=27506, season_name="2025/2026")
    
    # 1. Run for London City Lionesses
    lcl_profile = calculator.calculate_team_profile(target_team_name="London City Lionesses")
    calculator.save_and_export(lcl_profile, team_slug="london_city_lionesses")
    print_formatted_profile(lcl_profile)
