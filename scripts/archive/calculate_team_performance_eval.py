"""
WSL Data Hub - Performance Evaluation Engine
============================================
Calculates expected baselines and Over/Under performance for all WSL teams.
Includes:
- Expected Goals Conceded (xGA based on shots on target faced & league save %)
- Expected Goals (xGF based on shots on target & league conversion)
- Expected Assists (xAst based on goals scored & league assist ratio)
- Expected Points (xPTS based on goal difference regression)
- Possession-Adjusted Defensive Actions (PAdj Tackles + Interceptions vs League Baseline)

Saves structured JSON to `_data/performance_evaluations.json`.
"""

import os
import json
import numpy as np
import pandas as pd
from calculate_baseline_metrics import load_data, calculate_metrics
from paths import LEAGUE_TABLE_RAW_CSV, TEAMS_METADATA_JSON, PERFORMANCE_EVAL_JSON, SITE_DATA_DIR

SITE_DATA_DIR.mkdir(parents=True, exist_ok=True)

def load_team_metadata():
    with open(TEAMS_METADATA_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def compute_performance_evaluations():
    # 1. Base merged metrics from calculate_baseline_metrics
    df = calculate_metrics()
    
    # 2. Add League Standings / Points
    tbl_df = pd.read_csv(LEAGUE_TABLE_RAW_CSV)
    df = df.merge(tbl_df[['Squad', 'Pts', 'Rk']].rename(columns={'Squad': 'squad'}), on='squad', how='left')
    
    # 3. Add Raw Counts needed for weighted benchmarks
    _, _, shoot, gk, _, _ = load_data()
    df['sota_total'] = pd.to_numeric(gk['performance_sota'], errors='coerce')
    df['saves_total'] = pd.to_numeric(gk['performance_saves'], errors='coerce')
    df['sot_total'] = pd.to_numeric(shoot['standard_sot'], errors='coerce')
    
    # --- League Benchmarks ---
    total_league_sota = df['sota_total'].sum()
    total_league_saves = df['saves_total'].sum()
    league_avg_save_pct = total_league_saves / total_league_sota  # ~0.6546
    
    total_league_sot = df['sot_total'].sum()
    total_league_gf = df['gf'].sum()
    league_avg_g_per_sot = total_league_gf / total_league_sot    # ~0.315
    
    total_league_ast = df['ast'].sum()
    league_avg_ast_per_gf = total_league_ast / total_league_gf   # ~0.76
    
    # Linear Regression for Expected Points (xPTS) from Goal Difference (GD)
    slope, intercept = np.polyfit(df['gd'], df['Pts'], 1)
    
    # Possession-Adjusted Defensive Actions Benchmark
    df['opp_poss'] = 100.0 - df['poss_pct']
    df['padj_def_actions'] = (df['tklw_plus_int'] / (df['opp_poss'] / 50.0)).round(1)
    league_padj_avg = round(float(df['padj_def_actions'].mean()), 1)

    team_meta = load_team_metadata()
    evaluations = {}
    
    for _, row in df.iterrows():
        squad_name = row['squad']
        meta = team_meta.get(squad_name, {
            "slug": squad_name.lower().replace(" ", "-"),
            "name_he": squad_name,
            "name_en": squad_name
        })
        
        # Expected metrics
        exp_ga = round(row['sota_total'] * (1.0 - league_avg_save_pct), 1)
        ga_delta = round(row['ga'] - exp_ga, 1) # Positive = Conceded MORE than expected (Underperformance)
        
        exp_gf = round(row['sot_total'] * league_avg_g_per_sot, 1)
        gf_delta = round(row['gf'] - exp_gf, 1) # Positive = Scored MORE than expected (Overperformance)
        
        exp_ast = round(row['gf'] * league_avg_ast_per_gf, 1)
        ast_delta = round(row['ast'] - exp_ast, 1)
        
        exp_pts = round(slope * row['gd'] + intercept, 1)
        pts_delta = round(row['Pts'] - exp_pts, 1)

        def_delta = round(row['padj_def_actions'] - league_padj_avg, 1)
        
        evaluations[meta['slug']] = {
            "squad": squad_name,
            "team_slug": meta['slug'],
            "name_he": meta['name_he'],
            "name_en": meta['name_en'],
            "rank": int(row['Rk']),
            "actual_metrics": {
                "pts": int(row['Pts']),
                "gd": int(row['gd']),
                "gf": int(row['gf']),
                "ga": int(row['ga']),
                "sota": int(row['sota_total']),
                "save_pct": float(row['save_pct']),
                "sot": int(row['sot_total']),
                "sot_pct": float(row['sot_pct']),
                "ast": int(row['ast']),
                "poss": float(row['poss_pct']),
                "tklw_plus_int": int(row['tklw_plus_int']),
                "padj_def_actions": float(row['padj_def_actions'])
            },
            "expected_benchmarks": {
                "exp_ga": exp_ga,
                "exp_gf": exp_gf,
                "exp_ast": exp_ast,
                "exp_pts": exp_pts,
                "exp_padj_def": league_padj_avg,
                "league_avg_save_pct": round(league_avg_save_pct * 100, 1),
                "league_avg_g_per_sot": round(league_avg_g_per_sot, 2),
                "league_avg_ast_per_gf": round(league_avg_ast_per_gf, 2),
                "league_pts_slope": round(slope, 3),
                "league_pts_intercept": round(intercept, 2)
            },
            "deltas": {
                "ga_delta": ga_delta,
                "gf_delta": gf_delta,
                "ast_delta": ast_delta,
                "pts_delta": pts_delta,
                "def_delta": def_delta
            }
        }
        
    with open(PERFORMANCE_EVAL_JSON, "w", encoding="utf-8") as f:
        json.dump(evaluations, f, ensure_ascii=False, indent=2)
        
    print(f"[OK] Successfully computed performance evaluations for {len(evaluations)} teams.")
    print(f"[OK] Saved to: {PERFORMANCE_EVAL_JSON}")
    return evaluations

if __name__ == "__main__":
    compute_performance_evaluations()
