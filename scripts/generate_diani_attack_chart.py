"""
WSL Data Hub - Diani Attack & Wingers Comparison Chart Generator
================================================================
Generates high-resolution aesthetic comparison charts for Kadidiatou Diani
benchmarked against the top WSL wide & central forwards (James, Hemp, Mead, Smith, Thompson, Russo, Shaw, Hanson).
"""

import json
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from paths import ASSETS_IMAGES_DIR, SITE_DATA_DIR, ensure_all_directories

# Aesthetics Tokens
BG_COLOR = "#0b1329"
CARD_BG = "#131f3d"
TEXT_COLOR = "#f8fafc"
SUB_TEXT = "#94a3b8"
GRID_COLOR = "#1e293b"
CYAN_ACCENT = "#00B0C7"
GOLD_ACCENT = "#fbbf24"
ROSE_ACCENT = "#f43f5e"
EMERALD_ACCENT = "#10b981"
MUTED_SLATE = "#64748b"


def generate_diani_comparison_chart():
    ensure_all_directories()
    out_dir = ASSETS_IMAGES_DIR / "evaluations"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "diani_attack_comparison.png"

    # Data for the benchmark (Per 90 normalized)
    players_data = [
        {"player": "K. Diani", "team": "LCL / Lyon", "is_diani": True, "goals": 0.54, "big_chances": 0.54, "box_touches": 7.52, "crosses": 1.42, "final_3rd_wins": 1.42},
        {"player": "L. James", "team": "Chelsea", "is_diani": False, "goals": 0.58, "big_chances": 0.81, "box_touches": 4.83, "crosses": 2.30, "final_3rd_wins": 1.38},
        {"player": "L. Hemp", "team": "Man City", "is_diani": False, "goals": 0.07, "big_chances": 0.98, "box_touches": 6.96, "crosses": 2.34, "final_3rd_wins": 1.11},
        {"player": "B. Mead", "team": "Man City", "is_diani": False, "goals": 0.18, "big_chances": 0.44, "box_touches": 5.94, "crosses": 0.89, "final_3rd_wins": 1.24},
        {"player": "O. Smith", "team": "Arsenal", "is_diani": False, "goals": 0.38, "big_chances": 0.23, "box_touches": 8.49, "crosses": 0.45, "final_3rd_wins": 0.53},
        {"player": "A. Thompson", "team": "Chelsea", "is_diani": False, "goals": 0.44, "big_chances": 0.44, "box_touches": 6.15, "crosses": 0.70, "final_3rd_wins": 1.20},
        {"player": "A. Russo", "team": "Arsenal", "is_diani": False, "goals": 0.64, "big_chances": 0.34, "box_touches": 7.57, "crosses": 0.25, "final_3rd_wins": 1.03},
        {"player": "K. Shaw", "team": "Man City", "is_diani": False, "goals": 0.97, "big_chances": 0.32, "box_touches": 11.27, "crosses": 0.09, "final_3rd_wins": 1.20},
        {"player": "K. Hanson", "team": "Aston Villa", "is_diani": False, "goals": 0.64, "big_chances": 0.21, "box_touches": 6.26, "crosses": 0.32, "final_3rd_wins": 1.12}
    ]

    df = pd.DataFrame(players_data)

    fig, axs = plt.subplots(2, 2, figsize=(14, 9), facecolor=BG_COLOR)
    fig.suptitle("Kadidiatou Diani vs WSL Attackers & Wingers (Per 90 Metrics)", 
                 fontsize=16, fontweight="bold", color=TEXT_COLOR, y=0.98)

    metrics_config = [
        {"ax": axs[0, 0], "col": "goals", "title": "Goals / 90 (Finishing Threat)", "unit": "Gls/90"},
        {"ax": axs[0, 1], "col": "big_chances", "title": "Big Chances Created / 90 (Playmaking)", "unit": "BCC/90"},
        {"ax": axs[1, 0], "col": "box_touches", "title": "Touches in Opposition Box / 90", "unit": "Touches"},
        {"ax": axs[1, 1], "col": "final_3rd_wins", "title": "Possession Won Final 3rd / 90 (High Press)", "unit": "Wins/90"}
    ]

    for config in metrics_config:
        ax = config["ax"]
        col = config["col"]
        ax.set_facecolor(CARD_BG)
        ax.grid(axis="x", color=GRID_COLOR, linestyle="--", alpha=0.7)
        ax.set_axisbelow(True)

        sorted_df = df.sort_values(by=col, ascending=True).reset_index(drop=True)
        y_pos = np.arange(len(sorted_df))

        colors = [CYAN_ACCENT if is_d else MUTED_SLATE for is_d in sorted_df["is_diani"]]
        
        bars = ax.barh(y_pos, sorted_df[col], color=colors, height=0.6, edgecolor="none", zorder=3)

        # Highlight Diani bar with subtle glow edge
        for idx, is_d in enumerate(sorted_df["is_diani"]):
            if is_d:
                bars[idx].set_edgecolor(GOLD_ACCENT)
                bars[idx].set_linewidth(1.5)

        ax.set_yticks(y_pos)
        yticklabels = [f"{row['player']} ({row['team']})" for _, row in sorted_df.iterrows()]
        ax.set_yticklabels(yticklabels, color=TEXT_COLOR, fontsize=10)

        # Highlight Diani tick label
        for idx, is_d in enumerate(sorted_df["is_diani"]):
            if is_d:
                ax.get_yticklabels()[idx].set_color(GOLD_ACCENT)
                ax.get_yticklabels()[idx].set_fontweight("bold")

        # Value labels at the end of each bar
        for idx, val in enumerate(sorted_df[col]):
            is_d = sorted_df["is_diani"][idx]
            txt_color = GOLD_ACCENT if is_d else TEXT_COLOR
            font_w = "bold" if is_d else "normal"
            ax.text(val + (max(sorted_df[col]) * 0.02), idx, f"{val:.2f}", 
                    va="center", ha="left", color=txt_color, fontsize=9.5, fontweight=font_w)

        ax.set_title(config["title"], color=TEXT_COLOR, fontsize=12, fontweight="bold", pad=10)
        ax.set_xlim(0, max(sorted_df[col]) * 1.18)
        
        # Remove spines
        for spine in ["top", "right", "left", "bottom"]:
            ax.spines[spine].set_visible(False)
        ax.tick_params(colors=SUB_TEXT, labelsize=9)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(out_path, dpi=300, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close()
    print(f"[OK] Generated Diani comparison chart -> {out_path}")


if __name__ == "__main__":
    generate_diani_comparison_chart()
