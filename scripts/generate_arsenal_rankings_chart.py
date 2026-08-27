"""
Generate Arsenal WSL 2024/25 League Rankings Barometer
Visualizes Arsenal's league-leading dominance (#1 in Pressing, Box Touches, Defense, Shots, Passes).
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
fig.patch.set_facecolor('#0B132B')
ax.set_facecolor('#0F172A')

metrics = [
    "Possession Won Final 3rd / 90 (7.9)",
    "Touches in Opposition Box (897)",
    "Shots per 90 (18.23)",
    "Fewest Goals Conceded (14 GA)",
    "Assists (45 Ast)",
    "Accurate Passes / 90 (452.1)",
    "Shots on Target % (38.4%)",
    "Expected Goals (48.4 xG)",
    "Possession % (59.0%)",
    "Total Goals Scored (53 GF)",
    "Actual Points vs xPTS (51 vs 53.0)"
]

ranks = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
rank_labels = ["Rank #1", "Rank #1", "Rank #1", "Rank #1", "Rank #1", "Rank #1", "Rank #2", "Rank #2", "Rank #2", "Rank #2", "Rank #2 (Underperf)"]

y_pos = np.arange(len(metrics))
# Invert rank for visual bar length: Rank 1 gets longest bar (12), Rank 2 gets (11)
bar_lengths = [13 - r for r in ranks]

colors = []
for r in ranks[:6]:
    colors.append('#10B981') # Emerald for #1
colors.extend(['#38BDF8', '#38BDF8', '#38BDF8', '#38BDF8']) # Cyan for #2
colors.append('#F43F5E') # Rose red for points underperformance

bars = ax.barh(y_pos, bar_lengths, color=colors, height=0.62, edgecolor='none', zorder=3)

# Add rank badges on bars
for i, (bar, label, length) in enumerate(zip(bars, rank_labels, bar_lengths)):
    if i == len(bars) - 1:
        ax.text(length - 0.4, bar.get_y() + bar.get_height()/2, label,
                va='center', ha='right', color='#FFFFFF', fontweight='bold', fontsize=9)
    else:
        ax.text(length - 0.4, bar.get_y() + bar.get_height()/2, label,
                va='center', ha='right', color='#0B132B', fontweight='bold', fontsize=9)

ax.set_yticks(y_pos)
ax.set_yticklabels(metrics, fontsize=9.5, color='#F1F5F9', fontweight='medium')
ax.invert_yaxis()  # Top metric at top

ax.set_xlim(0, 13)
ax.set_xticks([1, 6, 11, 12])
ax.set_xticklabels(['Bottom (12)', 'Mid-table (6)', 'Rank #2', 'Rank #1'], fontsize=8.5, color='#94A3B8')

ax.grid(axis='x', linestyle=':', alpha=0.2, color='#475569', zorder=1)
ax.tick_params(colors='#94A3B8', length=0)

ax.set_title("Arsenal Women · WSL 2024/25 League Dominance Profile", fontsize=13, fontweight='bold', color='#F8FAFC', pad=14, loc='left')
fig.text(0.125, 0.91, "Rankings across 12 WSL clubs: League-leading in pressing, territorial dominance and defensive suppression", fontsize=8.5, color='#94A3B8', fontstyle='italic')

plt.tight_layout()

out_dir = Path('assets/images/evaluations')
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / 'arsenal_rankings_barometer.png'
plt.savefig(out_file, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print(f"Generated: {out_file}")
