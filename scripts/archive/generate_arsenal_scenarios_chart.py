import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Paths
OUT_DIR = Path("assets/images/evaluations")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_PATH = OUT_DIR / "arsenal_scenarios_matrix.png"

# Setup Figure (Dark Theme matching WSL Data Hub)
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
fig.patch.set_facecolor('#0B1329')
ax.set_facecolor('#0B1329')

# Data
scenarios = [
    "1. תרחיש שמרני\n(עומס צ'מפיונס ופציעות)",
    "2. תרחיש בסיס (Expected)\n(חיבור מודולרי ותיקון פתיחה)",
    "3. תרחיש עליון (Ceiling)\n(התפוצצות של אג'ימאן ו-G)"
]
pts = [62.0, 66.5, 70.0]
gd = ["+46 GD", "+53.6 GD", "+60.0 GD"]
colors = ['#F59E0B', '#10B981', '#38BDF8']

# Horizontal Bars
y_pos = np.arange(len(scenarios))
bars = ax.barh(y_pos, pts, height=0.52, color=colors, edgecolor='none', zorder=3)

# Threshold Reference Lines
ax.axvline(x=63, color='#EF4444', linestyle='--', linewidth=1.5, alpha=0.85, zorder=2, label="סף אליפות היסטורי ב-26 מש' (63 נק')")
ax.axvline(x=52, color='#64748B', linestyle=':', linewidth=1.2, alpha=0.75, zorder=2, label="סף ליגת האלופות (52 נק')")

# Bar Annotations
for i, bar in enumerate(bars):
    w = bar.get_width()
    ax.text(w + 0.8, bar.get_y() + bar.get_height()/2, f"{pts[i]:.1f} נק'  ({gd[i]})",
            va='center', ha='left', color='#F8FAFC', fontweight='bold', fontsize=12, family='sans-serif')

# Labels & Ticks
ax.set_yticks(y_pos)
ax.set_yticklabels(scenarios, fontsize=11, color='#E2E8F0', fontweight='semibold')
ax.set_xlim(40, 78)
ax.set_xlabel("סך נקודות חזוי (xPTS) בעונה של 26 מחזורים", fontsize=11, color='#94A3B8', labelpad=10, fontweight='bold')

# Grid & Spines
ax.grid(axis='x', color='#1E293B', linestyle='-', linewidth=0.8, zorder=1)
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis='x', colors='#94A3B8', labelsize=10)
ax.tick_params(axis='y', length=0)

# Title & Subtitle
plt.title("Arsenal 2026/27 · מודל 3 התרחישים והתקרה לאליפות", fontsize=15, color='#FFFFFF', fontweight='bold', pad=22, loc='right')
fig.text(0.90, 0.905, "שקלול דלתות העברות, עומק הסגל ומניעת איבודי נקודות בפתיחת העונה", fontsize=10, color='#94A3B8', ha='right')

# Legend
leg = ax.legend(loc='lower right', facecolor='#0F172A', edgecolor='#334155', fontsize=9.5)
for text in leg.get_texts():
    text.set_color('#CBD5E1')

plt.tight_layout()
plt.savefig(OUT_PATH, bbox_inches='tight', facecolor=fig.get_facecolor(), dpi=300)
plt.close()

print(f"Generated chart: {OUT_PATH}")
