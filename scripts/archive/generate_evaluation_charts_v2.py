"""
WSL Data Hub - Minimalist Lollipop Delta Chart Generator
========================================================
Generates a super-clean, minimalist Lollipop Chart for London City Lionesses.
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


def generate_lollipop_delta_chart():
    """Generates an ultra-clean, minimalist Lollipop Chart with zero clutter."""
    with open(PERFORMANCE_EVAL_JSON, "r", encoding="utf-8") as f:
        evals = json.load(f)

    lcl = evals["london-city-lionesses"]
    deltas = lcl["deltas"]

    # 4 Core Metrics
    metrics = [
        {"name": "Points (xPTS)", "val": deltas["pts_delta"], "is_pos_good": True, "label": f"+{deltas['pts_delta']:.1f} Pts"},
        {"name": "Goals Scored (GF)", "val": deltas["gf_delta"], "is_pos_good": True, "label": f"{deltas['gf_delta']:.1f} Gls"},
        {"name": "Assists (Ast)", "val": deltas["ast_delta"], "is_pos_good": True, "label": f"{deltas['ast_delta']:.1f} Ast"},
        {"name": "Goals Conceded (GA)", "val": deltas["ga_delta"], "is_pos_good": False, "label": f"+{deltas['ga_delta']:.1f} GA (Excess)"},
    ]

    fig, ax = plt.subplots(figsize=(10, 4.8), facecolor=BG_COLOR)
    ax.set_facecolor(CARD_BG)

    y_pos = np.arange(len(metrics))
    vals = [m["val"] for m in metrics]
    labels = [m["name"] for m in metrics]

    # Center baseline (Zero)
    ax.axvline(0, color="#64748b", linewidth=1.5, linestyle="--", zorder=2)

    for y, m in zip(y_pos, metrics):
        val = m["val"]
        is_ga = not m["is_pos_good"]
        
        # Color: For GA, positive is bad (Red). For others, positive is good (Green).
        if is_ga:
            color = CORAL_RED if val > 0 else EMERALD_GREEN
        else:
            color = EMERALD_GREEN if val > 0 else CORAL_RED

        # 1. Lollipop Stem (Thin Line)
        ax.hlines(y=y, xmin=0, xmax=val, color=color, linewidth=3, zorder=3, alpha=0.9)

        # 2. Lollipop Head (Circle Marker)
        ax.scatter(val, y, color=color, s=280, zorder=4, edgecolor=BG_COLOR, linewidth=2)

        # 3. Clean value label next to the circle
        offset = 0.55 if val >= 0 else -0.55
        ha = "left" if val >= 0 else "right"
        
        ax.text(
            val + offset,
            y,
            m["label"],
            color=TEXT_COLOR,
            fontsize=11.5,
            fontweight="bold",
            va="center",
            ha=ha,
            zorder=5
        )

    # Y-Axis Labels (Clean and well spaced)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, color=TEXT_COLOR, fontsize=12, fontweight="medium")
    ax.invert_yaxis()

    ax.set_xlim(-6.5, 10.5)
    ax.set_xlabel("Deviation from League Expected Baseline (Delta)", color=SUB_TEXT, fontsize=11, labelpad=10)
    ax.set_title("London City Lionesses · Performance vs Baseline", color=TEXT_COLOR, fontsize=15, fontweight="bold", pad=16)

    # Background grid & borders
    ax.grid(axis="x", color=GRID_COLOR, linestyle=":", alpha=0.7, zorder=1)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(GRID_COLOR)
    ax.spines["bottom"].set_color(GRID_COLOR)
    ax.tick_params(colors=SUB_TEXT)

    out_path = EVALUATIONS_CHARTS_DIR / "lcl_performance_deltas.png"
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, facecolor=BG_COLOR, bbox_inches="tight")
    plt.close()
    print(f"[OK] Generated Minimalist Lollipop Chart: {out_path}")


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
    print(f"[OK] Generated Goalkeeper Chart: {out_path}")


if __name__ == "__main__":
    generate_lollipop_delta_chart()
    generate_goalkeeper_chart_and_data()
