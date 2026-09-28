import requests, json

res = requests.get('https://www.fotmob.com/api/data/matchDetails?matchId=5981638', headers={'User-Agent': 'Mozilla/5.0'}).json()
content = res.get('content', {})
lineup = content.get('lineup', {})
away = lineup.get('awayTeam', {})
print("Tottenham Formation:", away.get('formation'))
for p in away.get('starters', []):
    print(f"  {p.get('name')}")

zones = content.get('attackingZones', {})
print("Attacking Zones:")
print(json.dumps(zones, indent=2))
