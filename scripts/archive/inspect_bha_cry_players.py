import json

d = json.load(open('scratch_bha_cry.json', encoding='utf-8'))
ps = d.get('content', {}).get('playerStats', {})

print("\n=== CRYSTAL PALACE PLAYERS VS BRIGHTON (MW8) ===")
for pid, p in ps.items():
    tname = p.get('teamName', '')
    if 'Palace' in tname or 'Crystal' in tname:
        name = p.get('name')
        usual_pos = p.get('usualPosition')
        sdict = {}
        for grp in p.get('stats', []):
            for sname, sdata in grp.get('stats', {}).items():
                sdict[sname] = sdata.get('stat', {}).get('value')
        minutes = sdict.get('Minutes played', 0)
        if minutes and minutes > 0:
            rating = sdict.get('FotMob rating')
            shots = sdict.get('Total shots', 0)
            xg = sdict.get('Expected goals (xG)', 0)
            box_touches = sdict.get('Touches in opposition box', 0)
            touches = sdict.get('Touches', 0)
            passes = f"{sdict.get('Accurate passes', 0)}"
            tackles = sdict.get('Tackles won', 0)
            interceptions = sdict.get('Interceptions', 0)
            recoveries = sdict.get('Recoveries', 0)
            duels_won = sdict.get('Ground duels won', 0)
            aerial_won = sdict.get('Aerial duels won', 0)
            disp = sdict.get('Dispossessed', 0)
            
            print(f"{name} ({usual_pos}) | {minutes}' | Rating: {rating}")
            print(f"  Attack: xG: {xg} | Shots: {shots} | Box Touches: {box_touches} | Touches: {touches}")
            print(f"  Defense/Work: Interceptions: {interceptions} | Recoveries: {recoveries} | Tackles won: {tackles}")
            print(f"  Duels/Loss: Ground won: {duels_won} | Aerial won: {aerial_won} | Dispossessed: {disp}")
            print()

print("\n=== BRIGHTON: FRAN KIRBY ===")
for pid, p in ps.items():
    if p.get('name') == 'Fran Kirby':
        sdict = {}
        for grp in p.get('stats', []):
            for sname, sdata in grp.get('stats', {}).items():
                sdict[sname] = sdata.get('stat', {}).get('value')
        print(f"Fran Kirby: {sdict.get('Minutes played')}' | Rating: {sdict.get('FotMob rating')}")
        print(f"  xG: {sdict.get('Expected goals (xG)')} | xA: {sdict.get('Expected assists (xA)')} | Chances created: {sdict.get('Chances created')}")
        print(f"  Touches: {sdict.get('Touches')} | Box Touches: {sdict.get('Touches in opposition box')}")
