import json
from pathlib import Path

scratch_files = sorted(Path('.').glob('scratch_*.json'))
teams_summary = {}

for f in scratch_files:
    try:
        d = json.load(open(f, encoding='utf-8'))
        content = d.get('content', {})
        stats = content.get('stats', {}).get('Periods', {}).get('All', {}).get('stats', [])
        mstats = {}
        for grp in stats:
            for s in grp.get('stats', []):
                mstats[s.get('title') or s.get('key')] = s.get('stats')
        gen = d.get('general', {})
        h_name = gen.get('homeTeam', {}).get('name')
        a_name = gen.get('awayTeam', {}).get('name')
        poss = mstats.get('Ball possession', [50, 50])
        box = mstats.get('Touches in opposition box', [0, 0])
        shots = mstats.get('Total shots', [0, 0])
        xg = mstats.get('Expected goals (xG)', [0, 0])
        
        for idx, tname in enumerate([h_name, a_name]):
            if not tname: continue
            if tname not in teams_summary:
                teams_summary[tname] = {'matches': 0, 'poss_list': [], 'box_list': [], 'shots_list': [], 'xg_list': []}
            t = teams_summary[tname]
            t['matches'] += 1
            t['poss_list'].append(float(poss[idx]))
            t['box_list'].append(float(box[idx]))
            t['shots_list'].append(float(shots[idx]))
            t['xg_list'].append(float(xg[idx]))
    except Exception:
        pass

print("=== TEAM BENCHMARKS ACROSS ALL SCRATCH MATCHES ===")
for tname, d in sorted(teams_summary.items(), key=lambda x: sum(x[1]['poss_list'])/len(x[1]['poss_list'])):
    avg_poss = sum(d['poss_list']) / len(d['poss_list'])
    avg_box = sum(d['box_list']) / len(d['box_list'])
    avg_shots = sum(d['shots_list']) / len(d['shots_list'])
    avg_xg = sum(d['xg_list']) / len(d['xg_list'])
    print(f"{tname:<32} | M:{d['matches']:<2} | Poss: {avg_poss:4.1f}% | Box: {avg_box:4.1f} | Shots: {avg_shots:4.1f} | xG: {avg_xg:4.2f}")

