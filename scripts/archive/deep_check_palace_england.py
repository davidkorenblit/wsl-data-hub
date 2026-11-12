import json
from pathlib import Path

files = [
    ("MW5 (at Villa 1-1)", "scratch_avl_cry.json"),
    ("MW6 (vs West Ham 0-1)", "scratch_cry_whu.json"),
    ("MW7 (vs Chelsea 1-3)", "scratch_cry_che.json"),
    ("MW8 (at Brighton 1-2)", "scratch_bha_cry.json")
]

print("=== BETH ENGLAND & CRYSTAL PALACE MATCH-BY-MATCH DATA ===")
for label, fname in files:
    if not Path(fname).exists():
        continue
    d = json.load(open(fname, encoding='utf-8'))
    content = d.get('content', {})
    
    # Team stats
    stats_p = content.get('stats', {}).get('Periods', {}).get('All', {}).get('stats', [])
    mstats = {}
    for grp in stats_p:
        for s in grp.get('stats', []):
            mstats[s.get('title') or s.get('key')] = s.get('stats')
    
    # Player stats
    ps = content.get('playerStats', {})
    england_stat = None
    for pid, p in ps.items():
        if 'England' in p.get('name', ''):
            sdict = {}
            for grp in p.get('stats', []):
                for sname, sdata in grp.get('stats', {}).items():
                    sdict[sname] = sdata.get('stat', {}).get('value')
            england_stat = (p.get('name'), sdict)
            break
            
    print(f"\n📌 {label}")
    poss = mstats.get('Ball possession', ['?', '?'])
    shots = mstats.get('Total shots', ['?', '?'])
    xg = mstats.get('Expected goals (xG)', ['?', '?'])
    box = mstats.get('Touches in opposition box', ['?', '?'])
    passes = mstats.get('Accurate passes', ['?', '?'])
    
    # Determine which index is Palace
    general = d.get('general', {})
    home_is_palace = 'Palace' in general.get('homeTeam', {}).get('name', '')
    pal_idx = 0 if home_is_palace else 1
    opp_idx = 1 if home_is_palace else 0
    opp_name = general.get('awayTeam' if home_is_palace else 'homeTeam', {}).get('name')
    
    print(f"  Team: Possession: {poss[pal_idx]}% (vs {poss[opp_idx]}% {opp_name})")
    print(f"  Team: Shots: {shots[pal_idx]} (xG: {xg[pal_idx]}) | Touches in box: {box[pal_idx]} vs {box[opp_idx]}")
    print(f"  Team: Accurate passes: {passes[pal_idx]}")
    
    if england_stat:
        name, es = england_stat
        mins = es.get('Minutes played', 0)
        print(f"  Beth England ({mins} mins):")
        print(f"    Shots: {es.get('Total shots', 0)} | xG: {es.get('Expected goals (xG)', 0)} | Touches in box: {es.get('Touches in opposition box', 0)}")
        print(f"    Total Touches: {es.get('Touches', 0)} | Accurate Passes: {es.get('Accurate passes', 0)}")
        print(f"    Defensive Work: Recoveries: {es.get('Recoveries', 0)} | Interceptions: {es.get('Interceptions', 0)} | Tackles won: {es.get('Tackles won', 0)}")
        print(f"    Duels: Ground won: {es.get('Ground duels won', 0)} | Aerial won: {es.get('Aerial duels won', 0)} | Dispossessed: {es.get('Dispossessed', 0)}")

