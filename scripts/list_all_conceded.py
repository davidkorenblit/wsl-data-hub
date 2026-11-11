import json

files = [
    'data/raw/fotmob/matches/mw1_bha_ars_5981533.json',
    'data/raw/fotmob/matches/mw2_cry_ars_5981639.json',
    'data/raw/fotmob/matches/mw3_mun_ars_5981644.json',
    'data/raw/fotmob/matches/mw4_che_ars_5981654.json',
    'data/raw/fotmob/matches/mw5_mci_ars_5981661.json',
    'data/raw/fotmob/matches/mw6_ars_bir_5981663.json',
    'data/raw/fotmob/matches/mw7_tot_ars_5981675.json',
    'data/raw/fotmob/matches/mw8_ars_avl_5981677.json',
    'data/raw/fotmob/matches/mw9_liv_ars_5981683.json'
]

total = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    gen = d.get('general', {})
    home = gen.get('homeTeam', {}).get('name')
    away = gen.get('awayTeam', {}).get('name')
    home_id = gen.get('homeTeam', {}).get('id')
    away_id = gen.get('awayTeam', {}).get('id')
    ars_id = home_id if 'Arsenal' in home else away_id
    opp_id = away_id if ars_id == home_id else home_id
    
    shotmap = d.get('content', {}).get('shotmap', {}).get('shots', [])
    events = d.get('content', {}).get('matchFacts', {}).get('events', {}).get('events', [])
    
    for s in shotmap:
        if s.get('teamId') == opp_id and s.get('eventType') == 'Goal':
            total += 1
            min_str = s.get('min')
            pname = s.get('playerName')
            xg = s.get('expectedGoals', 0)
            sit = s.get('situation')
            fb = s.get('fastBreak')
            
            # Find assist info from events
            assist_name = None
            for ev in events:
                if ev.get('type') == 'Goal' and ev.get('time') == min_str:
                    assist_name = ev.get('assistInput') or ev.get('assistStr')
            
            print(f"[{total}] {home} vs {away} | Min {min_str}' | Scorer: {pname} | Assist: {assist_name} | xG: {xg:.2f} | Sit: {sit} | FastBreak: {fb}")

print(f"\nTotal goals conceded by Arsenal: {total}")
