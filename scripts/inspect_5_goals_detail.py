import json

def inspect_match(fpath, target_min):
    with open(fpath, 'r', encoding='utf-8') as f:
        d = json.load(f)
    gen = d.get('general', {})
    home = gen.get('homeTeam', {}).get('name')
    away = gen.get('awayTeam', {}).get('name')
    print(f"\n==========================================")
    print(f"MATCH: {home} vs {away} (min {target_min})")
    
    # 1. Shotmap around target_min
    shots = d.get('content', {}).get('shotmap', {}).get('shots', [])
    for s in shots:
        if abs(s.get('min', 0) - target_min) <= 1:
            print(f"  SHOT: min={s.get('min')}', player={s.get('playerName')}, event={s.get('eventType')}, xG={s.get('expectedGoals'):.3f}, sit={s.get('situation')}, fastBreak={s.get('fastBreak')}, shotType={s.get('shotType')}, box={s.get('isFromInsideBox')}, x={s.get('x')}, y={s.get('y')}")
    
    # 2. Events in matchFacts
    events = d.get('content', {}).get('matchFacts', {}).get('events', {}).get('events', [])
    for ev in events:
        if abs(ev.get('time', 0) - target_min) <= 1:
            p = ev.get('player', {}).get('name')
            typ = ev.get('type')
            assist = ev.get('assistInput') or ev.get('assistStr')
            print(f"  EVENT: time={ev.get('time')}', type={typ}, player={p}, assist={assist}")

    # 3. Check playerStats for the assister and scorer
    pstats = d.get('content', {}).get('playerStats', {})
    for pid, pdata in pstats.items():
        name = pdata.get('name')
        # if scorer or assister
        # check stats
        pass

inspect_match('data/raw/fotmob/matches/mw9_liv_ars_5981683.json', 15)
inspect_match('data/raw/fotmob/matches/mw8_ars_avl_5981677.json', 25)
inspect_match('data/raw/fotmob/matches/mw6_ars_bir_5981663.json', 53)
inspect_match('data/raw/fotmob/matches/mw5_mci_ars_5981661.json', 84)
inspect_match('data/raw/fotmob/matches/mw3_mun_ars_5981644.json', 67)
