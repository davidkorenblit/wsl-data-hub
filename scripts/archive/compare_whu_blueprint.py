import json

# MW2 WHU vs LCL
with open("data/raw/fotmob/matches/mw2_whu_lcl_5981634.json", "r", encoding="utf-8") as f:
    d2 = json.load(f)

# MW8 WHU vs LIV
with open("scratch_whu_liv.json", "r", encoding="utf-8") as f:
    d8 = json.load(f)

def extract_match_overview(d, opponent_name):
    # Determine side
    home_name = d.get("general", {}).get("homeTeam", {}).get("name")
    whu_side = "homeTeam" if "West Ham" in home_name else "awayTeam"
    opp_side = "awayTeam" if whu_side == "homeTeam" else "homeTeam"
    
    score = f"{d.get('header', {}).get('teams', [{}])[0].get('score')} - {d.get('header', {}).get('teams', [{}])[1].get('score')}"
    
    # Team stats map
    stats_map = {}
    for sec in d.get("content", {}).get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
        for s in sec.get("stats", []):
            k = s.get("title") or s.get("key")
            st = s.get("stats", [None, None])
            whu_idx = 0 if whu_side == "homeTeam" else 1
            opp_idx = 1 if whu_side == "homeTeam" else 0
            stats_map[k] = (st[whu_idx], st[opp_idx])
            
    # Goals
    goals = []
    events = d.get("content", {}).get("matchFacts", {}).get("events", {}).get("events", [])
    for e in events:
        if e.get("type") == "Goal":
            goals.append({
                "min": e.get("timeStr"),
                "player": e.get("player", {}).get("name"),
                "assist": e.get("assistStr"),
                "team": "WHU" if e.get("isHome") == (whu_side == "homeTeam") else opponent_name
            })
            
    return score, stats_map, goals

s2, stats2, goals2 = extract_match_overview(d2, "LCL")
s8, stats8, goals8 = extract_match_overview(d8, "LIV")

print("=== WEST HAM: MW2 (vs LCL) vs MW8 (vs LIVERPOOL) ===")
print(f"Scores: MW2: {s2} vs LCL | MW8: {s8} vs Liverpool\n")

keys = [
    "Expected goals (xG)",
    "xG open play",
    "xG on target (xGOT)",
    "Total shots",
    "Shots on target",
    "Shots inside box",
    "Big chances",
    "Big chances missed",
    "Ball possession",
    "Passes",
    "Accurate passes",
    "Own half",
    "Opposition half",
    "Accurate long balls",
    "Tackles",
    "Interceptions",
    "Clearances",
    "Duels won",
    "Successful dribbles"
]

print(f"{'Metric':<26} {'MW2 vs LCL (WHU / Opp)':<25} {'MW8 vs LIV (WHU / Opp)':<25}")
print("-" * 78)
for k in keys:
    v2 = f"{stats2.get(k, ('-','-'))[0]} / {stats2.get(k, ('-','-'))[1]}"
    v8 = f"{stats8.get(k, ('-','-'))[0]} / {stats8.get(k, ('-','-'))[1]}"
    print(f"{k:<26} {v2:<25} {v8:<25}")

print("\nMW2 Goals vs LCL:")
for g in goals2:
    print(f"  {g['min']}' {g['player']} ({g['team']}) - assist: {g['assist']}")

print("\nMW8 Goals vs LIV:")
for g in goals8:
    print(f"  {g['min']}' {g['player']} ({g['team']}) - assist: {g['assist']}")

