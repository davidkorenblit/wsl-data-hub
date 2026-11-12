import json
from pathlib import Path

fp = Path('data/raw/fotmob/players/player_1414896_michelle_agyemang.json')
with open(fp, 'r', encoding='utf-8') as f:
    d = json.load(f)

print("=== MICHELLE AGYEMANG: FOTMOB IN-DEPTH TRAITS & METRICS ===")
stats_sec = d.get('firstSeasonStats', {}).get('statsSection', {}).get('items', [])
for sec in stats_sec:
    print(f"\n--- {sec.get('title', 'Section')} ---")
    for it in sec.get('items', []):
        t = it.get('title')
        val = it.get('statValue')
        p90 = it.get('per90')
        pct = it.get('percentileRank')
        print(f"  * {t}: Value={val}, Per90={p90}, Percentile={pct}%")
