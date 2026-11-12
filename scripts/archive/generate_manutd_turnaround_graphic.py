#!/usr/bin/env python3
"""
Generate Visual Infographic: Manchester United Defensive Turnaround & Maya Le Tissier Effect
=============================================================================================
Compares the pre-meeting collapse (MW2 vs Chelsea 0-5) against the post-meeting resurgence
(MW3 at Arsenal 1-1, MW4 vs West Ham 2-1, MW5 vs Liverpool 1-0).
Saves to assets/images/manutd_defensive_turnaround.png.
"""

import sys
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Fix Windows console UTF-8 output
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_IMG = PROJECT_ROOT / "assets" / "images" / "manutd_defensive_turnaround.png"
OUTPUT_IMG.parent.mkdir(parents=True, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['text.color'] = '#EDEDED'

def create_graphic():
    fig = plt.figure(figsize=(15, 8.5), facecolor='#080B10')
    ax = fig.add_subplot(111)
    ax.set_facecolor('#080B10')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Header
    ax.text(50, 95, "GLORY GLORY LE TISSIER · THE DEFENSIVE RESURGENCE", 
            fontsize=18, fontweight='bold', ha='center', va='center', color='#FFFFFF')
    ax.text(50, 90.5, "Manchester United Women 2026/27: The Turning Point from Chelsea (0-5) to Arsenal & Liverpool", 
            fontsize=10.5, ha='center', va='center', color='#9CA3AF')

    # Divider Line
    ax.plot([5, 95], [87, 87], color='#1F2937', lw=1.2)

    # -------------------------------------------------------------
    # LEFT PANEL: THE COLLAPSE (MW1-2 / Chelsea Horror Show)
    # -------------------------------------------------------------
    rect_left = patches.FancyBboxPatch((5, 12), 42, 72, boxstyle="round,pad=1.2,rounding_size=2",
                                       linewidth=1.2, edgecolor='#EF4444', facecolor='#110E14')
    ax.add_patch(rect_left)

    # Left Badge
    ax.text(26, 80, "PHASE 1: THE COLLAPSE", fontsize=11, fontweight='bold', color='#EF4444', ha='center')
    ax.text(26, 76.5, "MW2 vs Chelsea (0-5) · Before the Captain's Meeting", fontsize=8.5, color='#9CA3AF', ha='center')

    # Left Key Metrics
    left_metrics = [
        ("GOALS CONCEDED", "5", "In 90 minutes (2.94 xGA)", "#EF4444"),
        ("SHOTS CONCEDED", "25", "17 from inside the penalty box", "#F87171"),
        ("TACKLES WON", "11", "Severe midfield disconnect", "#9CA3AF"),
        ("LE TISSIER RATING", "4.63", "Career-low FotMob rating", "#EF4444"),
        ("POINTS EARNED", "0 / 6", "Back-to-back losses (MW1-2)", "#EF4444")
    ]

    y_pos = 69
    for title, val, sub, color in left_metrics:
        # Box inside left
        sub_box = patches.FancyBboxPatch((7, y_pos - 7.5), 38, 9, boxstyle="round,pad=0.5,rounding_size=1",
                                         facecolor='#18131E', edgecolor='#2D1B22', lw=0.8)
        ax.add_patch(sub_box)
        ax.text(9, y_pos - 1.5, title, fontsize=8, fontweight='bold', color='#9CA3AF', va='center')
        ax.text(42, y_pos - 3, val, fontsize=16, fontweight='bold', color=color, ha='right', va='center')
        ax.text(9, y_pos - 5.5, sub, fontsize=7.5, color='#6B7280', va='center')
        y_pos -= 11.5

    # -------------------------------------------------------------
    # RIGHT PANEL: THE RESURGENCE (MW3-5 / Leadership & Wall)
    # -------------------------------------------------------------
    rect_right = patches.FancyBboxPatch((53, 12), 42, 72, boxstyle="round,pad=1.2,rounding_size=2",
                                        linewidth=1.4, edgecolor='#10B981', facecolor='#0D1617')
    ax.add_patch(rect_right)

    # Right Badge
    ax.text(74, 80, "PHASE 2: THE IDENTITY BORN", fontsize=11, fontweight='bold', color='#10B981', ha='center')
    ax.text(74, 76.5, "MW3 at Emirates (1-1) & MW5 vs Liverpool (1-0)", fontsize=8.5, color='#9CA3AF', ha='center')

    # Right Key Metrics
    right_metrics = [
        ("GOALS CONCEDED", "2", "In 3 matches (0.67 / game)", "#10B981"),
        ("CLEARANCES (MW3)", "54", "15 by Maya Le Tissier alone!", "#38BDF8"),
        ("TACKLES (MW3)", "25", "2.3x increase vs Chelsea game", "#10B981"),
        ("LE TISSIER VS LIV", "8.21", "13/15 duels won (86.7%) & Clean Sheet", "#F59E0B"),
        ("POINTS EARNED", "7 / 9", "Unbeaten: Draw at Arsenal, Wins vs WHU & LIV", "#10B981")
    ]

    y_pos = 69
    for title, val, sub, color in right_metrics:
        # Box inside right
        sub_box = patches.FancyBboxPatch((55, y_pos - 7.5), 38, 9, boxstyle="round,pad=0.5,rounding_size=1",
                                         facecolor='#111F1D', edgecolor='#13352C', lw=0.8)
        ax.add_patch(sub_box)
        ax.text(57, y_pos - 1.5, title, fontsize=8, fontweight='bold', color='#9CA3AF', va='center')
        ax.text(90, y_pos - 3, val, fontsize=16, fontweight='bold', color=color, ha='right', va='center')
        ax.text(57, y_pos - 5.5, sub, fontsize=7.5, color='#6B7280', va='center')
        y_pos -= 11.5

    # Center Quote Bubble / Catalyst
    ax.annotate('', xy=(53, 50), xytext=(47, 50),
                arrowprops=dict(arrowstyle="->", color="#F59E0B", lw=2.5))
    ax.text(50, 54, "THE CAPTAIN'S\nCONVERSATION", fontsize=7.5, fontweight='bold', 
            ha='center', va='center', color='#F59E0B')

    # Bottom Maya Le Tissier Summary Strip
    strip_box = patches.FancyBboxPatch((5, 3), 90, 7.5, boxstyle="round,pad=0.8,rounding_size=1.5",
                                      facecolor='#0F172A', edgecolor='#334155', lw=1.0)
    ax.add_patch(strip_box)
    ax.text(7, 6.7, "MAYA LE TISSIER (CAPTAIN, 22) · SEASON TOTALS:", fontsize=8.5, fontweight='bold', color='#38BDF8')
    ax.text(7, 4.3, "450 Minutes (100%) · 37 Clearances (7.4/match) · 23 Recoveries · 73.5% Duels Won · Rating: 4.63 → 7.75 → 7.50 → 8.21", 
            fontsize=8, color='#CBD5E1')

    plt.tight_layout()
    plt.savefig(OUTPUT_IMG, dpi=200, facecolor='#080B10')
    plt.close()
    print(f"[OK] Saved graphic to {OUTPUT_IMG}")

if __name__ == "__main__":
    create_graphic()
