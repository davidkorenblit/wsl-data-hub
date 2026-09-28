"""
WSL Data Hub - Brighton Finishing Crisis & Underperformance Chart Generator
============================================================================
Visualizes Brighton Women's unprecedented finishing anomaly in the first 4 rounds of WSL 2026/27:
- Match-by-match xG vs Goals Scored
- Big chances missed per round
- Total xG (8.33) vs Actual Goals (3) - Deficit of -5.33
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from paths import ASSETS_IMAGES_DIR, ensure_all_directories

# Aesthetic Design Tokens
BG_COLOR = "#0b1329"
CARD_BG = "#131f3d"
TEXT_COLOR = "#f8fafc"
SUB_TEXT = "#94a3b8"
GRID_COLOR = "#1e293b"
CYAN_ACCENT = "#00B0C7"
ROSE_ACCENT = "#f43f5e"
GOLD_ACCENT = "#fbbf24"
EMERALD_ACCENT = "#10b981"
MUTED_SLATE = "#475569"

def generate_brighton_chart():
    ensure_all_directories()
    out_dir = ASSETS_IMAGES_DIR / "evaluations"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "brighton_finishing_anomaly_mw4.png"

    # Match data
    rounds = ["MW1 vs Arsenal", "MW2 vs Birmingham", "MW3 vs Aston Villa", "MW4 vs LCL"]
    xg = [0.70, 2.69, 3.17, 1.77]
    goals = [0, 2, 1, 0]
    big_chances_missed = [1, 3, 2, 4]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6.5), facecolor=BG_COLOR)
    fig.suptitle("Brighton Women · 2026/27 Finishing Anomaly Analysis (Rounds 1–4)",
                 fontsize=17, fontweight="bold", color=TEXT_COLOR, y=0.98)

    # Subplot 1: Match-by-Match xG vs Goals
    ax1.set_facecolor(CARD_BG)
    x = np.arange(len(rounds))
    width = 0.35

    rects1 = ax1.bar(x - width/2, xg, width, label="Expected Goals (xG)", color=CYAN_ACCENT, edgecolor="none", zorder=3)
    rects2 = ax1.bar(x + width/2, goals, width, label="Actual Goals Scored", color=GOLD_ACCENT, edgecolor="none", zorder=3)

    # Annotate Big Chances Missed as badges
    for i, bcm in enumerate(big_chances_missed):
        max_h = max(xg[i], goals[i])
        ax1.text(i, max_h + 0.15, f"{bcm} Big Chances\nMissed", ha="center", va="bottom",
                 fontsize=9, color=ROSE_ACCENT, fontweight="bold",
                 bbox=dict(boxstyle="round,pad=0.3", facecolor=BG_COLOR, edgecolor=ROSE_ACCENT, alpha=0.9, lw=1))

    # Bar values
    for r in rects1:
        h = r.get_height()
        ax1.text(r.get_x() + r.get_width()/2., h/2, f"{h:.2f}", ha='center', va='center', color=BG_COLOR, fontweight='bold', fontsize=10)
    for r in rects2:
        h = r.get_height()
        if h > 0:
            ax1.text(r.get_x() + r.get_width()/2., h/2, f"{int(h)}", ha='center', va='center', color=BG_COLOR, fontweight='bold', fontsize=10)

    ax1.set_title("Match-by-Match: Creation vs Reality", fontsize=13, fontweight="bold", color=TEXT_COLOR, pad=12)
    ax1.set_xticks(x)
    ax1.set_xticklabels(rounds, color=TEXT_COLOR, fontsize=10, fontweight="bold")
    ax1.tick_params(colors=SUB_TEXT)
    ax1.set_ylabel("Goals / xG", color=SUB_TEXT, fontsize=11)
    ax1.set_ylim(0, 4.3)
    ax1.grid(True, linestyle="--", alpha=0.4, color=GRID_COLOR, zorder=0)
    ax1.legend(loc="upper left", framealpha=0.3, facecolor=BG_COLOR, edgecolor=GRID_COLOR, labelcolor=TEXT_COLOR)

    for spine in ax1.spines.values():
        spine.set_color(GRID_COLOR)

    # Subplot 2: Cumulative Totals & Finishing Delta
    ax2.set_facecolor(CARD_BG)
    categories = ["Total xG Created", "Actual Goals Scored", "xG Allowed (xGA)", "Actual Goals Conceded"]
    values = [8.33, 3.0, 3.96, 6.0]
    colors = [CYAN_ACCENT, GOLD_ACCENT, EMERALD_ACCENT, ROSE_ACCENT]

    bars = ax2.bar(categories, values, color=colors, width=0.55, zorder=3)

    for bar, val in zip(bars, values):
        h = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., h + 0.2, f"{val:.2f}" if isinstance(val, float) else f"{val}",
                 ha='center', va='bottom', color=TEXT_COLOR, fontweight='bold', fontsize=12)

    # Annotation Box
    text_box = (
        "Key Tactical Takeaways:\n"
        "• Underperformance: -5.33 Goals below xG\n"
        "• Total 10 Big Chances Missed in 4 matches\n"
        "• Opponents scored 6 goals from just 3.96 xGA\n"
        "• Conclusion: Tactical creation is elite, regression to mean is imminent."
    )
    ax2.text(0.05, 0.92, text_box, transform=ax2.transAxes,
             fontsize=10, color=TEXT_COLOR, va="top",
             bbox=dict(boxstyle="round,pad=0.6", facecolor=BG_COLOR, edgecolor=CYAN_ACCENT, alpha=0.95, lw=1.2))

    ax2.set_title("Cumulative Balance: 4-Match Aggregates", fontsize=13, fontweight="bold", color=TEXT_COLOR, pad=12)
    ax2.set_xticks(range(len(categories)))
    ax2.set_xticklabels(["Total xG\n(8.33)", "Goals Scored\n(3)", "Total xGA\n(3.96)", "Goals Conceded\n(6)"],
                        color=TEXT_COLOR, fontsize=10, fontweight="bold")
    ax2.tick_params(colors=SUB_TEXT)
    ax2.set_ylabel("Total Metric Sum", color=SUB_TEXT, fontsize=11)
    ax2.set_ylim(0, 10.5)
    ax2.grid(True, linestyle="--", alpha=0.4, color=GRID_COLOR, zorder=0)

    for spine in ax2.spines.values():
        spine.set_color(GRID_COLOR)

    plt.tight_layout()
    plt.subplots_adjust(top=0.88)
    plt.savefig(out_path, dpi=200, facecolor=BG_COLOR, edgecolor="none")
    plt.close()
    print(f"[OK] Brighton chart saved successfully at: {out_path}")

if __name__ == "__main__":
    generate_brighton_chart()
