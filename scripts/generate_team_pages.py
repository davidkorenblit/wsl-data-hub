import json, os, pathlib

with open('wsl-data-hub/_data/league_table.json') as f:
    teams = json.load(f)

teams_dir = pathlib.Path('wsl-data-hub/teams')
teams_dir.mkdir(exist_ok=True)

for team in teams:
    content = f"""---
layout: team
title: "{team['squad']}"
team_name: "{team['squad']}"
team_slug: "{team['slug']}"
team_meta: "WSL 2025/26 · מיקום: {team['rk']}"
permalink: /teams/{team['slug']}/
---

<div class="bg-surface-800 rounded-2xl border border-surface-700 p-10 text-center shadow-xl">
  <p class="text-5xl mb-4">🚧</p>
  <h2 class="text-2xl font-bold text-white mb-2">כפרה עובדים</h2>
  <p class="text-slate-400">הניתוח המלא של {team['squad']} יפורסם בקרוב.</p>
</div>
"""
    path = teams_dir / f"{team['slug']}.md"
    path.write_text(content, encoding='utf-8')
    print(f"  Created: {path.name}")

print(f"Total: {len(teams)} pages")
