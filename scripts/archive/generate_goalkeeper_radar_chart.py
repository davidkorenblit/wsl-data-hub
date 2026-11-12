"""
WSL Data Hub - Goalkeeper Radar Chart Generator
===============================================
Generates an aesthetic Radar / Spider chart comparing:
Mary Earps (Paris S-G / ENG) vs Elene Lete (Lionesses / ESP)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

from paths import EVALUATIONS_CHARTS_DIR

EVALUATIONS_CHARTS_DIR.mkdir(parents=True, exist_ok=True)

# Theme Tokens
BG_COLOR = "#0b1329"
CARD_BG = "#131f3d"
TEXT_COLOR = "#f8fafc"
SUB_TEXT = "#94a3b8"
GRID_COLOR = "#334155"
EARPS_COLOR = "#10b981"  # Emerald Green
LETE_COLOR = "#f43f5e"   # Coral Rose


def generate_radar_chart():
    # 5 Key Metrics for Goalkeepers (Normalized 0 to 100 Scale for visual clarity)
    categories = [
        "Save %\n(Shot Stopping)",
        "Goals Against /90\n(Prevention - Inverted)",
        "Clean Sheet %\n(Shutout Rate)",
        "Win Rate %\n(Team Security)",
        "Points Per Match\n(PPM Index)"
    ]
    N = len(categories)

    # Lete metrics (2025/26 WSL): Save 57.3%, GA90 1.59 (Low score in prevention), CS% 13.6%, Win% 36.4%, PPM 1.23
    # Scaled to 0-100 benchmark (Min-Max league reference)
    # Lete values scaled:
    lete_values = [57.3, 40.0, 13.6, 36.4, 41.0]

    # Earps metrics (2025/26 PSG): Save 68.5%, GA90 0.81 (High score in prevention), CS% 42.9%, Win% 66.7%, PPM 2.10
    earps_values = [68.5, 82.0, 42.9, 66.7, 70.0]

    # Repeat first value to close polygon
    lete_plot = lete_values + [lete_values[0]]
    earps_plot = earps_values + [earps_values[0]]

    # Compute angle of each axis
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += [angles[0]]

    fig, ax = plt.subplots(figsize=(8.5, 8.5), subplot_kw=dict(polar=True), facecolor=BG_COLOR)
    ax.set_facecolor(CARD_BG)

    # Set angles and clockwise direction
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Draw axis lines and labels
    plt.xticks(angles[:-1], categories, color=TEXT_COLOR, size=11, fontweight="bold")

    # Y-ticks (Grid rings)
    ax.set_rlabel_position(0)
    plt.yticks([25, 50, 75], ["25", "50", "75"], color=SUB_TEXT, size=9)
    plt.ylim(0, 95)
    ax.grid(color=GRID_COLOR, linestyle="--", linewidth=0.8, alpha=0.7)

    # Plot Earps
    ax.plot(angles, earps_plot, linewidth=2.5, linestyle='solid', color=EARPS_COLOR, label="Mary Earps (Paris S-G · 2025/26)")
    ax.fill(angles, earps_plot, color=EARPS_COLOR, alpha=0.3)

    # Plot Lete
    ax.plot(angles, lete_plot, linewidth=2.5, linestyle='solid', color=LETE_COLOR, label="Elene Lete (Lionesses · 2025/26)")
    ax.fill(angles, lete_plot, color=LETE_COLOR, alpha=0.3)

    # Title & Legend
    plt.title("Goalkeeper Profile Comparison · Mary Earps vs Elene Lete", color=TEXT_COLOR, size=14, fontweight="bold", pad=28)
    plt.legend(loc="upper right", bbox_to_anchor=(1.15, 0.05), facecolor=CARD_BG, edgecolor=GRID_COLOR, labelcolor=TEXT_COLOR, fontsize=10)

    out_path = EVALUATIONS_CHARTS_DIR / "earps_vs_lete_radar.png"
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, facecolor=BG_COLOR, bbox_inches="tight")
    plt.close()
    print(f"[OK] Generated Radar Chart: {out_path}")


if __name__ == "__main__":
    generate_radar_chart()
