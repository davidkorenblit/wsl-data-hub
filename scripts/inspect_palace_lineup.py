import json

d = json.load(open('scratch_bha_cry.json', encoding='utf-8'))
lineup = d.get('content', {}).get('lineup', {})
away_team = lineup.get('awayTeam', {})
players = away_team.get('players', [])

print(f"=== PALACE PLAYERS VS BRIGHTON (MW8) ===")
for pgrp in players:
    for p in pgrp:
        name = p.get('name', {}).get('fullName')
        pos = p.get('positionStringShort')
        stats = p.get('stats', [])
        # collect stats
        sdict = {}
        for s in stats:
            for item in s.get('stats', {}).values():
                title = item.get('key') or item.get('title')
                val = item.get('value')
                sdict[title] = val
        minutes = sdict.get('minutes_played') or p.get('minutesOnField')
        print(f"\n{name} ({pos}, {minutes} mins):")
        # print relevant stats
        for k in ['shots', 'expected_goals', 'touches_in_opposition_box', 'dispossessed', 'miscontrols',
                  'tackles_won', 'total_tackles', 'interceptions', 'recoveries', 'ground_duels_won',
                  'ground_duels', 'aerial_duels_won', 'aerial_duels', 'passes_accuracy']:
            if k in sdict:
                print(f"  {k}: {sdict[k]}")

