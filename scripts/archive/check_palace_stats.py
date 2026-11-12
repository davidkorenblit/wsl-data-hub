import json
from pathlib import Path

print("=== CRYSTAL PALACE AVAILABLE SCRATCH MATCHES ===")
for p in sorted(Path('.').glob('scratch_*cry*.json')):
    d = json.load(open(p, encoding='utf-8'))
    content = d.get('content', {})
    stats_p = content.get('stats', {}).get('Periods', {}).get('All', {}).get('stats', [])
    mstats = {}
    for grp in stats_p:
        for s in grp.get('stats', []):
            key = s.get('title') or s.get('key')
            mstats[key] = s.get('stats')
    general = d.get('general', {})
    home = general.get('homeTeam', {}).get('name')
    away = general.get('awayTeam', {}).get('name')
    score = f"{general.get('homeTeam', {}).get('score')} - {general.get('awayTeam', {}).get('score')}"
    print(f"\nFile: {p.name} | Match: {home} {score} {away}")
    print(f"  Possession: {mstats.get('Ball possession')}")
    print(f"  xG: {mstats.get('Expected goals (xG)')}")
    print(f"  Total shots: {mstats.get('Total shots')} | Shots on target: {mstats.get('Shots on target')}")
    print(f"  Big chances: {mstats.get('Big chances')} | Missed: {mstats.get('Big chances missed')}")
    print(f"  Touches in opp box: {mstats.get('Touches in opposition box')}")
    print(f"  Total passes: {mstats.get('Passes')} | Accurate passes: {mstats.get('Accurate passes')}")
    print(f"  Tackles won: {mstats.get('Tackles won')} | Interceptions: {mstats.get('Interceptions')}")

