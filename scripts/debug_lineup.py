import requests, json

res = requests.get('https://www.fotmob.com/api/data/matchDetails?matchId=5981639', headers={'User-Agent': 'Mozilla/5.0'}).json()
content = res.get('content', {})
lineup = content.get('lineup', {})
for team_key in ['homeTeam', 'awayTeam']:
    t = lineup.get(team_key, {})
    print(f"\n=== {t.get('name')} (Team Rating: {t.get('rating')}) ===")
    for p in t.get('starters', []):
        name = p.get('name')
        rating = p.get('rating', {}).get('num', '-') if isinstance(p.get('rating'), dict) else p.get('rating')
        pos = p.get('usualPosition')
        print(f"  • {name} (Pos: {pos}) - Rating: {rating}")
        stats = p.get('stats', [])
        for grp in stats:
            for item in grp.get('stats', {}).values():
                title = item.get('title')
                val = item.get('stat', {}).get('value')
                if title in ['Total shots', 'Shots on target', 'Expected goals (xG)', 'Chances created', 'Saves', 'Goals prevented', 'Clearances', 'Blocks']:
                    print(f"      {title}: {val}")
