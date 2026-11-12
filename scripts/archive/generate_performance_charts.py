"""
WSL Data Hub - Performance Comparison Chart Generator
======================================================
Reads `_data/performance_evaluations.json` and creates dark-themed 
4-panel comparison charts for teams under `assets/images/evaluations/`.
"""

import os
import json
import argparse
import matplotlib.pyplot as plt

from paths import PERFORMANCE_EVAL_JSON, EVALUATIONS_CHARTS_DIR

DATA_FILE = PERFORMANCE_EVAL_JSON
CHARTS_DIR = EVALUATIONS_CHARTS_DIR
CHARTS_DIR.mkdir(parents=True, exist_ok=True)

def render_chart(team_eval, output_path):
    fig, axes = plt.subplots(2, 2, figsize=(12, 9), facecolor="#0f172a")
    plt.subplots_adjust(hspace=0.35, wspace=0.25)
    
    act = team_eval["actual_metrics"]
    exp = team_eval["expected_benchmarks"]
    delts = team_eval["deltas"]
    team_name = team_eval["name_en"]
    
    c_blue = "#38bdf8"
    c_purple = "#a855f7"
    c_emerald = "#10b981"
    c_coral = "#f43f5e"
    c_bg_card = "#1e293b"
    c_grid = "#334155"
    c_text = "#f8fafc"
    c_sub = "#94a3b8"
    
    fig.suptitle(f"{team_name} · Performance vs Baseline (2025/26)", 
                 fontsize=18, fontweight="bold", color=c_text, y=0.98)
    
    # 1. Goalkeeping (GA vs Expected GA)
    ax1 = axes[0, 0]
    ax1.set_facecolor(c_bg_card)
    cat1 = ['Actual GA\n(Conceded)', f'Expected GA\n(at {exp["league_avg_save_pct"]}% Save%)']
    val1 = [act['ga'], exp['exp_ga']]
    col1 = [c_coral if delts['ga_delta'] > 0 else c_emerald, "#64748b"]
    bars1 = ax1.bar(cat1, val1, color=col1, width=0.45, edgecolor="#0f172a", linewidth=1.5)
    ax1.set_title("1. Goalkeeping & Goals Conceded", fontsize=13, fontweight="bold", color=c_blue, pad=12)
    ax1.set_ylabel("Goals Conceded", fontsize=10, color=c_sub)
    ax1.tick_params(colors=c_text, labelsize=10)
    ax1.grid(axis='y', color=c_grid, linestyle='--', alpha=0.5)
    for b in bars1:
        yval = b.get_height()
        ax1.text(b.get_x() + b.get_width()/2.0, yval + 0.8, f"{yval:.1f}", ha='center', va='bottom', 
                 color=c_text, fontweight='bold', fontsize=11)
    diff_text1 = f"Delta: +{delts['ga_delta']:.1f} GA (Underperformance)" if delts['ga_delta'] > 0 else f"Delta: {delts['ga_delta']:.1f} GA (Solid)"
    ax1.text(0.5, -0.22, diff_text1, transform=ax1.transAxes, ha='center', fontsize=10, 
             fontweight='bold', color=c_coral if delts['ga_delta'] > 0 else c_emerald)

    # 2. Attack (GF vs Expected GF)
    ax2 = axes[0, 1]
    ax2.set_facecolor(c_bg_card)
    cat2 = ['Actual GF\n(Goals Scored)', f'Expected GF\n(from {act["sot"]} SoT)']
    val2 = [act['gf'], exp['exp_gf']]
    col2 = [c_emerald if delts['gf_delta'] >= 0 else c_coral, "#64748b"]
    bars2 = ax2.bar(cat2, val2, color=col2, width=0.45, edgecolor="#0f172a", linewidth=1.5)
    ax2.set_title("2. Attacking & Shot Conversion", fontsize=13, fontweight="bold", color=c_blue, pad=12)
    ax2.set_ylabel("Goals Scored", fontsize=10, color=c_sub)
    ax2.tick_params(colors=c_text, labelsize=10)
    ax2.grid(axis='y', color=c_grid, linestyle='--', alpha=0.5)
    for b in bars2:
        yval = b.get_height()
        ax2.text(b.get_x() + b.get_width()/2.0, yval + 0.8, f"{yval:.1f}", ha='center', va='bottom', 
                 color=c_text, fontweight='bold', fontsize=11)
    diff_text2 = f"Delta: {'+' if delts['gf_delta']>0 else ''}{delts['gf_delta']:.1f} GF"
    ax2.text(0.5, -0.22, diff_text2, transform=ax2.transAxes, ha='center', fontsize=10, 
             fontweight='bold', color=c_emerald if delts['gf_delta'] >= 0 else c_coral)

    # 3. Creation (Assists vs Expected Assists)
    ax3 = axes[1, 0]
    ax3.set_facecolor(c_bg_card)
    cat3 = ['Actual Assists\n(Ast)', f'Expected Assists\n(at {int(exp["league_avg_ast_per_gf"]*100)}% Goal Share)']
    val3 = [act['ast'], exp['exp_ast']]
    col3 = [c_emerald if delts['ast_delta'] >= 0 else c_coral, "#64748b"]
    bars3 = ax3.bar(cat3, val3, color=col3, width=0.45, edgecolor="#0f172a", linewidth=1.5)
    ax3.set_title("3. Chance Creation & Final Pass", fontsize=13, fontweight="bold", color=c_blue, pad=12)
    ax3.set_ylabel("Assists", fontsize=10, color=c_sub)
    ax3.tick_params(colors=c_text, labelsize=10)
    ax3.grid(axis='y', color=c_grid, linestyle='--', alpha=0.5)
    for b in bars3:
        yval = b.get_height()
        ax3.text(b.get_x() + b.get_width()/2.0, yval + 0.6, f"{yval:.1f}", ha='center', va='bottom', 
                 color=c_text, fontweight='bold', fontsize=11)
    diff_text3 = f"Delta: {'+' if delts['ast_delta']>0 else ''}{delts['ast_delta']:.1f} Ast"
    ax3.text(0.5, -0.22, diff_text3, transform=ax3.transAxes, ha='center', fontsize=10, 
             fontweight='bold', color=c_emerald if delts['ast_delta'] >= 0 else c_coral)

    # 4. Points (Actual Points vs xPTS)
    ax4 = axes[1, 1]
    ax4.set_facecolor(c_bg_card)
    cat4 = ['Actual Points\n(Final Standings)', 'Expected Points\n(xPTS from GD model)']
    val4 = [act['pts'], exp['exp_pts']]
    col4 = [c_purple if delts['pts_delta'] >= 0 else c_coral, "#64748b"]
    bars4 = ax4.bar(cat4, val4, color=col4, width=0.45, edgecolor="#0f172a", linewidth=1.5)
    ax4.set_title("4. Expected Points (xPTS Linear Model)", fontsize=13, fontweight="bold", color=c_blue, pad=12)
    ax4.set_ylabel("League Points", fontsize=10, color=c_sub)
    ax4.tick_params(colors=c_text, labelsize=10)
    ax4.grid(axis='y', color=c_grid, linestyle='--', alpha=0.5)
    for b in bars4:
        yval = b.get_height()
        ax4.text(b.get_x() + b.get_width()/2.0, yval + 0.8, f"{yval:.1f}", ha='center', va='bottom', 
                 color=c_text, fontweight='bold', fontsize=11)
    diff_text4 = f"Delta: {'+' if delts['pts_delta']>0 else ''}{delts['pts_delta']:.1f} Pts (Overperformance)" if delts['pts_delta'] > 0 else f"Delta: {delts['pts_delta']:.1f} Pts"
    ax4.text(0.5, -0.22, diff_text4, transform=ax4.transAxes, ha='center', fontsize=10, 
             fontweight='bold', color=c_purple if delts['pts_delta'] >= 0 else c_coral)

    plt.savefig(output_path, dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"[OK] Created chart: {output_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--team", type=str, default="all", help="Team slug or 'all'")
    args = parser.parse_args()
    
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        evaluations = json.load(f)
        
    if args.team == "all":
        for slug, data in evaluations.items():
            out_img = os.path.join(CHARTS_DIR, f"{slug}_performance_evaluation.png")
            render_chart(data, out_img)
    else:
        matched = False
        for slug, data in evaluations.items():
            if args.team.lower() in slug.lower():
                out_img = os.path.join(CHARTS_DIR, f"{slug}_performance_evaluation.png")
                render_chart(data, out_img)
                matched = True
                break
        if not matched:
            print(f"Team '{args.team}' not found in evaluations data.")

if __name__ == "__main__":
    main()
