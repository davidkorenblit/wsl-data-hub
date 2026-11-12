import json

files = {
    "MW9 vs Liverpool (Olsson 15')": ('data/raw/fotmob/matches/mw9_liv_ars_5981683.json', 15),
    "MW8 vs Aston Villa (Grant 25')": ('data/raw/fotmob/matches/mw8_ars_avl_5981677.json', 25),
    "MW6 vs Birmingham (Hurtré 53')": ('data/raw/fotmob/matches/mw6_ars_bir_5981663.json', 53),
    "MW5 vs Man City (Shaw 84')": ('data/raw/fotmob/matches/mw5_mci_ars_5981661.json', 84),
    "MW3 vs Man United (Zigiotti 67')": ('data/raw/fotmob/matches/mw3_mun_ars_5981644.json', 67),
}

for name, (path, g_min) in files.items():
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print("=" * 60)
    print(f"MATCH: {name}")
    
    # Check shotmap
    shots = d.get('content', {}).get('shotmap', {}).get('shots', [])
    for s in shots:
        if s.get('min') == g_min:
            print(f"Shot: player={s.get('playerName')}, min={s.get('min')}, event={s.get('eventType')}, xG={s.get('expectedGoals')}, sit={s.get('situation')}, fastBreak={s.get('fastBreak')}, shotType={s.get('shotType')}, x={s.get('x')}, y={s.get('y')}")
    
    # Check events & matchFacts
    events = d.get('content', {}).get('matchFacts', {}).get('events', {}).get('events', [])
    for ev in events:
        if ev.get('time') == g_min:
            print(f"Event: type={ev.get('type')}, player={ev.get('player', {}).get('name')}, assist={ev.get('assistInput') or ev.get('assistStr')}, isHome={ev.get('isHome')}")
    
    # Check if there is momentum or timeline or commentary
    content = d.get('content', {})
    for key in ['liveticker', 'overview', 'matchFacts']:
        if key in content:
            pass
