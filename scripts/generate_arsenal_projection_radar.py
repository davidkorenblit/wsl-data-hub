import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT_PATH = Path("assets/images/evaluations/arsenal_projection_radar.png")
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

# Theme Tokens (WSL Data Hub Dark Theme)
BG_COLOR = "#0b1329"
CARD_BG = "#131f3d"
TEXT_COLOR = "#f8fafc"
SUB_TEXT = "#94a3b8"
GRID_COLOR = "#334155"
PROJECTED_COLOR = "#38bdf8"  # Sky Blue / Cyan
BASELINE_COLOR = "#f59e0b"   # Amber Gold
CHAMPION_COLOR = "#10b981"   # Emerald Green

# 6 Pillars for Title Projection (0-100 Percentile Scale)
categories = [
    "Points Per Match\n(PPM Ceiling)",
    "Goal Difference\nPer 90 (+GD)",
    "Goal Prevention\n(Low GA /90)",
    "Opposition Box\nDominance",
    "Final 3rd Pressing\n& Recoveries",
    "Squad Modularity\n& Bench Depth"
]
N = len(categories)

# Scaled values (0-100 index)
baseline_2025_26 = [82, 85, 92, 88, 90, 72]      # 2025/26 Baseline (51 pts, 14 GA, 53 GF)
projected_2026_27 = [96, 95, 97, 98, 98, 96]     # 2026/27 Projection (66.5 pts, 68 GF, 14.5 GA)

# Close polygon
base_plot = baseline_2025_26 + [baseline_2025_26[0]]
proj_plot = projected_2026_27 + [projected_2026_27[0]]

angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += [angles[0]]

fig, ax = plt.subplots(figsize=(8.5, 8.5), subplot_kw=dict(polar=True), facecolor=BG_COLOR)
ax.set_facecolor(CARD_BG)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Axis labels
plt.xticks(angles[:-1], categories, color=TEXT_COLOR, size=11, fontweight="bold")

# Y-ticks
ax.set_rlabel_position(0)
plt.yticks([40, 60, 80, 100], ["40", "60", "80", "100"], color=SUB_TEXT, size=9)
plt.ylim(0, 105)
ax.grid(color=GRID_COLOR, linestyle="--", linewidth=0.8, alpha=0.7)

# Plot Baseline
ax.plot(angles, base_plot, linewidth=2.2, linestyle='--', color=BASELINE_COLOR, label="Arsenal 2025/26 Baseline (51 Pts · 2nd)")
ax.fill(angles, base_plot, color=BASELINE_COLOR, alpha=0.15)

# Plot Projected
ax.plot(angles, proj_plot, linewidth=2.8, linestyle='solid', color=PROJECTED_COLOR, label="Arsenal 2026/27 Projection (66.5 Pts · Title Ceiling)")
ax.fill(angles, proj_plot, color=PROJECTED_COLOR, alpha=0.28)

# Title
plt.title("ARSENAL 2026/27 · TITLE RADAR PROJECTION", size=15, color="#FFFFFF", fontweight="bold", y=1.09)
fig.text(0.5, 0.94, "Baseline 2025/26 vs 2026/27 Projected Title Radar", color=SUB_TEXT, size=10, ha="center")

# Legend
leg = plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.06), ncol=1, facecolor="#0f172a", edgecolor="#334155", fontsize=10)
for t in leg.get_texts():
    t.set_color("#f8fafc")

plt.tight_layout()
plt.savefig(OUT_PATH, dpi=300, facecolor=fig.get_facecolor(), bbox_inches="tight")
plt.close()

print(f"Generated radar chart: {OUT_PATH}")
