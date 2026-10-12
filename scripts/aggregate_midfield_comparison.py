import json

matches = [
    ("MW1 vs LCL", r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\mw1_lcl_mun_5981531.json", "before"),
    ("MW2 vs Chelsea", r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\match_5981635.json", "before"),
    ("MW3 vs Arsenal", r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\mw3_mun_ars_5981644.json", "after"),
    ("MW4 vs West Ham", r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\mw4_mun_whu_5981650.json", "after"),
    ("MW5 vs Liverpool", r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\mw5_mun_liv_5981656.json", "after"),
]

def extract_stat_val(stats_dict, stat_name):
    for grp in stats_dict:
        stats = grp.get('stats', {})
        if stat_name in stats:
            s = stats[stat_name].get('stat', {})
            val = s.get('value')
            if val is not None:
                return val
    return 0

mid_players = ["Hinata Miyazawa", "Julia Zigiotti Olme", "Ella Toone", "Simi Awujo"]

results = {
    "before": {"tackles": 0, "itc": 0, "recoveries": 0, "dribbled_past": 0, "duels_won": 0, "def_actions": 0, "matches": 2},
    "after": {"tackles": 0, "itc": 0, "recoveries": 0, "dribbled_past": 0, "duels_won": 0, "def_actions": 0, "matches": 3}
}

for label, fpath, phase in matches:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    content = data.get("content", {})
    player_stats = content.get("playerStats", {})
    lineup = content.get("lineup", {})
    mun = lineup.get("homeTeam") if "Manchester United" in lineup.get("homeTeam", {}).get("name", "") else lineup.get("awayTeam")
    all_p = mun.get("starters", []) + mun.get("subs", [])
    
    print(f"\n--- {label} ({phase}) ---")
    for p in all_p:
        raw_name = p.get("name")
        name = raw_name if isinstance(raw_name, str) else raw_name.get("fullName", "")
        if any(m.lower() in name.lower() for m in mid_players):
            pid = str(p.get("id"))
            ps = player_stats.get(pid, {})
            stats_groups = ps.get("stats", [])
            
            min_played = extract_stat_val(stats_groups, "Minutes played")
            if min_played == 0: continue
            
            tkl = extract_stat_val(stats_groups, "Tackles")
            itc = extract_stat_val(stats_groups, "Interceptions")
            rec = extract_stat_val(stats_groups, "Recoveries")
            dp = extract_stat_val(stats_groups, "Dribbled past")
            dw = extract_stat_val(stats_groups, "Duels won")
            da = extract_stat_val(stats_groups, "Defensive actions")
            
            results[phase]["tackles"] += tkl
            results[phase]["itc"] += itc
            results[phase]["recoveries"] += rec
            results[phase]["dribbled_past"] += dp
            results[phase]["duels_won"] += dw
            results[phase]["def_actions"] += da
            
            print(f"  {name:20s}: Tkl={tkl}, Itc={itc}, Rec={rec}, DribPast={dp}, DuelsWon={dw}, DefAct={da}")

print("\n" + "="*50)
print("AGGREGATE MIDFIELD COMPARISON (Miyazawa + Zigiotti + Toone + Awujo):")
b = results["before"]
a = results["after"]
print(f"BEFORE (MW1-2, 2 games):")
print(f"  Tackles: {b['tackles']} ({b['tackles']/2:.1f}/game)")
print(f"  Interceptions: {b['itc']} ({b['itc']/2:.1f}/game)")
print(f"  Recoveries: {b['recoveries']} ({b['recoveries']/2:.1f}/game)")
print(f"  Dribbled past (Bypassed!): {b['dribbled_past']} ({b['dribbled_past']/2:.1f}/game)")
print(f"  Duels won: {b['duels_won']} ({b['duels_won']/2:.1f}/game)")
print(f"  Defensive actions: {b['def_actions']} ({b['def_actions']/2:.1f}/game)")

print(f"\nAFTER (MW3-5, 3 games):")
print(f"  Tackles: {a['tackles']} ({a['tackles']/3:.1f}/game)")
print(f"  Interceptions: {a['itc']} ({a['itc']/3:.1f}/game)")
print(f"  Recoveries: {a['recoveries']} ({a['recoveries']/3:.1f}/game)")
print(f"  Dribbled past (Bypassed!): {a['dribbled_past']} ({a['dribbled_past']/3:.1f}/game)")
print(f"  Duels won: {a['duels_won']} ({a['duels_won']/3:.1f}/game)")
print(f"  Defensive actions: {a['def_actions']} ({a['def_actions']/3:.1f}/game)")
