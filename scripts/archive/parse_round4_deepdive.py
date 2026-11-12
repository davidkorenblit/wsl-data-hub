import json

def load(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def get_player_stats_flat(pdata):
    res = {}
    for cat in pdata.get("stats", []):
        cat_stats = cat.get("stats", {})
        if isinstance(cat_stats, dict):
            for k, v in cat_stats.items():
                stat_obj = v.get("stat", {})
                val = stat_obj.get("value")
                total = stat_obj.get("total")
                if total is not None:
                    res[k] = f"{val}/{total}"
                else:
                    res[k] = val
    return res

che_ars = load("scratch_che_ars.json")
tot_avl = load("scratch_tot_avl.json")
lcl_bha = load("scratch_lcl_bha.json")
mun_whu = load("scratch_mun_whu.json")
bir_cry = load("scratch_bir_cry.json")

print("="*60)
print("1. CHELSEA VS ARSENAL (1 - 0)")
print("="*60)
content_ca = che_ars.get("content", {})
# Goal details
for ev in content_ca.get("matchFacts", {}).get("events", {}).get("events", []):
    if ev.get("type") == "Goal":
        print(f"GOAL: Min {ev.get('time')}, Scorer: {ev.get('player', {}).get('name')}, Assist: {ev.get('assist', {}).get('name')}")

# Team Defence / Attack
print("\n--- Team Stats (Chelsea / Arsenal) ---")
for grp in content_ca.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
    for s in grp.get("stats", []):
        key = s.get("title") or s.get("key")
        if any(w in str(key).lower() for w in ["shot", "xg", "clearance", "recovery", "tackle", "interception", "possession", "duel"]):
            print(f"  {key}: {s.get('stats')}")

# Player Stats
pstats_ca = content_ca.get("playerStats", {})
target_players = ["Russo", "Buchanan", "Bronze", "McCabe", "Baum", "Kelly", "Thompson"]
for pid, pdata in pstats_ca.items():
    name = pdata.get("name", "")
    for tp in target_players:
        if tp.lower() in name.lower():
            flat = get_player_stats_flat(pdata)
            print(f"\n--- Player: {name} ---")
            interesting_keys = [
                "Minutes played", "FotMob rating", "Goals", "Assists", "Total shots", "Shots on target", "Blocked shots",
                "Touches", "Touches in opposition box", "Accurate passes", "Chances created", "Expected goals (xG)",
                "Tackles won", "Defensive actions", "Clearances", "Interceptions", "Recoveries", 
                "Dribbles", "Successful dribbles", "Dribbled past",
                "Ground duels won", "Aerial duels won", "Was fouled", "Fouls committed", "Yellow cards"
            ]
            for ik in interesting_keys:
                if ik in flat:
                    print(f"  {ik}: {flat[ik]}")

print("\n" + "="*60)
print("2. TOTTENHAM VS ASTON VILLA: TOKO KOGA")
print("="*60)
content_ta = tot_avl.get("content", {})
pstats_ta = content_ta.get("playerStats", {})
for pid, pdata in pstats_ta.items():
    name = pdata.get("name", "")
    if "koga" in name.lower():
        flat = get_player_stats_flat(pdata)
        print(f"\n--- Player: {name} ---")
        for k, v in flat.items():
            print(f"  {k}: {v}")

print("\n" + "="*60)
print("3. LONDON CITY LIONESSES VS BRIGHTON")
print("="*60)
content_lb = lcl_bha.get("content", {})
for ev in content_lb.get("matchFacts", {}).get("events", {}).get("events", []):
    if ev.get("type") == "Goal":
        print(f"GOAL: Min {ev.get('time')}, Scorer: {ev.get('player', {}).get('name')}, Assist: {ev.get('assist', {}).get('name')}")

print("\nLCL Starting Lineup & Positions:")
for team in content_lb.get("lineup", {}).get("lineup", []):
    if "london city" in team.get("teamName", "").lower():
        for p in team.get("players", []):
            print(f"  {p.get('name', {}).get('fullName')} - {p.get('role')} / {p.get('position')}")

print("\nLCL vs Brighton Team Stats (LCL / Brighton):")
for grp in content_lb.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
    for s in grp.get("stats", []):
        key = s.get("title") or s.get("key")
        if any(w in str(key).lower() for w in ["shot", "xg", "possession", "chance", "clearance"]):
            print(f"  {key}: {s.get('stats')}")

pstats_lb = content_lb.get("playerStats", {})
for pid, pdata in pstats_lb.items():
    name = pdata.get("name", "")
    if "putellas" in name.lower() or "león" in name.lower() or "leon" in name.lower():
        flat = get_player_stats_flat(pdata)
        print(f"\n--- Player: {name} ---")
        for k in ["Minutes played", "FotMob rating", "Goals", "Assists", "Total shots", "Shots on target", "Touches", "Accurate passes", "Chances created", "Expected goals (xG)", "Tackles won", "Clearances", "Interceptions", "Recoveries"]:
            if k in flat:
                print(f"  {k}: {flat[k]}")

print("\n" + "="*60)
print("4. MANCHESTER UNITED LINEUP & 'MEDINA'")
print("="*60)
content_mw = mun_whu.get("content", {})
for team in content_mw.get("lineup", {}).get("lineup", []):
    if "united" in team.get("teamName", "").lower():
        print("United Starting 11:")
        for p in team.get("players", []):
            print(f"  {p.get('name', {}).get('fullName')} (Shirt: {p.get('shirtNumber')}) - {p.get('role')} / {p.get('position')}")
        print("United Bench:")
        for p in team.get("bench", []):
            print(f"  {p.get('name', {}).get('fullName')} (Shirt: {p.get('shirtNumber')})")

print("\n" + "="*60)
print("5. BIRMINGHAM CITY VS CRYSTAL PALACE (3 - 3)")
print("="*60)
content_bc = bir_cry.get("content", {})
for ev in content_bc.get("matchFacts", {}).get("events", {}).get("events", []):
    if ev.get("type") == "Goal":
        print(f"GOAL: Min {ev.get('time')}, Scorer: {ev.get('player', {}).get('name')}, Assist: {ev.get('assist', {}).get('name')}")
for grp in content_bc.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
    for s in grp.get("stats", []):
        key = s.get("title") or s.get("key")
        if any(w in str(key).lower() for w in ["shot", "xg", "chance", "error"]):
            print(f"  {key}: {s.get('stats')}")
