import json

with open("scratch_ars_avl.json", "r", encoding="utf-8") as f:
    d = json.load(f)

ps = d['content'].get('playerStats', {})
id_to_name = {}
for side in ['homeTeam', 'awayTeam']:
    t = d['content']['lineup'][side]
    for p in t.get('starters', []) + t.get('subs', []):
        id_to_name[str(p.get('id'))] = (p.get('name'), side, p.get('positionStringShort'))

for pid, stats in ps.items():
    pinfo = id_to_name.get(pid, (pid, 'unknown', ''))
    pname, side, pos = pinfo
    if any(n in pname for n in ['Williamson', 'Batlle', 'Hinds', 'Russo', 'Grant']):
        print(f"\n=== [{side}] {pname} ===")
        for grp in stats.get('stats', []):
            g_title = grp.get('title')
            items = []
            for k, v in grp.get('stats', {}).items():
                val = v.get('stat', {}).get('value') if isinstance(v, dict) else v
                items.append(f"{k}: {val}")
            print(f"  {g_title}: {', '.join(items)}")

