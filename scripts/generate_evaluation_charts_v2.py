"""
WSL Data Hub - Refined Evaluation Visualizations
===============================================
Generates two high-impact charts for London City Lionesses evaluation:
1. lcl_performance_deltas.png - Clean Diverging delta chart (No text overlap).
2. lcl_goalkeeper_evaluation.png - Goalkeeper performance comparison across WSL.
Also exports `_data/goalkeeping_squad.json` for Jekyll web rendering.
"""

import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path

from paths import PERFORMANCE_EVAL_JSON, EVALUATIONS_CHARTS_DIR, LEAGUE_DIR, SITE_DATA_DIR

EVALUATIONS_CHARTS_DIR.mkdir(parents=True, exist_ok=True)
SITE_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Aesthetic Theme Tokens
BG_COLOR = "#0b1329"
CARD_BG = "#131f3d"
TEXT_COLOR = "#f8fafc"
SUB_TEXT = "#94a3b8"
GRID_COLOR = "#1e293b"
CORAL_RED = "#f43f5e"
EMERALD_GREEN = "#10b981"
ACCENT_BLUE = "#38bdf8"
ACCENT_GOLD = "#fbbf24"


def generate_delta_chart():
    """Generates the Diverging Bar / Delta Chart for London City Lionesses without text overlap."""
    with open(PERFORMANCE_EVAL_JSON, "r", encoding="utf-8") as f:
        evals = json.load(f)

    lcl = evals["london-city-lionesses"]
    deltas = lcl["deltas"]

    metrics = [
        {"name": "Points (xPTS Delta)\nWinning tight games", "val": deltas["pts_delta"], "label": f"+{deltas['pts_delta']:.1f} Pts (Overperformed)", "is_positive_good": True},
        {"name": "Goals Scored (GF Delta)\nFinishing vs Shot volume", "val": deltas["gf_delta"], "label": f"{deltas['gf_delta']:.1f} Goals (Underperformed)", "is_positive_good": True},
        {"name": "Assists (Ast Delta)\nDirect chance conversion", "val": deltas["ast_delta"], "label": f"{deltas['ast_delta']:.1f} Assists (Underperformed)", "is_positive_good": True},
        {"name": "Goals Conceded (GA Delta)\nExcess goals allowed", "val": deltas["ga_delta"], "label": f"+{deltas['ga_delta']:.1f} GA (Weak Goalkeeping)", "is_positive_good": False},
    ]

    fig, ax = plt.subplots(figsize=(11, 5.5), facecolor=BG_COLOR)
    ax.set_facecolor(CARD_BG)

    y_pos = np.arange(len(metrics))
    vals = [m["val"] for m in metrics]
    labels = [m["name"] for m in metrics]

    colors = []
    for m in metrics:
        if "Goals Conceded" in m["name"]:
            colors.append(CORAL_RED if m["val"] > 0 else EMERALD_GREEN)
        else:
            colors.append(EMERALD_GREEN if m["val"] > 0 else CORAL_RED)

    bars = ax.barh(y_pos, vals, color=colors, height=0.48, edgecolor="none", zorder=3)

    # Center baseline
    ax.axvline(0, color="#64748b", linewidth=1.5, linestyle="--", zorder=4)

    # Value annotations placed with ample padding
    for bar, m in zip(bars, metrics):
        val = m["val"]
        width = bar.get_width()
        
        # Position label outside the bar with clear spacing
        if val >= 0:
            text_x = width + 0.4
            ha = "left"
        else:
            text_x = width - 0.4
            ha = "right"

        ax.text(
            text_x,
            bar.get_y() + bar.get_height() / 2,
            m["label"],
            va="center",
            ha=ha,
            color=TEXT_COLOR,
            fontsize=11,
            fontweight="bold",
        )

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, color=TEXT_COLOR, fontsize=11, fontweight="medium")
    ax.invert_yaxis()

    ax.set_xlim(-7.5, 11)
    ax.set_xlabel("Statistical Deviation from League Expected Baseline (Delta)", color=SUB_TEXT, fontsize=11, labelpad=12)
    ax.set_title("London City Lionesses · Actual Performance vs Expected Baseline", color=TEXT_COLOR, fontsize=15, fontweight="bold", pad=18)

    ax.grid(axis="x", color=GRID_COLOR, linestyle=":", alpha=0.8, zorder=1)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(GRID_COLOR)
    ax.spines["bottom"].set_color(GRID_COLOR)
    ax.tick_params(colors=SUB_TEXT)

    out_path = EVALUATIONS_CHARTS_DIR / "lcl_performance_deltas.png"
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, facecolor=BG_COLOR)
    plt.close()
    print(f"[OK] Generated: {out_path}")


def generate_goalkeeper_chart_and_data():
    """Generates the Goalkeeper chart and exports JSON table data."""
    df_gk = pd.read_csv(LEAGUE_DIR / "wsl_goalkeeping_squad.csv")
    
    # Export full JSON for Jekyll Table rendering
    json_path = SITE_DATA_DIR / "goalkeeping_squad.json"
    gk_records = df_gk.to_dict(orient="records")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(gk_records, f, ensure_ascii=False, indent=2)
    print(f"[OK] Exported goalkeeping JSON data to: {json_path}")

    # Generate visual chart
    df_sorted = df_gk.sort_values(by="performance_save%", ascending=True).reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(11, 7), facecolor=BG_COLOR)
    ax.set_facecolor(CARD_BG)

    squads = df_sorted["squad"].tolist()
    save_pcts = df_sorted["performance_save%"].tolist()
    sota = df_sorted["performance_sota"].tolist()
    ga = df_sorted["performance_ga"].tolist()

    y_pos = np.arange(len(squads))

    colors = [CORAL_RED if s == "Lionesses" else ("#f59e0b" if s in ["Aston Villa", "West Ham"] else ACCENT_BLUE) for s in squads]
    bars = ax.barh(y_pos, save_pcts, color=colors, height=0.55, zorder=3)

    league_avg = 66.2
    top3_avg = 73.9
    ax.axvline(league_avg, color=ACCENT_GOLD, linestyle="--", linewidth=1.5, label=f"League Average ({league_avg}%)", zorder=4)
    ax.axvline(top3_avg, color=EMERALD_GREEN, linestyle=":", linewidth=1.5, label=f"Top 3 Benchmark ({top3_avg}%)", zorder=4)

    for bar, pct, s, shots, conceded in zip(bars, save_pcts, squads, sota, ga):
        highlight_suffix = " ◄ (Elena / LCL - Ranked #11/12)" if s == "Lionesses" else f" ({conceded} GA / {shots} SoTA)"
        ax.text(
            pct + 0.8,
            bar.get_y() + bar.get_height() / 2,
            f"{pct:.1f}%{highlight_suffix}",
            va="center",
            ha="left",
            color=CORAL_RED if s == "Lionesses" else TEXT_COLOR,
            fontsize=10,
            fontweight="bold" if s == "Lionesses" else "normal",
        )

    ax.set_yticks(y_pos)
    ax.set_yticklabels(squads, color=TEXT_COLOR, fontsize=11, fontweight="medium")
    ax.set_xlim(45, 86)
    ax.set_xlabel("Save Percentage (Save %)", color=SUB_TEXT, fontsize=12, labelpad=10)
    ax.set_title("WSL Goalkeeping Rankings · Save % Across All 12 Teams", color=TEXT_COLOR, fontsize=16, fontweight="bold", pad=20)

    ax.legend(facecolor=CARD_BG, edgecolor=GRID_COLOR, labelcolor=TEXT_COLOR, loc="lower right", fontsize=10)

    ax.grid(axis="x", color=GRID_COLOR, linestyle=":", alpha=0.8, zorder=1)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(GRID_COLOR)
    ax.spines["bottom"].set_color(GRID_COLOR)
    ax.tick_params(colors=SUB_TEXT)

    out_path = EVALUATIONS_CHARTS_DIR / "lcl_goalkeeper_evaluation.png"
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, facecolor=BG_COLOR)
    plt.close()
    print(f"[OK] Generated: {out_path}")


if __name__ == "__main__":
    generate_delta_chart()
    generate_goalkeeper_chart_and_data()
