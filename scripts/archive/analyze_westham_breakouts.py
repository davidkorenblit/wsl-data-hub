import json

def analyze_match_turnovers(filepath, label):
    with open(filepath, "r", encoding="utf-8") as fp:
        d = json.load(fp)
    
    print(f"\n==================== {label} ====================")
    content = d.get("content", {})
    stats = content.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", [])
    
    for grp in stats:
        for s in grp.get("stats", []):
            if any(k in s.get("title", "").lower() for k in ["possession", "tackle", "interception", "recovery", "duel", "pass", "dispossessed", "box", "xg"]):
                print(f"  {s.get('title')}: {s.get('stats')}")
                
    # Player stats for West Ham key players
    pstats = content.get("playerStats", {})
    print(f"\n  West Ham Key Players in {label}:")
    for pid, pdata in pstats.items():
        name = pdata.get("name", "")
        if any(k in name for k in ["Asseyi", "Gago", "Piubel", "Zelem", "Siren"]):
            sd = {}
            for sec in pdata.get("stats", []):
                for sname, sinfo in sec.get("stats", {}).items():
                    sd[sinfo.get("key", sname)] = sinfo.get("stat", {}).get("value", 0)
            print(f"    {name:<18} | Mins: {sd.get('minutes_played', 0):<2} | Touches: {sd.get('touches', 0):<2} | BoxT: {sd.get('touches_opp_box', 0):<2} | Dispossessed: {sd.get('dispossessed', 0):<2} | DuelsLost: {sd.get('duels_lost', 0):<2} | PassesAcc: {sd.get('accurate_passes', 0)}")

analyze_match_turnovers("data/raw/fotmob/matches/mw9_mci_whu_5981687.json", "Man City 5 - 0 West Ham (MW9)")
analyze_match_turnovers("data/raw/fotmob/matches/mw8_whu_liv_5981682.json", "West Ham 4 - 1 Liverpool (MW8)")
analyze_match_turnovers("data/raw/fotmob/matches/mw7_bha_whu_5981671.json", "Brighton 2 - 2 West Ham (MW7)")
