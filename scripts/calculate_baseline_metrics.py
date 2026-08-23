"""
WSL Data Hub - Question 1: Squad Baseline Metrics Calculator
=============================================================
This script calculates all available baseline metrics for the 12 WSL teams
and generates a comparative analysis for any selected team (default: London City Lionesses).
"""

import os
import sys
import json
import argparse
import pandas as pd
import numpy as np

from paths import SQUADS_DIR, OPPONENTS_DIR, LEAGUE_DIR, BASELINE_SUMMARY_JSON, ASSETS_DATA_DIR, SITE_DATA_DIR

def load_data():
    std = pd.read_csv(LEAGUE_DIR / "wsl_standard_squad.csv")
    std_opp = pd.read_csv(OPPONENTS_DIR / "wsl_standard_opponent.csv")
    shoot = pd.read_csv(LEAGUE_DIR / "wsl_shooting_squad.csv")
    gk = pd.read_csv(LEAGUE_DIR / "wsl_goalkeeping_squad.csv")
    misc = pd.read_csv(LEAGUE_DIR / "wsl_misc_squad.csv")
    poss = pd.read_csv(SQUADS_DIR / "wsl_possession_squad.csv")
    
    return std, std_opp, shoot, gk, misc, poss

def calculate_metrics():
    std, std_opp, shoot, gk, misc, poss = load_data()
    
    df = pd.DataFrame()
    df['squad'] = std['squad'].str.strip()
    
    # 1. Attacking Metrics
    df['gf'] = pd.to_numeric(std['performance_gls'], errors='coerce')
    df['gf_per90'] = pd.to_numeric(std['per_90_minutes_gls'], errors='coerce')
    df['sh_per90'] = pd.to_numeric(shoot['standard_sh/90'], errors='coerce')
    df['sot_pct'] = pd.to_numeric(shoot['standard_sot%'], errors='coerce')
    df['g_per_sh'] = pd.to_numeric(shoot['standard_g/sh'], errors='coerce')
    
    # 2. Chance Creation (Assists & Key Volume)
    df['ast'] = pd.to_numeric(std['performance_ast'], errors='coerce')
    df['ast_per90'] = pd.to_numeric(std['per_90_minutes_ast'], errors='coerce')
    
    # 3. Defensive Solidity
    df['ga'] = pd.to_numeric(std_opp['performance_gls'], errors='coerce')
    df['ga_per90'] = pd.to_numeric(std_opp['per_90_minutes_gls'], errors='coerce')
    sota = pd.to_numeric(gk['performance_sota'], errors='coerce')
    ninety = pd.to_numeric(gk['playing_time_90s'], errors='coerce')
    df['sota_per90'] = (sota / ninety).round(2)
    df['save_pct'] = pd.to_numeric(gk['performance_save%'], errors='coerce')
    
    tklw = pd.to_numeric(misc['performance_tklw'], errors='coerce')
    intercept = pd.to_numeric(misc['performance_int'], errors='coerce')
    df['tklw_plus_int'] = tklw + intercept
    
    # 4. Macro Metrics
    df['gd'] = df['gf'] - df['ga']
    df['poss_pct'] = pd.to_numeric(poss['poss'], errors='coerce')
    
    return df

def generate_report(df, target_team="Lionesses"):
    print("=" * 85)
    print(f"WSL 2025/26 - SQUAD BASELINE COMPARISON TABLE (ALL 12 TEAMS)")
    print("=" * 85)
    display_cols = ['squad', 'gf', 'sh_per90', 'sot_pct', 'g_per_sh', 'ast', 'ga', 'sota_per90', 'save_pct', 'tklw_plus_int', 'poss_pct', 'gd']
    print(df[display_cols].to_string(index=False))
    
    # Filter target team
    matches = df[df['squad'].str.contains(target_team, case=False, na=False)]
    if len(matches) == 0:
        print(f"\nError: Team matching '{target_team}' not found!")
        return
    team_row = matches.iloc[0]
    actual_team_name = team_row['squad']
    
    print("\n" + "=" * 85)
    print(f"{actual_team_name.upper()} - DETAILED RANKINGS & LEAGUE BENCHMARKS")
    print("=" * 85)
    
    metrics_to_rank = [
        ('gf', 'Goals Scored (GF)', False),
        ('gf_per90', 'Goals / 90 (GF/90)', False),
        ('sh_per90', 'Shots / 90 (Sh/90)', False),
        ('sot_pct', 'Shots on Target % (SoT%)', False),
        ('g_per_sh', 'Goal Efficiency (G/Sh)', False),
        ('ast', 'Assists (Ast - Chance Creation)', False),
        ('ast_per90', 'Assists / 90 (Ast/90)', False),
        ('ga', 'Goals Conceded (GA)', True),
        ('ga_per90', 'Goals Conceded / 90 (GA/90)', True),
        ('sota_per90', 'Shots on Target Allowed / 90 (SoTA/90)', True),
        ('save_pct', 'Save Percentage (Save%)', False),
        ('tklw_plus_int', 'Tackles Won + Interceptions (TklW+Int)', False),
        ('poss_pct', 'Possession % (Poss%)', False),
        ('gd', 'Goal Difference (GD)', False),
    ]
    
    rankings = {}
    for col, label, ascending in metrics_to_rank:
        ranked = df.sort_values(by=col, ascending=ascending).reset_index(drop=True)
        rank = int(ranked[ranked['squad'] == actual_team_name].index[0] + 1)
        val = float(team_row[col]) if pd.notnull(team_row[col]) else None
        league_avg = round(float(df[col].mean()), 2)
        best_team = ranked.iloc[0]['squad']
        best_val = ranked.iloc[0][col]
        if pd.notnull(best_val):
            best_val = float(best_val) if isinstance(best_val, (np.floating, float)) else int(best_val)
        
        rankings[col] = {
            'label': label,
            'team_value': val,
            'rank': rank,
            'total_teams': len(df),
            'league_avg': league_avg,
            'best_team': str(best_team),
            'best_value': best_val
        }
        
        print(f"{label:<42} | {actual_team_name}: {val:>6} | Rank: {rank:>2}/12 | League Avg: {league_avg:>6} | Best: {best_team} ({best_val})")

    # Possession Breakdown: Big 3 vs Rest of League
    big3_teams = ['Chelsea', 'Arsenal', 'Manchester City']
    big3_df = df[df['squad'].isin(big3_teams)]
    rest_df = df[~df['squad'].isin(big3_teams)]
    
    big3_poss_avg = round(float(big3_df['poss_pct'].mean()), 2)
    rest_poss_avg = round(float(rest_df['poss_pct'].mean()), 2)
    
    rest_ranked = rest_df.sort_values(by='poss_pct', ascending=False).reset_index(drop=True)
    in_rest = actual_team_name in rest_df['squad'].values
    rest_rank_str = f"#{int(rest_ranked[rest_ranked['squad'] == actual_team_name].index[0] + 1)} out of 9 teams" if in_rest else "Part of Big 3"
    
    print("\n" + "=" * 85)
    print("POSSESSION SEGMENTATION: BIG 3 vs REST OF THE LEAGUE")
    print("=" * 85)
    print(f"Big 3 (Chelsea, Arsenal, Man City) Avg Possession: {big3_poss_avg}%")
    print(f"Rest of League (9 teams) Avg Possession:          {rest_poss_avg}%")
    print(f"{actual_team_name} Possession:                          {team_row['poss_pct']}%")
    print(f"{actual_team_name} Rank among Rest of League (non-Big 3): {rest_rank_str}")
    
    # Save output to JSON
    out_data = {
        'target_team': actual_team_name,
        'all_teams': json.loads(df.to_json(orient='records')),
        'rankings': rankings,
        'possession_breakdown': {
            'big3_avg': big3_poss_avg,
            'rest_avg': rest_poss_avg,
            'team_value': float(team_row['poss_pct']),
            'team_rank_in_rest': rest_rank_str
        }
    }
    
    SITE_DATA_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    with open(BASELINE_SUMMARY_JSON, "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)
        
    with open(ASSETS_DATA_DIR / "baseline_q1_summary.json", "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)
        
    print(f"\nSaved summary JSON to {BASELINE_SUMMARY_JSON}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate WSL Baseline Metrics")
    parser.add_argument("--team", type=str, default="Lionesses", help="Target team name to rank (default: Lionesses)")
    args = parser.parse_args()
    
    df = calculate_metrics()
    generate_report(df, target_team=args.team)
