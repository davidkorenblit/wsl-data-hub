"""
FotMob Insights Fetcher: Mapi León & London City Lionesses (LCL)
================================================================
This script communicates directly with FotMob's internal JSON endpoints (HTTP requests)
to extract advanced metrics without HTML scraping:
1. Mapi León: Attacking actions, ball progression, chance creation, Per 90 stats & positional percentiles.
2. WSL / LCL 2025/2026 Team Stats: League-wide rankings for possession, pass accuracy, long balls, and chance creation.
"""

import json
import requests
from typing import Dict, Any, List, Optional


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}


def extract_mapi_leon_metrics(player_id: int = 829862) -> Dict[str, Any]:
    """
    Extracts Mapi León's player profile, Per 90 stats, and percentile rankings vs positional peers (Center-Backs).
    """
    url = f"https://www.fotmob.com/api/data/playerData?id={player_id}"
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    data = response.json()

    extracted = {
        "name": data.get("name", "Mapi León"),
        "primary_team": data.get("primaryTeam", {}).get("teamName"),
        "role": data.get("positionDescription", {}).get("primaryPosition", {}).get("label"),
        "overall_traits": [],
        "attacking_and_progression": []
    }

    # High-level traits
    traits = data.get("traits", {})
    if traits:
        for t in traits.get("items", []):
            extracted["overall_traits"].append({
                "trait": t.get("title"),
                "percentile": int(t.get("value", 0) * 100)
            })

    # Target metrics for deep ball progression and playmaking analysis
    target_keywords = [
        "chances created",
        "big chances created",
        "accurate passes",
        "pass accuracy",
        "accurate long balls",
        "long ball accuracy",
        "successful crosses",
        "cross accuracy",
        "touches",
        "possession won final 3rd",
        "shots",
        "recoveries",
        "dribbles"
    ]

    season_groups = data.get("firstSeasonStats", {}).get("statsSection", {}).get("items", [])
    for group in season_groups:
        category_name = group.get("title")
        for stat in group.get("items", []):
            title = stat.get("title", "")
            if any(k in title.lower() for k in target_keywords):
                extracted["attacking_and_progression"].append({
                    "category": category_name,
                    "metric": title,
                    "raw_total": stat.get("statValue"),
                    "per_90": round(float(stat.get("per90", 0)), 2) if stat.get("per90") is not None else None,
                    "percentile_rank_per_90": round(float(stat.get("percentileRankPer90", 0)), 1) if stat.get("percentileRankPer90") is not None else None
                })

    return extracted


def extract_lcl_and_wsl_metrics(season_id: int = 27506, league_id: int = 9227) -> Dict[str, Any]:
    """
    Extracts team rankings from the 2025/2026 WSL season (FotMob league stats)
    focusing on possession, progression, and chance creation metrics.
    """
    url = f"https://data.fotmob.com/stats/{league_id}/season/{season_id}/topstats.json"
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    data = response.json()

    categories_of_interest = {
        "possession_percentage_team": "Average Possession (%)",
        "accurate_pass_team": "Accurate Passes / Match",
        "accurate_long_balls_team": "Accurate Long Balls / Match",
        "touches_in_opp_box_team": "Touches in Opposition Box / Match",
        "big_chance_team": "Big Chances Created",
        "expected_goals_team": "Expected Goals (xG)",
        "poss_won_att_3rd_team": "Possession Won Final 3rd / Match"
    }

    team_comparisons = {}
    for top_list in data.get("TopLists", []):
        stat_name = top_list.get("StatName")
        if stat_name in categories_of_interest:
            friendly_name = categories_of_interest[stat_name]
            team_rankings = []
            for item in top_list.get("StatList", []):
                team_rankings.append({
                    "team_name": item.get("ParticipantName"),
                    "team_id": item.get("ParticiantId"),
                    "value": item.get("StatValue")
                })
            team_comparisons[friendly_name] = team_rankings

    return team_comparisons


def run_pipeline():
    print("=" * 75)
    print("1. Mapi León - Advanced Profile & Percentiles (vs Center-Backs)")
    print("=" * 75)
    mapi_data = extract_mapi_leon_metrics()
    print(f"Name: {mapi_data['name']} | Role: {mapi_data['role']} | Club: {mapi_data['primary_team']}\n")

    print("--- High-Level Traits (Percentiles vs Center-Backs) ---")
    for trait in mapi_data["overall_traits"]:
        print(f" * {trait['trait']:<25}: {trait['percentile']}th percentile")

    print("\n--- Detailed Progression & Playmaking Metrics (Per 90 + Percentiles) ---")
    for row in mapi_data["attacking_and_progression"]:
        cat = f"[{row['category']}]"
        per90_str = f"Per90: {row['per_90']:<6}" if row['per_90'] is not None else ""
        pct_str = f"Percentile: {row['percentile_rank_per_90']:>5}%" if row['percentile_rank_per_90'] is not None else ""
        print(f" {cat:<15} {row['metric']:<28} | {per90_str:<14} | {pct_str}")

    print("\n" + "=" * 75)
    print("2. WSL 2025/2026 Team Comparisons (Buildup & Chance Creation)")
    print("=" * 75)
    wsl_data = extract_lcl_and_wsl_metrics()
    for metric_name, rankings in wsl_data.items():
        print(f"\n>> Metric: {metric_name}")
        for idx, r in enumerate(rankings, 1):
            is_lcl = "London City Lionesses" in r["team_name"]
            marker = " <--- [LCL]" if is_lcl else ""
            print(f"   {idx:>2}. {r['team_name']:<30} : {r['value']}{marker}")


if __name__ == "__main__":
    run_pipeline()
