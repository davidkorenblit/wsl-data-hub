"""
WSL Data Hub - Refined Evaluation Visualizations
===============================================
Generates two high-impact charts for London City Lionesses evaluation:
1. lcl_performance_deltas.png - Diverging delta chart (Actual vs Expected).
2. lcl_goalkeeper_evaluation.png - Goalkeeper performance comparison across WSL.
"""

import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path

from paths import PERFORMANCE_EVAL_JSON, EVALUATIONS_CHARTS_DIR, LEAGUE_DIR

EVALUATIONS_CHARTS_DIR.mkdir(parents=True, exist_ok=True)

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
    """Generates the Diverging Bar / Delta Chart for London City Lionesses."""
    with open(PERFORMANCE_EVAL_JSON, "r", encoding="utf-8") as f:
        evals = json.load(f)

    lcl = evals["london-city-lionesses"]
    deltas = lcl["deltas"]

    metrics = [
        {"name": "Points (xPTS Delta)\n(Clutch / Winning close games)", "val": deltas["pts_delta"], "is_positive_good": True},
        {"name": "Goals Scored (GF Delta)\n(Finishing vs Shot Volume)", "val": deltas["gf_delta"], "is_positive_good": True},
        {"name": "Assists (Ast Delta)\n(Direct chance conversion)", "val": deltas["ast_delta"], "is_positive_good": True},
        {"name": "Goals Conceded (GA Delta)\n(Conceded MORE than expected)", "val": deltas["ga_delta"], "is_positive_good": False},
    ]

    fig, ax = plt.subplots(figsize=(10, 6), facecolor=BG_COLOR)
    ax.set_facecolor(CARD_BG)

    y_pos = np.arange(len(metrics))
    vals = [m["val"] for m in metrics]
    labels = [m["name"] for m in metrics]

    # Color logic: for Points/GF/Ast positive is good (Green), negative is bad (Red).
    # For GA, positive means conceded MORE (Bad -> Red).
    colors = []
    for m in metrics:
        if m["name"].startswith("Goals Conceded"):
            colors.append(CORAL_RED if m["val"] > 0 else EMERALD_GREEN)
        else:
            colors.append(EMERALD_GREEN if m["val"] > 0 else CORAL_RED)

    bars = ax.barh(y_pos, vals, color=colors, height=0.55, edgecolor="none", zorder=3)

    # Center baseline
    ax.axvline(0, color="#64748b", linewidth=1.5, linestyle="--", zorder=4)

    # Value annotations
    for bar, val, m in zip(bars, vals, metrics):
        width = bar.get_width()
        sign = "+" if val > 0 else ""
        text_x = width + (0.3 if val >= 0 else -0.3)
        ha = "left" if val >= 0 else "right"
        
        status_label = ""
        if m["name"].startswith("Goals Conceded"):
            status_label = " (Excess GA: Poor Goalkeeping)"
        elif val > 0:
            status_label = " (Overperformed)"
        else:
            status_label = " (Underperformed)"

        ax.text(
            text_x,
            bar.get_y() + bar.get_height() / 2,
            f"{sign}{val:.1f}{status_label}",
            va="center",
            ha=ha,
            color=TEXT_COLOR,
            fontsize=11,
            fontweight="bold",
        )

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, color=TEXT_COLOR, fontsize=12, fontweight="medium")
    ax.invert_yaxis()  # Top to bottom

    ax.set_xlim(-6, 9)
    ax.set_xlabel("Deviation from League Expected Baseline (Delta)", color=SUB_TEXT, fontsize=11, labelpad=10)
    ax.set_title("London City Lionesses · Performance vs Expected Baseline", color=TEXT_COLOR, fontsize=16, fontweight="bold", pad=20)

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


def generate_goalkeeper_chart():
    """Generates the Goalkeeper league-wide evaluation chart."""
    df_gk = pd.read_csv(LEAGUE_DIR / "wsl_goalkeeping_squad.csv")
    df_gk = df_gk.sort_values(by="performance_save%", ascending=True).reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(11, 7), facecolor=BG_COLOR)
    ax.set_facecolor(CARD_BG)

    squads = df_gk["squad"].tolist()
    save_pcts = df_gk["performance_save%"].tolist()
    sota = df_gk["performance_sota"].tolist()
    ga = df_gk["performance_ga"].tolist()

    y_pos = np.arange(len(squads))

    # Highlight Lionesses in bright Coral, others in Slate
    colors = [CORAL_RED if s == "Lionesses" else ("#f59e0b" if s in ["Aston Villa", "West Ham"] else ACCENT_BLUE) for s in squads]

    bars = ax.barh(y_pos, save_pcts, color=colors, height=0.6, zorder=3)

    # Benchmark lines
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
    ax.set_xlim(45, 85)
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
    generate_goalkeeper_chart()
