import json

def inspect_match(filepath, title):
    with open(filepath, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(f"\n==================== {title} ====================")
    gen = d.get('general', {})
    h_team = gen.get('homeTeam', {}).get('name')
    a_team = gen.get('awayTeam', {}).get('name')
    print(f"Match: {h_team} vs {a_team}")
    
    ps = d.get('content', {}).get('playerStats', {})
    records = []
    for pid, pdata in ps.items():
        name = pdata.get('name')
        tname = pdata.get('teamName')
        stat_dict = {}
        for section in pdata.get('stats', []):
            section_stats = section.get('stats', {})
            if isinstance(section_stats, dict):
                for sname, sinfo in section_stats.items():
                    stat_dict[sinfo.get('key', sname)] = sinfo.get('stat', {}).get('value', 0)
        mins = stat_dict.get('minutes_played', 0)
        if mins >= 45:
            records.append({
                'name': name,
                'team': tname,
                'mins': mins,
                'pos': stat_dict.get('role', ''),
                'box_t': stat_dict.get('touches_opp_box', 0),
                'def_act': stat_dict.get('defensive_actions', 0),
                'tackles': stat_dict.get('tackles', 0),
                'rec': stat_dict.get('recoveries', 0),
                'shots': stat_dict.get('total_shots', 0),
                'xg': stat_dict.get('expected_goals', 0.0)
            })
    
    print(f"{'Player':<22} | {'Team':<20} | {'Mins':<4} | {'BoxT':<5} | {'DefAct':<6} | {'Tack+Rec':<8} | {'Shots':<5} | {'xG':<5}")
    print("-" * 85)
    for r in sorted(records, key=lambda x: (x['team'], -x['box_t'])):
        # only show front players or high box touch
        if r['box_t'] > 1 or r['shots'] > 0 or any(k in r['name'] for k in ['England', 'Larkin', 'Blanchard', 'Hopcroft', 'Vangsgaard', 'Grant', 'Daly', 'Asseyi', 'Gago']):
            print(f"{r['name']:<22} | {r['team']:<20} | {r['mins']:<4} | {r['box_t']:<5} | {r['def_act']:<6} | {r['tackles']}+{r['rec']:<8} | {r['shots']:<5} | {r['xg']:<5}")

inspect_match('scratch_avl_cry.json', 'ASTON VILLA vs CRYSTAL PALACE')
inspect_match('scratch_bha_whu.json', 'BRIGHTON vs WEST HAM')
inspect_match('scratch_bha_cry.json', 'BRIGHTON vs CRYSTAL PALACE')

