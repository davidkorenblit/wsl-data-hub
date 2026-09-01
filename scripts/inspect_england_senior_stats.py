import json
from pathlib import Path

fp = Path('data/raw/fotmob/players/player_1414896_michelle_agyemang.json')
with open(fp, 'r', encoding='utf-8') as f:
    d = json.load(f)

print("=== ALL MATCHES / STATS FOR ENGLAND SENIOR IN 2025 ===")
for ss in d.get('statSeasons', []):
    print(ss.get('seasonName'), ss.get('teamName'))
    for tour in ss.get('tournaments', []):
        print("  -", tour.get('name'), "goals:", tour.get('goals'), "matches:", tour.get('matches'), "started:", tour.get('started'), "minutes:", tour.get('minutes'))
