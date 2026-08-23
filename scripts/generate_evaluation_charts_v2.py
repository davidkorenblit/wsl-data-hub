"""
WSL Data Hub - Refined Evaluation Visualizations (Fixed Layout)
===============================================================
Generates clean, collision-free charts for London City Lionesses evaluation:
1. lcl_performance_deltas.png - Clean horizontal diverging bar chart with zero text overlap.
2. lcl_goalkeeper_evaluation.png - Goalkeeper performance comparison across WSL.
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
    """Generates the Diverging Bar / Delta Chart with titles above bars to eliminate text collisions."""
    with open(PERFORMANCE_EVAL_JSON, "r", encoding="utf-8") as f:
        evals = json.load(f)

    lcl = evals["london-city-lionesses"]
    deltas = lcl["deltas"]

    items = [
        {
            "title": "1. Points Delta (xPTS vs Actual)",
            "subtitle": "Winning close/clutch matches",
            "val": deltas["pts_delta"],
            "unit": "Pts",
            "is_positive_good": True,
            "note": "Overperformed (+1.2 Pts)"
        },
        {
            "title": "2. Goals Scored Delta (GF vs xG Expected)",
            "subtitle": "Finishing efficiency vs shot volume",
            "val": deltas["gf_delta"],
            "unit": "Goals",
            "is_positive_good": True,
            "note": "Underperformed (-3.7 Goals)"
        },
        {
            "title": "3. Assists Delta (Ast vs Expected)",
            "subtitle": "Direct playmaking & chance conversion",
            "val": deltas["ast_delta"],
            "unit": "Assists",
            "is_positive_good": True,
            "note": "Underperformed (-0.9 Ast)"
        },
        {
            "title": "4. Goals Conceded Delta (GA vs xGA Expected)",
            "subtitle": "Excess goals allowed (Goalkeeping gap)",
            "val": deltas["ga_delta"],
            "unit": "Goals",
            "is_positive_good": False,
            "note": "Excess Goals Conceded (+6.7 GA)"
        },
    ]

    fig, ax = plt.subplots(figsize=(11, 6.5), facecolor=BG_COLOR)
    ax.set_facecolor(CARD_BG)

    y_positions = [3.3, 2.2, 1.1, 0.0]
    
    # Draw bars
    for y, item in zip(y_positions, items):
        val = item["val"]
        is_ga = not item["is_positive_good"]
        
        # Color decision
        if is_ga:
            color = CORAL_RED if val > 0 else EMERALD_GREEN
        else:
            color = EMERALD_GREEN if val > 0 else CORAL_RED

        # Bar
        ax.barh(y, val, height=0.38, color=color, zorder=3, edgecolor="none")

        # Category title & subtitle above the bar
        ax.text(-9.5, y + 0.32, item["title"], color=TEXT_COLOR, fontsize=12, fontweight="bold", va="center", ha="left")
        ax.text(-9.5, y + 0.18, item["subtitle"], color=SUB_TEXT, fontsize=9.5, va="center", ha="left")

        # Value annotation at the tip of the bar
        sign = "+" if val > 0 else ""
        if val >= 0:
            text_x = val + 0.35
            ha = "left"
        else:
            text_x = val - 0.35
            ha = "right"

        ax.text(
            text_x,
            y,
            f"{sign}{val:.1f} {item['unit']} · {item['note']}",
            color=TEXT_COLOR,
            fontsize=11,
            fontweight="bold",
            va="center",
            ha=ha,
            zorder=5
        )

    # Center baseline (0)
    ax.axvline(0, color="#64748b", linewidth=1.5, linestyle="--", zorder=4)

    # Set limits and clean axis
    ax.set_xlim(-10, 12)
    ax.set_ylim(-0.4, 3.8)
    ax.set_yticks([])  # Remove Y tick labels completely to avoid overlap!

    ax.set_xlabel("Deviation from League Expected Baseline (Delta)", color=SUB_TEXT, fontsize=11, labelpad=12)
    ax.set_title("London City Lionesses · Actual Performance vs Expected Baseline", color=TEXT_COLOR, fontsize=15, fontweight="bold", pad=20)

    ax.grid(axis="x", color=GRID_COLOR, linestyle=":", alpha=0.8, zorder=1)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color(GRID_COLOR)
    ax.tick_params(colors=SUB_TEXT)

    out_path = EVALUATIONS_CHARTS_DIR / "lcl_performance_deltas.png"
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, facecolor=BG_COLOR, bbox_inches="tight")
    plt.close()
    print(f"[OK] Generated clean delta chart: {out_path}")


def generate_goalkeeper_chart_and_data():
    """Generates the Goalkeeper chart and exports JSON table data."""
    df_gk = pd.read_csv(LEAGUE_DIR / "wsl_goalkeeping_squad.csv")
    
    json_path = SITE_DATA_DIR / "goalkeeping_squad.json"
    gk_records = df_gk.to_dict(orient="records")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(gk_records, f, ensure_ascii=False, indent=2)

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
    plt.savefig(out_path, dpi=200, facecolor=BG_COLOR, bbox_inches="tight")
    plt.close()
    print(f"[OK] Generated: {out_path}")


if __name__ == "__main__":
    generate_delta_chart()
    generate_goalkeeper_chart_and_data()
