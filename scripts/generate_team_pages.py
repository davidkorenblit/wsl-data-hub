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

<div class="bg-surface-900 rounded-xl border border-surface-700/80 p-8 text-center">
  <p class="text-3xl mb-3">🚧</p>
  <h2 class="font-serif text-xl font-bold text-white mb-1">כפרה עובדים</h2>
  <p class="text-neutral-400 text-xs sm:text-sm">הניתוח המלא של {team['squad']} יפורסם בקרוב.</p>
</div>
"""
    path = teams_dir / f"{team['slug']}.md"
    path.write_text(content, encoding='utf-8')
    print(f"  Created: {path.name}")

print(f"Total: {len(teams)} pages")
