import json

matches = [
    ("MW1 vs LCL (1:2)", r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\mw1_lcl_mun_5981531.json"),
    ("MW2 vs Chelsea (0:5)", r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\match_5981635.json"),
    ("MW3 vs Arsenal (1:1)", r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\mw3_mun_ars_5981644.json"),
    ("MW4 vs West Ham (2:1)", r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\mw4_mun_whu_5981650.json"),
    ("MW5 vs Liverpool (1:0)", r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\mw5_mun_liv_5981656.json"),
]

for label, fpath in matches:
    print(f"\n{'='*20} {label} {'='*20}")
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    content = data.get("content", {})
    lineup = content.get("lineup", {})
    mun = lineup.get("homeTeam") if "Manchester United" in lineup.get("homeTeam", {}).get("name", "") else lineup.get("awayTeam")
    
    starters = mun.get("starters", [])
    subs = mun.get("subs", [])
    
    medina = None
    for p in starters + subs:
        raw_name = p.get("name")
        name = raw_name if isinstance(raw_name, str) else raw_name.get("fullName", "")
        if "medina" in name.lower():
            medina = p
            break
            
    if not medina:
        print("Andrea Medina not found in lineup!")
        continue
        
    pid = str(medina.get("id"))
    pos_short = medina.get("positionStringShort")
    pos_id = medina.get("positionId")
    usual_pos = medina.get("usualPlayingPositionId")
    h_layout = medina.get("horizontalLayout")
    v_layout = medina.get("verticalLayout")
    
    # Check playerStats
    ps = content.get("playerStats", {}).get(pid, {})
    stat_groups = ps.get("stats", [])
    
    flat_stats = {}
    for grp in stat_groups:
        for k, v in grp.get("stats", {}).items():
            s = v.get("stat", {})
            val = s.get("value")
            tot = s.get("total")
            flat_stats[k] = f"{val}/{tot}" if tot is not None else val
            
    rating = flat_stats.get("FotMob rating")
    minutes = flat_stats.get("Minutes played")
    tackles = flat_stats.get("Tackles")
    interceptions = flat_stats.get("Interceptions")
    recoveries = flat_stats.get("Recoveries")
    clearances = flat_stats.get("Clearances")
    dribbles = flat_stats.get("Successful dribbles")
    chances = flat_stats.get("Chances created")
    crosses = flat_stats.get("Accurate crosses")
    ground_duels = flat_stats.get("Ground duels won")
    aerial_duels = flat_stats.get("Aerial duels won")
    duels_won = flat_stats.get("Duels won")
    duels_lost = flat_stats.get("Duels lost")
    passes = flat_stats.get("Accurate passes")
    touches = flat_stats.get("Touches")
    dribbled_past = flat_stats.get("Dribbled past")
    
    print(f"Position: {pos_short} (H:{h_layout}, V:{v_layout}) | Usual: {usual_pos} | Min: {minutes} | Rating: {rating}")
    print(f"  Tackles: {tackles} | Itc: {interceptions} | Rec: {recoveries} | Clr: {clearances} | DribPast: {dribbled_past}")
    print(f"  Duels: Won {duels_won} / Lost {duels_lost} (Ground: {ground_duels}, Aerial: {aerial_duels})")
    print(f"  Attack: Touches: {touches} | Passes: {passes} | Dribbles: {dribbles} | Chances: {chances} | Crosses: {crosses}")
