"""
Parse Arsenal 2025/26 Squad & Transfers
Extracts all players from FotMob squad structure and sets up player comparisons.
"""

import json
from pathlib import Path

with open("data/raw/fotmob/teams/team_258657_arsenal_women.json", "r", encoding="utf-8") as f:
    d = json.load(f)

squad_obj = d.get("squad", {})
squad_groups = squad_obj.get("squad", []) if isinstance(squad_obj, dict) else []

print(f"Squad groups found: {len(squad_groups)}")

parsed_squad = []
for group in squad_groups:
    group_title = group.get("title", "") # e.g. "goalkeepers", "defenders", "midfielders", "forwards"
    members = group.get("members", [])
    for m in members:
        parsed_squad.append({
            "id": m.get("id"),
            "name": m.get("name"),
            "shirt_number": m.get("cname"),
            "role": group_title,
            "position": m.get("role", {}).get("key") if isinstance(m.get("role"), dict) else m.get("role")
        })

print(f"Total Arsenal players in squad: {len(parsed_squad)}")
for p in parsed_squad:
    print(f"  #{p.get('shirt_number') or '--':<3} {p.get('name'):<25} | {p.get('role'):<15} (ID: {p.get('id')})")

# Save structured squad to _data/squads/arsenal.json
squad_out = Path("_data/squads/arsenal.json")
squad_out.parent.mkdir(parents=True, exist_ok=True)
with open(squad_out, "w", encoding="utf-8") as f:
    json.dump({"team": "Arsenal Women", "season": "2025/26", "players": parsed_squad}, f, indent=2, ensure_ascii=False)

print(f"\nSaved structured squad to: {squad_out}")
