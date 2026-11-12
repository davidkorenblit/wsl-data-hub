"""
Generate WSL 2024/25 Scatter Plot: Possession % vs Touches in Opposition Box
Highlights London City Lionesses' midfield control vs box penetration bottleneck.
"""

import json
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

# Set dark aesthetic style
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
fig.patch.set_facecolor('#0B132B')
ax.set_facecolor('#0F172A')

# Load data
data_path = Path('_data/baseline_q1_summary.json')
with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

teams = data['all_teams']

# Extract metrics
names = []
poss = []
touches = []
gfs = []

for t in teams:
    squad_name = t['squad']
    if squad_name == 'Lionesses':
        squad_name = 'London City'
    names.append(squad_name)
    poss.append(t['poss_pct'])
    touches.append(t['touches_opp_box'])
    gfs.append(t['gf'])

poss = np.array(poss)
touches = np.array(touches)
gfs = np.array(gfs)

# Colors
colors = []
edgecolors = []
sizes = []
for name in names:
    if name == 'London City':
        colors.append('#38BDF8')       # Bright Cyan
        edgecolors.append('#FFFFFF')
        sizes.append(260)
    elif name in ['Arsenal', 'Chelsea', 'Manchester City']:
        colors.append('#F59E0B')       # Amber Gold
        edgecolors.append('#FCD34D')
        sizes.append(180)
    else:
        colors.append('#64748B')       # Slate Gray
        edgecolors.append('#94A3B8')
        sizes.append(130)

# Plot scatter
scatter = ax.scatter(
    poss, touches, 
    s=sizes, 
    c=colors, 
    edgecolors=edgecolors, 
    linewidth=2, 
    alpha=0.9, 
    zorder=4
)

# Reference lines (League Averages)
avg_poss = np.mean(poss)
avg_touches = np.mean(touches)

ax.axvline(avg_poss, color='#334155', linestyle='--', linewidth=1.2, zorder=2)
ax.axhline(avg_touches, color='#334155', linestyle='--', linewidth=1.2, zorder=2)

ax.text(avg_poss + 0.3, 310, f'Avg Poss: {avg_poss:.1f}%', color='#64748B', fontsize=8, fontfamily='sans-serif')
ax.text(39.5, avg_touches + 12, f'Avg Touches: {avg_touches:.0f}', color='#64748B', fontsize=8, fontfamily='sans-serif')

# Labels for each point
for i, name in enumerate(names):
    x = poss[i]
    y = touches[i]
    
    if name == 'London City':
        ax.annotate(
            f"★ {name}\n(49.8%, 487 Touches)",
            (x, y),
            xytext=(x - 4.5, y + 60),
            fontsize=10,
            fontweight='bold',
            color='#38BDF8',
            ha='center',
            arrowprops=dict(arrowstyle="->", color='#38BDF8', lw=1.5, connectionstyle="arc3,rad=-0.15"),
            zorder=6,
            bbox=dict(boxstyle="round,pad=0.4", fc="#0B132B", ec="#38BDF8", lw=1.5)
        )
    elif name in ['Arsenal', 'Manchester City', 'Chelsea']:
        ax.annotate(
            name,
            (x, y),
            xytext=(x, y + 25),
            fontsize=9,
            fontweight='bold',
            color='#FCD34D',
            ha='center',
            zorder=5
        )
    else:
        ax.annotate(
            name,
            (x, y),
            xytext=(x, y - 25),
            fontsize=8,
            color='#94A3B8',
            ha='center',
            zorder=5
        )

# Titles and Axis formatting
ax.set_title(
    "WSL 2024/25 · Possession % vs. Touches in Opposition Box",
    fontsize=14,
    fontweight='bold',
    color='#F8FAFC',
    pad=16,
    loc='left'
)
ax.set_xlabel("Possession Percentage (%)", fontsize=11, fontweight='semibold', color='#CBD5E1', labelpad=10)
ax.set_ylabel("Touches in Opposition Box (Total)", fontsize=11, fontweight='semibold', color='#CBD5E1', labelpad=10)

ax.set_xlim(38, 63)
ax.set_ylim(280, 960)

ax.grid(True, linestyle=':', alpha=0.25, color='#475569', zorder=1)
ax.tick_params(colors='#94A3B8', labelsize=9)

# Subtitle / Insight Note
fig.text(
    0.125, 0.90,
    "Midfield parity without final-third entry: LCL controlled tempo (#6 poss) but struggled to penetrate the penalty area (#7 touches)",
    fontsize=9,
    color='#94A3B8',
    fontstyle='italic'
)

plt.tight_layout()

# Save image
out_dir = Path('assets/images/evaluations')
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / 'lcl_possession_vs_box_touches.png'
plt.savefig(out_file, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()

print(f"Successfully generated: {out_file}")
