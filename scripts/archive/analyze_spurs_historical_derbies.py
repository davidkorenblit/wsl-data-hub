import json
import os

files = {
    "Chelsea 1-0 Spurs (MW6 25/26)": r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\match_4892993_chelsea_spurs_1_0.json",
    "Spurs 0-0 Arsenal (MW9 25/26)": r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\match_4893135_spurs_arsenal_0_0.json",
    "Arsenal 5-2 Spurs (MW19 25/26)": r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\matches\match_4893222_arsenal_spurs_5_2.json"
}

for title, path in files.items():
    print(f"\n{'='*25} {title} {'='*25}")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    content = data.get("content", {})
    stats_data = content.get("stats", {})
    # Team stats
    periods = stats_data.get("Periods", {}).get("All", {}).get("stats", [])
    
    stat_map = {}
    for p in periods:
        items = p.get("stats", [])
        for item in items:
            key = item.get("title")
            val = item.get("stats")
            stat_map[key] = val
            
    # Lineup info
    lineup = content.get("lineup", {})
    home = lineup.get("homeTeam", {})
    away = lineup.get("awayTeam", {})
    
    spurs = home if "Tottenham" in home.get("name", "") else away
    opp = away if spurs == home else home
    
    print(f"Spurs Home/Away: {'Home' if spurs == home else 'Away'} | Formation: {spurs.get('formation')} vs Opp: {opp.get('name')} ({opp.get('formation')})")
    
    # Print key match stats
    for k in ["Possession", "Expected goals (xG)", "Total shots", "Shots on target", "Big chances", "Clearances", "Tackles", "Interceptions", "Saves", "Corner kicks", "Accurate passes"]:
        if k in stat_map:
            print(f"  {k:25s}: {stat_map[k]}")

    # Top performing Spurs players
    player_stats = content.get("playerStats", {})
    print("\n  Spurs Starting XI & Ratings:")
    for p in spurs.get("starters", []):
        raw_name = p.get("name")
        name = raw_name if isinstance(raw_name, str) else raw_name.get("fullName", "")
        pid = str(p.get("id"))
        ps = player_stats.get(pid, {})
        rating = "-"
        for grp in ps.get("stats", []):
            if "FotMob rating" in grp.get("stats", {}):
                rating = grp.get("stats", {})["FotMob rating"].get("stat", {}).get("value", "-")
                break
        pos = p.get("positionStringShort", "")
        print(f"    {pos:4s} {name:22s} | Rating: {str(rating):5s}")
