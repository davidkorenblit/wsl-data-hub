import json, os, pathlib

with open('wsl-data-hub/_data/league_table.json') as f:
    teams = json.load(f)

teams_dir = pathlib.Path('wsl-data-hub/teams')
teams_dir.mkdir(exist_ok=True)

for team in teams:
    path = teams_dir / f"{team['slug']}.md"
    if path.exists() and team['slug'] == 'london-city-lionesses':
        print(f"  Skipping custom page: {path.name}")
        continue

    content = f"""---
layout: team
title: "{team['squad']}"
team_name: "{team['squad']}"
team_slug: "{team['slug']}"
team_meta: "WSL 2025/26 · מיקום: {team['rk']}"
permalink: /teams/{team['slug']}/
---

<div class="rounded-md border border-neutral-200 bg-white p-8 text-center">
  <h2 class="font-serif text-xl font-semibold text-neutral-900 mb-1">כפרה עובדים</h2>
  <p class="text-neutral-500 text-xs sm:text-sm">הניתוח המלא של {team['squad']} יפורסם בקרוב.</p>
</div>
"""
    path.write_text(content, encoding='utf-8')
    print(f"  Created: {path.name}")

print(f"Total: {len(teams)} pages processed")
