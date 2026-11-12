import json

with open("scratch_whu_liv.json", "r", encoding="utf-8") as f:
    d = json.load(f)

ps = d['content'].get('playerStats', {})
id_to_name = {}
for side in ['homeTeam', 'awayTeam']:
    t = d['content']['lineup'][side]
    for p in t.get('starters', []) + t.get('subs', []):
        id_to_name[str(p.get('id'))] = (p.get('name'), side, p.get('positionStringShort'))

print("=== WEST HAM KEY PLAYERS vs LIVERPOOL ===")
for pid, stats in ps.items():
    pname, side, pos = id_to_name.get(pid, (pid, 'unknown', ''))
    if side == "homeTeam" and any(n in pname for n in ['Asseyi', 'Wandeler', 'Endemann', 'Gorry', 'Piubel', 'Itamura', 'Mengwen']):
        print(f"\n[{side}] {pname} (Pos: {pos}):")
        for grp in stats.get('stats', []):
            g_title = grp.get('title')
            items = []
            for k, v in grp.get('stats', {}).items():
                val = v.get('stat', {}).get('value') if isinstance(v, dict) else v
                items.append(f"{k}: {val}")
            print(f"  {g_title}: {', '.join(items)}")

# Check Liverpool keeper stats (Khiara Keating)
for pid, stats in ps.items():
    pname, side, pos = id_to_name.get(pid, (pid, 'unknown', ''))
    if "Keating" in pname:
        print(f"\n[LIV Keeper] {pname}:")
        for grp in stats.get('stats', []):
            items = [f"{k}: {v.get('stat', {}).get('value') if isinstance(v, dict) else v}" for k, v in grp.get('stats', {}).items()]
            print(f"  {grp.get('title')}: {', '.join(items)}")

