import json

with open('scratch_cry_whu.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

ps = d.get('content', {}).get('playerStats', {})
records = []

for pid, pdata in ps.items():
    name = pdata.get('name')
    team = pdata.get('teamName')
    
    stat_dict = {}
    for section in pdata.get('stats', []):
        section_stats = section.get('stats', {})
        if isinstance(section_stats, dict):
            for sname, sinfo in section_stats.items():
                s_stat = sinfo.get('stat', {})
                val = s_stat.get('value', 0)
                key = sinfo.get('key', sname)
                stat_dict[key] = val
                stat_dict[sname] = val
    
    mins = stat_dict.get('minutes_played', 0)
    if mins > 20:
        records.append({
            'name': name,
            'team': team,
            'mins': mins,
            'box_t': stat_dict.get('touches_opp_box', stat_dict.get('Touches in opposition box', 0)),
            'touches': stat_dict.get('touches', stat_dict.get('Touches', 0)),
            'def_act': stat_dict.get('defensive_actions', stat_dict.get('Defensive actions', 0)),
            'tackles': stat_dict.get('tackles', stat_dict.get('Tackles', 0)),
            'rec': stat_dict.get('recoveries', stat_dict.get('Recoveries', 0)),
            'shots': stat_dict.get('total_shots', stat_dict.get('Total shots', 0)),
            'xg': stat_dict.get('expected_goals', stat_dict.get('Expected goals (xG)', 0.0))
        })

print(f"{'Player':<22} | {'Team':<16} | {'Mins':<4} | {'BoxT':<5} | {'DefAct':<6} | {'Tack+Rec':<8} | {'Shots':<5} | {'xG':<5}")
print("-" * 85)
for r in sorted(records, key=lambda x: (x['team'], -x['box_t'])):
    print(f"{r['name']:<22} | {r['team']:<16} | {r['mins']:<4} | {r['box_t']:<5} | {r['def_act']:<6} | {r['tackles']}+{r['rec']:<6} | {r['shots']:<5} | {r['xg']:<5}")
