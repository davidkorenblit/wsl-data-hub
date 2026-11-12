import json

with open('_data/hampton_fotmob_raw.json', encoding='utf-8') as f:
    data = json.load(f)

recent = data.get('recentMatches', [])
print(f'Hampton has {len(recent)} recent matches:')
conceded_matches = []
for m in recent:
    opp = m.get('opponentTeamName')
    h_score = m.get('homeScore')
    a_score = m.get('awayScore')
    date = m.get('matchDate', {}).get('utcTime', '')[:10]
    mid = m.get('id')
    league = m.get('leagueName')
    team = m.get('teamName')
    is_home = m.get('isHomeTeam')
    
    # Did Chelsea concede in this match?
    conceded = 0
    if "Chelsea" in team:
        conceded = a_score if is_home else h_score
        if conceded is not None and conceded > 0:
            conceded_matches.append({
                "match_id": mid,
                "date": date,
                "opponent": opp,
                "score": f"{h_score}-{a_score}",
                "conceded": conceded,
                "league": league
            })

print(f"\nChelsea matches where Hampton conceded ({len(conceded_matches)}):")
for cm in conceded_matches:
    print(f"{cm['date']} | {cm['league']} | vs {cm['opponent']} | {cm['score']} (conceded {cm['conceded']}) | ID: {cm['match_id']}")

with open('_data/chelsea_hampton_conceded_matches.json', 'w', encoding='utf-8') as f:
    json.dump(conceded_matches, f, ensure_ascii=False, indent=2)
