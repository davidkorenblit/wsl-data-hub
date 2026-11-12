"""
WSL Data Hub - Intuitive LCL Before vs After Comparison Chart
============================================================
Generates an ultra-intuitive, clean Paired Bar Chart comparing
2024/25 Baseline (Gray/Navy) vs 2025/26 Projected with Transfers (Emerald/Gold).
Zero mental load — immediately understood in 1 second.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from paths import ASSETS_IMAGES_DIR, ensure_all_directories

# Aesthetic Theme Tokens
BG_COLOR = "#0b1329"
CARD_BG = "#131f3d"
TEXT_COLOR = "#f8fafc"
SUB_TEXT = "#94a3b8"
GRID_COLOR = "#1e293b"
BASE_COLOR = "#475569"     # Muted Slate for Baseline (Past)
PROJ_COLOR = "#10b981"     # Emerald Green for Improvement (Future)
GOLD_COLOR = "#fbbf24"     # Gold for Points


def generate_intuitive_improvement_chart():
    ensure_all_directories()
    out_dir = ASSETS_IMAGES_DIR / "evaluations"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "lcl_improvement_forecast.png"

    categories = [
        "Expected Points\n(xPTS)",
        "Goals Scored\n(GF)",
        "Goals Conceded\n(GA - Lower is better)",
        "Goal Difference\n(GD)"
    ]
    
    baseline_vals = [31.9, 30.7, 39.0, -8.3]
    projected_vals = [49.4, 49.2, 27.0, 22.2]
    deltas = ["+17.5 Pts", "+18.5 Goals", "-12.0 Saved", "+30.5 Delta"]

    fig, ax = plt.subplots(figsize=(12, 6.2), facecolor=BG_COLOR)
    ax.set_facecolor(CARD_BG)
    ax.grid(axis="y", color=GRID_COLOR, linestyle="--", alpha=0.7)
    ax.set_axisbelow(True)

    x = np.arange(len(categories))
    width = 0.32

    # Baseline Bars
    bars1 = ax.bar(x - width/2, baseline_vals, width, label="Baseline (2024/25 Scaled)", 
                   color=BASE_COLOR, edgecolor="#334155", linewidth=1.2, zorder=3)

    # Projected Bars (Gold for Points, Emerald for others)
    colors_proj = [GOLD_COLOR, PROJ_COLOR, "#38bdf8", PROJ_COLOR]
    bars2 = ax.bar(x + width/2, projected_vals, width, label="Projected (2025/26 with Transfers)", 
                   color=colors_proj, edgecolor="#ffffff", linewidth=1.5, zorder=3)

    # Add Zero Line
    ax.axhline(0, color="#64748b", linewidth=1.2, linestyle="-", alpha=0.8, zorder=2)

    # Annotate Values on Baseline Bars
    for bar in bars1:
        h = bar.get_height()
        va = "bottom" if h >= 0 else "top"
        offset = 1.2 if h >= 0 else -2.5
        ax.text(bar.get_x() + bar.get_width()/2, h + offset, f"{h:.1f}", 
                ha="center", va=va, color=SUB_TEXT, fontsize=11, fontweight="bold", fontfamily="monospace")

    # Annotate Values and Delta Badges on Projected Bars
    for idx, bar in enumerate(bars2):
        h = bar.get_height()
        va = "bottom" if h >= 0 else "top"
        offset = 1.2 if h >= 0 else -2.5
        txt_color = GOLD_COLOR if idx == 0 else ("#38bdf8" if idx == 2 else PROJ_COLOR)
        
        # Projected Value
        ax.text(bar.get_x() + bar.get_width()/2, h + offset, f"{h:.1f}", 
                ha="center", va=va, color=txt_color, fontsize=12, fontweight="bold", fontfamily="monospace")

        # Delta Badge floating above the pair
        badge_y = max(baseline_vals[idx], projected_vals[idx]) + 5.5
        ax.text(x[idx], badge_y, deltas[idx], ha="center", va="center", 
                color="#ffffff", fontsize=10.5, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", facecolor=CARD_BG, edgecolor=PROJ_COLOR, linewidth=1.5, alpha=0.95))

    ax.set_xticks(x)
    ax.set_xticklabels(categories, color=TEXT_COLOR, fontsize=11, fontweight="bold")
    ax.set_title("London City Lionesses: 2024/25 Baseline vs 2025/26 Season Projection", 
                 color=TEXT_COLOR, fontsize=14, fontweight="bold", pad=20)
    ax.set_ylim(-16, 72)

    # Clean Legend in upper right
    legend = ax.legend(frameon=True, facecolor=CARD_BG, edgecolor=GRID_COLOR, fontsize=10.5, loc="upper right")
    for text in legend.get_texts():
        text.set_color(TEXT_COLOR)

    for spine in ["top", "right", "left", "bottom"]:
        ax.spines[spine].set_visible(False)
    ax.tick_params(colors=SUB_TEXT, labelsize=9)

    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close()
    print(f"[OK] Generated intuitive paired-bar improvement chart -> {out_path}")


if __name__ == "__main__":
    generate_intuitive_improvement_chart()
