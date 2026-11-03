import json
from pathlib import Path

arsenal_matches = [
    ("MW1", "Brighton 0-1 Arsenal", "data/raw/fotmob/matches/mw1_bha_ars_5981533.json"),
    ("MW2", "Arsenal 0-0 Palace", "data/raw/fotmob/matches/mw2_cry_ars_5981639.json"),
    ("MW3", "Arsenal 1-1 Man United", "data/raw/fotmob/matches/mw3_mun_ars_5981644.json"),
    ("MW4", "Chelsea 1-0 Arsenal", "data/raw/fotmob/matches/mw4_che_ars_5981654.json"),
    ("MW5", "Man City 4-2 Arsenal", "data/raw/fotmob/matches/mw5_mci_ars_5981661.json"),
    ("MW6", "Arsenal 1-1 Birmingham", "data/raw/fotmob/matches/mw6_ars_bir_5981663.json"),
    ("MW7", "Spurs 1-2 Arsenal", "data/raw/fotmob/matches/mw7_tot_ars_5981675.json"),
    ("MW8", "Arsenal 1-1 Aston Villa", "data/raw/fotmob/matches/mw8_ars_avl_5981677.json"),
]

lineups_history = []
player_starts_count = {}
position_history = {
    "GK": [],
    "RB": [],
    "CB1": [],
    "CB2": [],
    "LB": [],
    "DM1": [],
    "DM2": [],
    "AM": [],
    "RW": [],
    "LW": [],
    "CF": []
}

for mw, title, fpath in arsenal_matches:
    with open(fpath, "r", encoding="utf-8") as f:
        d = json.load(f)
    home = d.get("general", {}).get("homeTeam", {}).get("name")
    ars_side = "homeTeam" if "Arsenal" in home else "awayTeam"
    
    lineup_data = d.get("content", {}).get("lineup", {}).get(ars_side, {})
    formation = lineup_data.get("formation", "Unknown")
    starters = lineup_data.get("starters", [])
    
    starter_names = [p.get("name") for p in starters]
    for s in starter_names:
        player_starts_count[s] = player_starts_count.get(s, 0) + 1
        
    lineups_history.append({
        "mw": mw,
        "title": title,
        "formation": formation,
        "starters": starter_names
    })

print("=" * 90)
print(" ⚽ ARSENAL MATCH-BY-MATCH STARTING XI (MW1 to MW8)")
print("=" * 90)
for lh in lineups_history:
    print(f"\n📌 {lh['mw']} ({lh['title']}) | Formation: {lh['formation']}")
    print("   " + ", ".join(lh['starters']))

print("\n" + "=" * 90)
print(" 📊 TOTAL STARTS PER PLAYER (OUT OF 8 MATCHES)")
print("=" * 90)
sorted_counts = sorted(player_starts_count.items(), key=lambda x: x[1], reverse=True)
for p, c in sorted_counts:
    pct = round(c / 8 * 100)
    print(f"   {p:<26}: {c}/8 starts ({pct}%)")

# Detailed position breakdown if available in lineup structure
print("\n" + "=" * 90)
print(" 🔍 LINEUP POSITIONS EXTRACTED FROM MATCH DATA")
print("=" * 90)
for mw, title, fpath in arsenal_matches:
    with open(fpath, "r", encoding="utf-8") as f:
        d = json.load(f)
    home = d.get("general", {}).get("homeTeam", {}).get("name")
    ars_side = "homeTeam" if "Arsenal" in home else "awayTeam"
    lineup_data = d.get("content", {}).get("lineup", {}).get(ars_side, {})
    
    print(f"\n{mw}: {title}")
    # inspect lineup structure
    lineup_grid = lineup_data.get("lineup", [])
    if lineup_grid:
        for row_idx, row in enumerate(lineup_grid):
            p_names = [p.get("name") for p in row]
            print(f"   Line {row_idx+1}: {', '.join(p_names)}")
    else:
        # Check starters list order
        starters = lineup_data.get("starters", [])
        print("   Starters order:", [f"{p.get('name')} ({p.get('positionStringShort', '')})" for p in starters])

