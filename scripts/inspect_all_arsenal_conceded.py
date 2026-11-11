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
    opp_name = away if ars_id == home_id else home
    
    shotmap = d.get('content', {}).get('shotmap', {}).get('shots', [])
    events = d.get('content', {}).get('matchFacts', {}).get('events', {}).get('events', [])
    
    opp_goals = [s for s in shotmap if s.get('teamId') == opp_id and s.get('eventType') == 'Goal']
    
    if opp_goals:
        print(f"=== {home} vs {away} (Goals against Arsenal: {len(opp_goals)}) ===")
        for s in opp_goals:
            pname = s.get('playerName')
            min_str = s.get('min')
            min_added = s.get('minAdded')
            m_display = f"{min_str}+{min_added}" if min_added else f"{min_str}"
            xg = s.get('expectedGoals')
            sit = s.get('situation')
            fb = s.get('fastBreak')
            shot_type = s.get('shotType')
            box = "Inside Box" if s.get('isBox') or s.get('box') else "Outside Box"
            x, y = s.get('x'), s.get('y')
            print(f"  ⚽ Goal by {pname} at {m_display}'")
            print(f"     xG: {xg}, situation: {sit}, fastBreak: {fb}, shotType: {shot_type}, coords: ({x:.1f}, {y:.1f})")
            
            # Find commentary or event description
            for ev in events:
                if ev.get('type') == 'Goal' and ev.get('time') == s.get('min'):
                    print(f"     Event: {ev}")
