import json

with open('scratch_tot_ars.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

away = d['content']['lineup']['awayTeam']
print("Formation:", away.get('formation'))

for p in away['starters']:
    name = p.get('name')
    if any(n in name for n in ['Hinds', 'Foord', 'Smith', 'Russo', 'Batlle']):
        print(f"\n=== {name} | Rating: {p.get('rating', {}).get('num')} ===")
        for s in p.get('stats', []):
            title = s.get('title')
            stats = s.get('stats', {})
            vals = {}
            for k, v in stats.items():
                if isinstance(v, dict):
                    vals[k] = v.get('stat', {}).get('value')
                else:
                    vals[k] = v
            print(f"  {title}: {vals}")

# Also check Foord's historical goals vs Spurs if in shotmap
print("\nShots by Foord/Hinds/Smith/Russo:")
for s in d.get('content', {}).get('shotmap', {}).get('shots', []):
    if any(n in s.get('playerName', '') for n in ['Foord', 'Hinds', 'Smith', 'Russo']):
        print(f"  {s.get('playerName')}: min {s.get('min')}, xG {s.get('expectedGoals')}, type: {s.get('eventType')}")

