import requests, json

res = requests.get('https://www.fotmob.com/api/data/matchDetails?matchId=5981639', headers={'User-Agent': 'Mozilla/5.0'}).json()
content = res.get('content', {})
p_stats = content.get('playerStats', {})
print("playerStats keys:", list(p_stats.keys()) if isinstance(p_stats, dict) else type(p_stats))
if p_stats:
    # Print sample
    first_key = list(p_stats.keys())[0]
    print(f"Sample for {first_key}:", json.dumps(p_stats[first_key], indent=2)[:500])
