import json
from pathlib import Path

raw_dir = Path("data/raw/fotmob/matches")

match_files = {
    "lcl_mancity": "mw8_lcl_mci_5981681.json",
    "charlton_chelsea": "mw8_cha_che_5981680.json",
    "arsenal_villa": "mw8_ars_avl_5981677.json",
    "birmingham_tottenham": "mw8_bir_tot_5981678.json",
    "westham_liverpool": "mw8_whu_liv_5981682.json",
    "brighton_palace": "mw8_bha_cry_5981679.json",
    "everton_manutd": "mw8_eve_mun_5981676.json"
}

output_data = {
    "round": 8,
    "season": "2026/27",
    "matches": {}
}

for key, fname in match_files.items():
    fpath = raw_dir / fname
    if not fpath.exists():
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        d = json.load(f)
        
    header_teams = d.get("header", {}).get("teams", [])
    home_name = header_teams[0].get("name", "") if len(header_teams) > 0 else ""
    away_name = header_teams[1].get("name", "") if len(header_teams) > 1 else ""
    home_score = header_teams[0].get("score", 0) if len(header_teams) > 0 else 0
    away_score = header_teams[1].get("score", 0) if len(header_teams) > 1 else 0
    score_str = f"{home_score} - {away_score}"
    
    # parse stats
    stats_periods = d.get("content", {}).get("stats", {}).get("Periods", {}).get("All", {}).get("stats", [])
    
    stat_map = {}
    for group in stats_periods:
        for item in group.get("stats", []):
            stat_map[item.get("title")] = item.get("stats")
            
    xg = stat_map.get("Expected goals (xG)", [None, None])
    shots = stat_map.get("Total shots", [None, None])
    sot = stat_map.get("Shots on target", [None, None])
    poss = stat_map.get("Ball possession", [None, None])
    bc = stat_map.get("Big chances", [None, None])
    touches_box = stat_map.get("Touches in opposition box", [None, None])
    
    # parse goals
    events = d.get("content", {}).get("matchFacts", {}).get("events", {}).get("events", [])
    goals_list = []
    for ev in events:
        if ev.get("type") == "Goal":
            pname = ev.get("nameStr") or ev.get("player", {}).get("name") or ev.get("fullName", "")
            is_home = ev.get("isHome", True)
            tname = home_name if is_home else away_name
            goals_list.append({
                "player": pname,
                "min": f"{ev.get('timeStr', ev.get('time', ''))}'",
                "team": tname
            })
            
    output_data["matches"][key] = {
        "title": f"{home_name} {score_str} {away_name}",
        "home_team": home_name,
        "away_team": away_name,
        "score": score_str,
        "xg": {"home": float(xg[0]) if xg and xg[0] is not None else None, "away": float(xg[1]) if xg and xg[1] is not None else None},
        "shots": {"home": int(shots[0]) if shots and shots[0] is not None else None, "away": int(shots[1]) if shots and shots[1] is not None else None},
        "sot": {"home": int(sot[0]) if sot and sot[0] is not None else None, "away": int(sot[1]) if sot and sot[1] is not None else None},
        "possession": {"home": int(poss[0]) if poss and poss[0] is not None else None, "away": int(poss[1]) if poss and poss[1] is not None else None},
        "big_chances": {"home": int(bc[0]) if bc and bc[0] is not None else None, "away": int(bc[1]) if bc and bc[1] is not None else None},
        "touches_in_box": {"home": int(touches_box[0]) if touches_box and touches_box[0] is not None else None, "away": int(touches_box[1]) if touches_box and touches_box[1] is not None else None},
        "goals": goals_list
    }

out_path = Path("_data/mw8_analysis.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"Generated {out_path} with {len(output_data['matches'])} matches.")
