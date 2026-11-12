import json

with open("scratch_lcl_mci.json", "r", encoding="utf-8") as f:
    d = json.load(f)

# Check lineup structure in content -> lineup -> awayTeam -> starters
# FotMob sometimes has 'role' or 'position' inside the starter dict or 'formation'
away = d['content']['lineup']['awayTeam']
for idx, p in enumerate(away.get('starters', [])):
    print(f"{idx+1}. {p.get('name')}: id={p.get('id')}, pos={p.get('position')}, isCaptain={p.get('isCaptain')}")

# Check if there are events mentioning Clinton
events = d['content']['matchFacts']['events']['events']
for e in events:
    if 'Clinton' in str(e):
        print("Event:", e.get('timeStr'), e.get('type'), e.get('player', {}).get('name'), e.get('cardDescription'), e.get('swap'))

# Check shotmap for Clinton
for s in d['content']['shotmap']['shots']:
    if 'Clinton' in str(s.get('playerName')):
        print("Shot:", s.get('min'), "xG:", s.get('expectedGoals'), "x:", s.get('x'), "y:", s.get('y'), "situation:", s.get('situation'))

