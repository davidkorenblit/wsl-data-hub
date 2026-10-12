import json

matches = [
    ("MW1 vs LCL (1:2 L)", r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\mw1_lcl_mun_5981531.json"),
    ("MW2 vs Chelsea (0:5 L)", r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\match_5981635.json"),
    ("MW3 vs Arsenal (1:1 D)", r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\mw3_mun_ars_5981644.json"),
    ("MW4 vs West Ham (2:1 W)", r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\mw4_mun_whu_5981650.json"),
    ("MW5 vs Liverpool (1:0 W)", r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\mw5_mun_liv_5981656.json"),
]

def extract_stat_val(stats_dict, group_title, stat_name):
    # Search across groups
    for grp in stats_dict:
        # if group_title and grp.get('title') != group_title: continue
        stats = grp.get('stats', {})
        if stat_name in stats:
            s = stats[stat_name].get('stat', {})
            val = s.get('value')
            tot = s.get('total')
            if tot is not None:
                return f"{val}/{tot}"
            return val
    return 0

for label, fpath in matches:
    print(f"\n==================== {label} ====================")
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    content = data.get("content", {})
    lineup = content.get("lineup", {})
    home = lineup.get("homeTeam", {})
    away = lineup.get("awayTeam", {})
    mun = home if "Manchester United" in home.get("name", "") else away
    
    player_stats = content.get("playerStats", {})
    
    # We want to identify the midfield unit:
    # Starters positions 5, 6, 7, 8 usually correspond to DM, DM, AM or wingers
    # Let's inspect all starters and any sub midfielders who played
    starters = mun.get("starters", [])
    subs = mun.get("subs", [])
    all_players = starters + subs
    
    print(f"{'Player':22s} | {'Pos':5s} | {'Min':3s} | {'Rat':4s} | {'Tkl':3s} | {'Itc':3s} | {'Rec':3s} | {'DefAct':6s} | {'DuelsW/T':8s} | {'DribPast':8s} | {'Passes':7s} | {'Touches':7s}")
    print("-" * 105)
    
    # Midfielders list of interest:
    mid_names = [
        "Hinata Miyazawa", "Julia Zigiotti Olme", "Ella Toone", "Simi Awujo", 
        "Dominique Janssen", "Jessica Park", "Hayley Ladd", "Lisa Naalsund", "Grace Clinton"
    ]
    
    # Also let's check all starters who played in midfield
    for p in all_players:
        raw_name = p.get("name")
        name = raw_name if isinstance(raw_name, str) else raw_name.get("fullName", "")
        pid = str(p.get("id"))
        pos = p.get("positionStringShort", "")
        
        ps = player_stats.get(pid, {})
        stats_groups = ps.get("stats", [])
        if not stats_groups:
            continue
            
        minutes = extract_stat_val(stats_groups, "Top stats", "Minutes played")
        if not minutes or minutes == 0:
            continue
            
        rating = extract_stat_val(stats_groups, "Top stats", "FotMob rating")
        tackles = extract_stat_val(stats_groups, "Defense", "Tackles")
        interceptions = extract_stat_val(stats_groups, "Defense", "Interceptions")
        recoveries = extract_stat_val(stats_groups, "Defense", "Recoveries")
        def_actions = extract_stat_val(stats_groups, "Defense", "Defensive actions")
        dribbled_past = extract_stat_val(stats_groups, "Defense", "Dribbled past")
        ground_duels = extract_stat_val(stats_groups, "Duels", "Ground duels won")
        duels_won = extract_stat_val(stats_groups, "Duels", "Duels won")
        duels_lost = extract_stat_val(stats_groups, "Duels", "Duels lost")
        accurate_passes = extract_stat_val(stats_groups, "Top stats", "Accurate passes")
        touches = extract_stat_val(stats_groups, "Attack", "Touches")
        
        # Check if in midfield or relevant
        is_mid = any(m.lower() in name.lower() for m in mid_names) or pos in ["CM", "DM", "AM", "LM", "RM", "M"]
        
        # If it's a starter or played significant minutes
        if is_mid or pos in ["CM", "DM", "AM"]:
            duel_str = f"{duels_won}/{int(duels_won or 0) + int(duels_lost or 0)}" if duels_won else "-"
            print(f"{name:22s} | {pos:5s} | {str(minutes):3s} | {str(rating):4s} | {str(tackles):3s} | {str(interceptions):3s} | {str(recoveries):3s} | {str(def_actions):6s} | {duel_str:8s} | {str(dribbled_past):8s} | {str(accurate_passes):7s} | {str(touches):7s}")

