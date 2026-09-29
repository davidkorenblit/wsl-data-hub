"""
WSL Data Hub - Clean Minimalist LinkedIn Stat Card Generator
============================================================
Creates a high-contrast, uncluttered 1200x675 KPI image optimized for LinkedIn:
- 3 Large, beautiful metric pillars (xG, Goals Scored, Big Chances Missed)
- Clean dark background, ample padding
- Sleek footer with defensive variance & Nnadozie stat
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path

# Paths
OUTPUT_DIR = Path("assets/images/evaluations")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_PATH = OUTPUT_DIR / "brighton_stat_card_linkedin.png"

# Color Palette
BG_COLOR = "#070b14"
CARD_BG = "#0f172a"
BORDER_COLOR = "#1e293b"
CYAN = "#00d2eb"
GOLD = "#f59e0b"
ROSE = "#f43f5e"
TEXT_WHITE = "#f8fafc"
TEXT_MUTED = "#94a3b8"
TEXT_SUB = "#64748b"

def generate_stat_card():
    # 16:9 Aspect Ratio optimized for LinkedIn Feed (12 x 6.75 inches @ 150 DPI = 1800 x 1012 px)
    fig, ax = plt.subplots(figsize=(12, 6.75), facecolor=BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Top Tag
    ax.text(50, 91, "WSL 2026/27  ·  ROUNDS 1–4", ha="center", va="center",
            fontsize=11, fontfamily="sans-serif", fontweight="bold", color=CYAN)

    # Main Title
    ax.text(50, 83, "BRIGHTON & HOVE ALBION", ha="center", va="center",
            fontsize=26, fontfamily="sans-serif", fontweight="heavy", color=TEXT_WHITE)

    # Subtitle
    ax.text(50, 76.5, "The Double-Variance Anomaly", ha="center", va="center",
            fontsize=13, fontfamily="sans-serif", color=TEXT_MUTED, style="italic")

    # 3 Large Metric Cards
    cards_data = [
        {
            "x": 6, "w": 26.6,
            "num": "8.33", "color": CYAN,
            "label": "Expected Goals (xG)",
            "badge": "RANK #3 IN WSL",
            "badge_bg": "#083344", "badge_color": CYAN
        },
        {
            "x": 36.6, "w": 26.6,
            "num": "3", "color": GOLD,
            "label": "Actual Goals Scored",
            "badge": "-5.33 DEFICIT",
            "badge_bg": "#451a03", "badge_color": GOLD
        },
        {
            "x": 67.3, "w": 26.6,
            "num": "10", "color": ROSE,
            "label": "Big Chances Missed",
            "badge": "12 CREATED TOTAL",
            "badge_bg": "#4c0519", "badge_color": ROSE
        }
    ]

    for c in cards_data:
        # Card Background
        rect = patches.FancyBboxPatch(
            (c["x"], 24), c["w"], 46,
            boxstyle="round,pad=1.2,rounding_size=2.5",
            facecolor=CARD_BG, edgecolor=BORDER_COLOR, linewidth=1.5
        )
        ax.add_patch(rect)

        # Huge Number
        cx = c["x"] + c["w"] / 2
        ax.text(cx, 55, c["num"], ha="center", va="center",
                fontsize=52, fontfamily="sans-serif", fontweight="heavy", color=c["color"])

        # Metric Label
        ax.text(cx, 41, c["label"], ha="center", va="center",
                fontsize=11.5, fontfamily="sans-serif", fontweight="bold", color=TEXT_WHITE)

        # Context Badge
        ax.text(cx, 31.5, f"  {c['badge']}  ", ha="center", va="center",
                fontsize=9, fontfamily="sans-serif", fontweight="bold", color=c["badge_color"],
                bbox=dict(boxstyle="round,pad=0.45", facecolor=c["badge_bg"], edgecolor=c["badge_color"], lw=1))

    # Bottom Footer Strip
    footer_rect = patches.FancyBboxPatch(
        (6, 7), 88, 12,
        boxstyle="round,pad=0.8,rounding_size=2.0",
        facecolor="#0b1120", edgecolor="#1e293b", linewidth=1.0
    )
    ax.add_patch(footer_rect)

    # Footer Text Left (Defensive Slump)
    ax.text(9, 13, "DEFENSIVE VARIANCE: ", ha="left", va="center",
            fontsize=9.5, fontfamily="sans-serif", fontweight="bold", color=ROSE)
    ax.text(29, 13, "6 Conceded from 3.96 xGA  ·  Nnadozie 60.0% Save Rate", ha="left", va="center",
            fontsize=9.5, fontfamily="sans-serif", color=TEXT_MUTED)

    # Footer Text Right (Brand)
    ax.text(91, 13, "WSL DATA HUB", ha="right", va="center",
            fontsize=9.5, fontfamily="sans-serif", fontweight="heavy", color=TEXT_SUB)

    # Save cleanly
    plt.savefig(OUT_PATH, dpi=160, bbox_inches="tight", facecolor=BG_COLOR, edgecolor="none")
    plt.close()
    print(f"[OK] Stat card saved successfully at: {OUT_PATH}")

if __name__ == "__main__":
    generate_stat_card()
