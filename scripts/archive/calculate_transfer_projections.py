"""
WSL Transfer Projections & Season Forecast Engine
=================================================
Calculates the Net Additive Value of transfers and projects season performance (GF, GA, GD, xPTS, League Rank).
"""

import json
import logging
from pathlib import Path
from typing import Dict, Any

from paths import SITE_DATA_DIR, ensure_all_directories

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("TransferProjections")


def calculate_london_city_projections() -> Dict[str, Any]:
    ensure_all_directories()

    # 1. Baseline Season (2024/25 - 22 Matches)
    baseline_22 = {
        "matches": 22,
        "points": 27,
        "rank": 6,
        "gf": 26,
        "ga": 33,
        "gd": -7,
        "shots_on_target_for": 91,
        "shots_on_target_against": 96,
        "save_pct": 64.9,
        "assists": 18
    }

    # Normalized to 26 matches (14 teams in 2025/26) without transfers
    baseline_26 = {
        "matches": 26,
        "gf": round(baseline_22["gf"] * (26 / 22), 1),      # 30.7
        "ga": round(baseline_22["ga"] * (26 / 22), 1),      # 39.0
        "gd": round(baseline_22["gd"] * (26 / 22), 1),      # -8.3
        "points": round(baseline_22["points"] * (26 / 22), 1) # 31.9
    }

    # 2. Transfer Delta Calculations
    # Defense & Goalkeeping Savings (GA reduction)
    earps_ga_prevented = 8.5   # Based on 76.8% save rate & +4.8 PSxG over 26 matches
    mapi_def_ga_prevented = 3.5 # Based on possession dominance, box suppression & high recoveries
    total_ga_saved = earps_ga_prevented + mapi_def_ga_prevented # 12.0

    # Attacking & Midfield Boost (GF increase)
    alexia_direct_g = 11.5     # 0.56 / 90
    alexia_direct_a = 7.5      # 0.43 / 90
    diani_direct_g = 10.0      # 0.54 / 90
    diani_direct_a = 4.5       # 0.22 / 90
    mapi_set_piece_creation = 3.5

    # Net Goal Output (Adjusted for team possession rebalancing & cannibalization)
    net_gf_added = 18.5        # Net increase above baseline

    # 3. Projected 2025/26 Totals
    proj_ga = round(baseline_26["ga"] - total_ga_saved, 1)  # 39.0 - 12.0 = 27.0
    proj_gf = round(baseline_26["gf"] + net_gf_added, 1)    # 30.7 + 18.5 = 49.2
    proj_gd = round(proj_gf - proj_ga, 1)                   # +22.2

    # 4. xPTS Model (WSL empirical regression scaled to 26 games)
    # Model: Base pts for 0 GD is ~36.6 pts, with 0.576 slope per GD unit
    proj_xpts = round(36.6 + (0.576 * proj_gd), 1)          # ~49.4 pts (Range: 47 - 52)
    xpts_range = [round(proj_xpts - 2.5), round(proj_xpts + 2.5)]

    # 5. League Benchmark Comparison (2025/26 Projections)
    league_landscape = [
        {"team": "Chelsea", "proj_xpts": 58, "proj_rank": 1, "tier": "Title Contender"},
        {"team": "Arsenal", "proj_xpts": 53, "proj_rank": 2, "tier": "Title Contender / UWCL"},
        {"team": "Manchester City", "proj_xpts": 51, "proj_rank": 3, "tier": "UWCL Spot"},
        {"team": "London City Lionesses (Projected)", "proj_xpts": round(proj_xpts), "proj_rank": 3.5, "tier": "UWCL Battle (Top 3-4)"},
        {"team": "Manchester United", "proj_xpts": 41, "proj_rank": 5, "tier": "Upper Midtable"},
        {"team": "Tottenham", "proj_xpts": 33, "proj_rank": 6, "tier": "Midtable"}
    ]

    result = {
        "team_slug": "london-city-lionesses",
        "team_name": "London City Lionesses",
        "baseline_2024_25": baseline_22,
        "baseline_scaled_26": baseline_26,
        "transfer_deltas": {
            "ga_reduction": total_ga_saved,
            "gf_increase": net_gf_added,
            "earps_ga_saved": earps_ga_prevented,
            "mapi_def_savings": mapi_def_ga_prevented,
            "alexia_goals_projected": alexia_direct_g,
            "diani_goals_projected": diani_direct_g,
            "alexia_assists_projected": alexia_direct_a,
            "diani_assists_projected": diani_direct_a,
            "mapi_assists_projected": mapi_set_piece_creation
        },
        "projections_2025_26": {
            "matches": 26,
            "projected_gf": proj_gf,
            "projected_ga": proj_ga,
            "projected_gd": proj_gd,
            "projected_xpts": proj_xpts,
            "xpts_range": xpts_range,
            "projected_rank": "3-4 (UWCL Qualification Contender)"
        },
        "league_landscape": league_landscape
    }

    # Save to Site Data
    out_dir = SITE_DATA_DIR / "projections"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "london_city_lionesses.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    logger.info(f"Saved projections to: {out_path}")

    return result


if __name__ == "__main__":
    data = calculate_london_city_projections()
    print("\n" + "=" * 80)
    print(" LONDON CITY LIONESSES - 2025/26 SEASON PROJECTION SUMMARY")
    print("=" * 80)
    b = data["baseline_2024_25"]
    p = data["projections_2025_26"]
    d = data["transfer_deltas"]
    print(f" Matches:          22 (2024/25) -> 26 (2025/26)")
    print(f" Goals Scored (GF): {b['gf']} -> {p['projected_gf']} (+{d['gf_increase']} Gls)")
    print(f" Goals Conceded (GA): {b['ga']} -> {p['projected_ga']} (-{d['ga_reduction']} GA Saved)")
    print(f" Goal Difference (GD): {b['gd']} -> +{p['projected_gd']} (+{round(p['projected_gd'] - b['gd'], 1)} Delta)")
    print(f" Projected xPTS:   {b['points']} Pts -> {p['projected_xpts']} Pts (Range: {p['xpts_range'][0]}-{p['xpts_range'][1]} Pts)")
    print(f" Projected Finish: 6th -> {p['projected_rank']}")
    print("=" * 80)
