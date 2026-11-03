import json
from pathlib import Path

def print_hdr(title):
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)

# ----------------------------------------------------
# 2. CHELSEA vs CHARLTON & ALYSSA THOMPSON
# ----------------------------------------------------
print_hdr("2. CHELSEA vs CHARLTON & THOMPSON / MALARD")
with open("scratch_cha_che.json", "r", encoding="utf-8") as f:
    cha_che = json.load(f)

# Chelsea team stats
top_stats = cha_che.get("content", {}).get("stats", {}).get("Periods", {}).get("All", {}).get("stats", [])
for sec in top_stats:
    for s in sec.get("stats", []):
        if s.get("key") in ["expected_goals", "total_shots", "shots_on_target", "big_chance", "touches_opp_box"]:
            print(f"  {s.get('title')}: CHA {s.get('stats')[0]} | CHE {s.get('stats')[1]}")

print("\nChelsea Goals:")
for e in cha_che.get("content", {}).get("matchFacts", {}).get("events", {}).get("events", []):
    if e.get("type") == "Goal":
        print(f"  {e.get('timeStr')}' {e.get('player', {}).get('name')} (assist: {e.get('assistStr')})")

print("\nChelsea Starters & Subs:")
lineup_che = cha_che.get("content", {}).get("lineup", {}).get("awayTeam", {})
starters_che = lineup_che.get("starters", [])
subs_che = lineup_che.get("subs", [])
for p in starters_che:
    print(f"  Starter: {p.get('name')} ({p.get('positionStringShort')})")
for p in subs_che:
    print(f"  Sub: {p.get('name')}")

# Check Malard stats
shots_che = cha_che.get("content", {}).get("shotmap", {}).get("shots", [])
malard_shots = [s for s in shots_che if "Malard" in str(s.get("playerName"))]
print(f"\nMalard shots ({len(malard_shots)}): total xG = {sum(s.get('expectedGoals', 0) for s in malard_shots):.2f}")
for s in malard_shots:
    print(f"  min {s.get('min')}, xG {s.get('expectedGoals'):.3f}, result: {s.get('eventType')}")

# Check Alyssa Thompson in previous matches / season data
print("\nAlyssa Thompson in dataset:")
all_matches = Path("data/raw/fotmob/matches")
thompson_appearances = []
for p in sorted(all_matches.glob("*.json")):
    try:
        d = json.load(open(p, "r", encoding="utf-8"))
        for side in ["homeTeam", "awayTeam"]:
            t = d.get("content", {}).get("lineup", {}).get(side, {})
            all_p = t.get("starters", []) + t.get("subs", [])
            for pl in all_p:
                if "Thompson" in pl.get("name", ""):
                    mtitle = f"{d.get('general', {}).get('homeTeam', {}).get('name')} vs {d.get('general', {}).get('awayTeam', {}).get('name')}"
                    round_str = d.get('general', {}).get('matchTimeUTC', '')[:10]
                    # check if started or subbed
                    is_starter = pl in t.get("starters", [])
                    rating = pl.get("rating", {}).get("num")
                    thompson_appearances.append((p.name, mtitle, round_str, is_starter, rating))
    except Exception:
        pass
for app in thompson_appearances:
    print(f"  {app[0]}: {app[1]} ({app[2]}) | Starter: {app[3]}, Rating: {app[4]}")

# ----------------------------------------------------
# 3. ARSENAL vs ASTON VILLA
# ----------------------------------------------------
print_hdr("3. ARSENAL vs ASTON VILLA")
with open("scratch_ars_avl.json", "r", encoding="utf-8") as f:
    ars_avl = json.load(f)

for sec in ars_avl.get("content", {}).get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
    for s in sec.get("stats", []):
        if s.get("key") in ["expected_goals", "total_shots", "shots_on_target", "big_chance", "touches_opp_box", "possession"]:
            print(f"  {s.get('title')}: ARS {s.get('stats')[0]} | AVL {s.get('stats')[1]}")

print("\nGoals:")
for e in ars_avl.get("content", {}).get("matchFacts", {}).get("events", {}).get("events", []):
    if e.get("type") == "Goal":
        print(f"  {e.get('timeStr')}' {e.get('player', {}).get('name')} (assist: {e.get('assistStr')})")

print("\nArsenal Lineup:")
ars_lineup = ars_avl.get("content", {}).get("lineup", {}).get("homeTeam", {})
print("  Starters:", [p.get("name") for p in ars_lineup.get("starters", [])])
print("  Subs:", [p.get("name") for p in ars_lineup.get("subs", [])])

# Villa shotmap
print("\nVilla Shots:")
for s in ars_avl.get("content", {}).get("shotmap", {}).get("shots", []):
    if s.get("teamId") == 231494: # Villa
        print(f"  {s.get('min')}' {s.get('playerName')}: xG {s.get('expectedGoals'):.3f}, result: {s.get('eventType')}")

# ----------------------------------------------------
# 4. BIRMINGHAM vs TOTTENHAM
# ----------------------------------------------------
print_hdr("4. BIRMINGHAM vs TOTTENHAM")
with open("scratch_bir_tot.json", "r", encoding="utf-8") as f:
    bir_tot = json.load(f)

print("\nSpurs Goals:")
for e in bir_tot.get("content", {}).get("matchFacts", {}).get("events", {}).get("events", []):
    if e.get("type") == "Goal":
        print(f"  {e.get('timeStr')}' {e.get('player', {}).get('name')} (assist: {e.get('assistStr')})")

print("\nSpurs Shotmap (Holdt, Gaupset, etc.):")
for s in bir_tot.get("content", {}).get("shotmap", {}).get("shots", []):
    if s.get("teamId") == 628117: # Spurs
        if s.get("eventType") == "Goal" or any(n in str(s.get("playerName")) for n in ["Holdt", "Gaupset", "Vinberg", "Pelova", "Blakstad"]):
            print(f"  {s.get('min')}' {s.get('playerName')}: xG {s.get('expectedGoals'):.3f}, xGOT {s.get('expectedGoalsOnTarget')}, result: {s.get('eventType')}")

# ----------------------------------------------------
# 5. WEST HAM vs LIVERPOOL & HISTORICAL 4-1 vs LCL
# ----------------------------------------------------
print_hdr("5. WEST HAM vs LIVERPOOL & HISTORICAL MATCHES")
with open("scratch_whu_liv.json", "r", encoding="utf-8") as f:
    whu_liv = json.load(f)

for sec in whu_liv.get("content", {}).get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
    for s in sec.get("stats", []):
        if s.get("key") in ["expected_goals", "total_shots", "shots_on_target", "big_chance", "possession", "accurate_passes"]:
            print(f"  {s.get('title')}: WHU {s.get('stats')[0]} | LIV {s.get('stats')[1]}")

print("\nGoals in WHU vs LIV:")
for e in whu_liv.get("content", {}).get("matchFacts", {}).get("events", {}).get("events", []):
    if e.get("type") == "Goal":
        print(f"  {e.get('timeStr')}' {e.get('player', {}).get('name')} (assist: {e.get('assistStr')})")

# Look for MW2 WHU vs LCL
p_whu_lcl = Path("data/raw/fotmob/matches/mw2_whu_lcl_5981634.json")
if p_whu_lcl.exists():
    d_whu_lcl = json.load(open(p_whu_lcl, "r", encoding="utf-8"))
    print("\nWHU vs LCL (MW2):")
    h = d_whu_lcl.get('header', {}).get('teams', [])
    print(f"  Score: {h[0].get('name')} {h[0].get('score')} - {h[1].get('score')} {h[1].get('name')}")
    for sec in d_whu_lcl.get("content", {}).get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
        for s in sec.get("stats", []):
            if s.get("key") in ["expected_goals", "total_shots", "shots_on_target", "big_chance", "possession"]:
                print(f"    {s.get('title')}: {s.get('stats')}")

# ----------------------------------------------------
# 6. EVERTON vs MAN UNITED
# ----------------------------------------------------
print_hdr("6. EVERTON vs MAN UNITED")
with open("scratch_eve_mun.json", "r", encoding="utf-8") as f:
    eve_mun = json.load(f)

for sec in eve_mun.get("content", {}).get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
    for s in sec.get("stats", []):
        if s.get("key") in ["expected_goals", "total_shots", "shots_on_target", "big_chance", "possession", "accurate_passes"]:
            print(f"  {s.get('title')}: EVE {s.get('stats')[0]} | MUN {s.get('stats')[1]}")

