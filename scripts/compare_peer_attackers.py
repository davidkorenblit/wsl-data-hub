import json
from pathlib import Path

LOW_POSS_TEAMS = ['Crystal Palace', 'West Ham United', 'Birmingham City', 'Aston Villa', 'Charlton', 'Everton']

scratch_files = sorted(Path('.').glob('scratch_*.json'))

player_data = {}

def get_stat(p, stat_name):
    for grp in p.get('stats', []):
        for sname, sdata in grp.get('stats', {}).items():
            if sname == stat_name:
                v = sdata.get('stat', {}).get('value')
                return v if v is not None else 0
    return 0

for fpath in scratch_files:
    try:
        d = json.load(open(fpath, encoding='utf-8'))
        ps = d.get('content', {}).get('playerStats', {})
        if not ps: continue
        for pid, p in ps.items():
            tname = p.get('teamName', '')
            matched_team = None
            for t in LOW_POSS_TEAMS:
                if t in tname:
                    matched_team = t
                    break
            if not matched_team: continue
            
            pos = p.get('usualPosition') # 2=MF, 3=FW
            if pos not in [2, 3]: continue
            
            mins = get_stat(p, 'Minutes played')
            if not mins or mins < 45: continue
            
            name = p.get('name')
            if name not in player_data:
                player_data[name] = {
                    'team': matched_team,
                    'pos': 'FW' if pos == 3 else 'AM/W',
                    'mins': 0,
                    'box_touches': 0,
                    'shots': 0,
                    'xg': 0.0,
                    'def_act': 0
                }
            rec = player_data[name]
            rec['mins'] += mins
            rec['box_touches'] += get_stat(p, 'Touches in opposition box')
            rec['shots'] += get_stat(p, 'Total shots')
            rec['xg'] += float(get_stat(p, 'Expected goals (xG)') or 0.0)
            rec['def_act'] += (get_stat(p, 'Interceptions') + get_stat(p, 'Recoveries') + get_stat(p, 'Tackles won'))
    except Exception:
        pass

print(f"{'Player':<22} | {'Team':<18} | {'Pos':<4} | {'Mins':<5} | {'BoxT/90':<7} | {'DefAct/90':<9} | {'Ratio':<8} | {'xG/Shot':<7}")
print("-" * 95)

rows = []
for name, d in player_data.items():
    if d['mins'] < 120: continue
    m90 = d['mins'] / 90.0
    box_p90 = d['box_touches'] / m90
    def_p90 = d['def_act'] / m90
    ratio = (def_p90 / box_p90) if box_p90 > 0 else 99.0
    xg_per_shot = (d['xg'] / d['shots']) if d['shots'] > 0 else 0.0
    rows.append((name, d['team'], d['pos'], d['mins'], box_p90, def_p90, ratio, xg_per_shot))

# Sort by ratio descending
rows.sort(key=lambda x: x[6], reverse=True)

for r in rows:
    tag = "🔴 PALACE" if r[1] == 'Crystal Palace' else "⚪ PEER"
    print(f"{r[0]:<22} | {r[1]:<18} | {r[2]:<4} | {r[3]:<5} | {r[4]:<7.2f} | {r[5]:<9.2f} | {r[6]:<8.2f} | {r[7]:<7.2f} {tag}")

