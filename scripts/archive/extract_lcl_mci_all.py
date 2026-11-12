import json
from pathlib import Path

def print_hdr(title):
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)

# ==========================================
# 1. LONDON CITY LIONESSES vs MANCHESTER CITY
# ==========================================
print_hdr("1. LONDON CITY LIONESSES vs MANCHESTER CITY (DEEP EXTRACTION)")
with open("scratch_lcl_mci.json", "r", encoding="utf-8") as f:
    lcl_mci = json.load(f)

# Team stats
print("\n--- TEAM STATS ---")
periods = lcl_mci.get("content", {}).get("stats", {}).get("Periods", {}).get("All", {}).get("stats", [])
for sec in periods:
    print(f"\n[{sec.get('title')}]")
    for s in sec.get("stats", []):
        print(f"  {s.get('title')}: LCL {s.get('stats', [None, None])[0]} | MCI {s.get('stats', [None, None])[1]}")

# Shotmap
print("\n--- SHOTMAP ---")
shots = lcl_mci.get("content", {}).get("shotmap", {}).get("shots", [])
for s in shots:
    pname = s.get("playerName")
    min_ = s.get("min")
    xg = round(s.get("expectedGoals", 0), 3)
    xgot = round(s.get("expectedGoalsOnTarget") or 0, 3)
    ev = s.get("eventType")
    team = "LCL" if s.get("teamId") == 1075419 else "MCI"
    print(f"  [{team}] {min_}' {pname}: xG {xg}, xGOT {xgot}, Result: {ev}")

# Goals & Key Sequences
print("\n--- GOAL EVENTS ---")
events = lcl_mci.get("content", {}).get("matchFacts", {}).get("events", {}).get("events", [])
for e in events:
    if e.get("type") == "Goal":
        print(f"  Goal at {e.get('timeStr')}': {e.get('player', {}).get('name')} (Assist: {e.get('assistStr')}) | Team: {e.get('team')}")

# Player Deep Dives: Fowler, Clinton, Shaw, Hemp, Earps, Knaak, Jana Fernandez
print("\n--- KEY PLAYERS IN LCL vs MCI ---")
lineup = lcl_mci.get("content", {}).get("lineup", {})
for side in ["homeTeam", "awayTeam"]:
    tname = "LCL" if side == "homeTeam" else "MCI"
    starters = lineup.get(side, {}).get("starters", [])
    subs = lineup.get(side, {}).get("subs", [])
    for p in starters + subs:
        name = p.get("name", "")
        # Check interesting players
        if any(target in name for target in ["Fowler", "Clinton", "Shaw", "Hemp", "Earps", "Knaak", "Fernández", "Zelem", "Asllani", "Diani"]):
            rating = p.get("rating", {}).get("num")
            pos = p.get("positionStringShort")
            print(f"\n  [{tname}] {name} (Pos: {pos}, Rating: {rating}):")
            for grp in p.get("stats", []):
                g_title = grp.get("title")
                stat_items = grp.get("stats", {})
                row = []
                for k, v in stat_items.items():
                    val = v.get("stat", {}).get("value") if isinstance(v, dict) else v
                    row.append(f"{k}: {val}")
                if row:
                    print(f"    {g_title}: {', '.join(row)}")

