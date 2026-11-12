import json
from pathlib import Path

fp = Path('data/raw/fotmob/players/player_1414896_michelle_agyemang.json')
with open(fp, 'r', encoding='utf-8') as f:
    d = json.load(f)

nat = d.get('careerHistory', {}).get('careerItems', {}).get('national team', {})
print("National Team Entries:")
for entry in nat.get('teamEntries', []):
    print(entry)

print("\nNational Team Season Entries:")
for s in nat.get('seasonEntries', []):
    print(s.get('seasonName'), s.get('team'), 'apps:', s.get('appearances'), 'goals:', s.get('goals'), 'assists:', s.get('assists'))
    for t in s.get('tournamentStats', []):
        print('   *', t.get('leagueName'), t.get('seasonName'), 'apps:', t.get('appearances'), 'goals:', t.get('goals'), 'assists:', t.get('assists'))
