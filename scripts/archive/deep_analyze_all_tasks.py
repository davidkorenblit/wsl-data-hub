import json
import glob
from pathlib import Path

print("=" * 70)
print("COMPREHENSIVE MATCHWEEK 9 DEEP ANALYSIS")
print("=" * 70)

# -------------------------------------------------------------
# TASK 1: BUNNY SHAW & CITY VS WEST HAM
# -------------------------------------------------------------
print("\n--- TASK 1: Bunny Shaw & City vs West Ham ---")
with open("data/raw/fotmob/leagues/league_9227_wsl_overview.json", "r", encoding="utf-8") as f:
    overview = json.load(f)

# Top scorers from overview
players_stats = overview.get("stats", {}).get("players", [])
for pcat in players_stats:
    header = pcat.get("header")
    if header in ["Top scorer", "Assists", "Goals + Assists"]:
        print(f"\n{header}:")
        for top in pcat.get("topThree", []):
            print(f"  {top.get('name')}: {top.get('value')}")

# City vs West Ham stats
with open("data/raw/fotmob/matches/mw9_mci_whu_5981687.json", "r", encoding="utf-8") as f:
    mci_whu = json.load(fp=f)

pstats = mci_whu.get("content", {}).get("playerStats", {})
print("\nCity Midfield & Attack vs West Ham:")
for pid, pdata in pstats.items():
    name = pdata.get("name", "")
    if any(k in name for k in ["Shaw", "Fujino", "Hasegawa", "Fowler", "Asseyi", "Gago"]):
        sd = {}
        for sec in pdata.get("stats", []):
            for sname, sinfo in sec.get("stats", {}).items():
                sd[sinfo.get("key", sname)] = sinfo.get("stat", {}).get("value", 0)
        print(f"  {name:<18} | Min: {sd.get('minutes_played', 0):<2} | Touches: {sd.get('touches', 0):<2} | BoxT: {sd.get('touches_opp_box', 0):<2} | Shots: {sd.get('total_shots', 0):<2} | Goals: {sd.get('goals', 0):<2} | Tack+Rec: {sd.get('tackles', 0)}+{sd.get('recoveries', 0)}")

# -------------------------------------------------------------
# TASK 2: ARSENAL (LIVERPOOL 1 - 2 ARSENAL)
# -------------------------------------------------------------
print("\n--- TASK 2: Arsenal vs Liverpool & Conceded Goals ---")
with open("data/raw/fotmob/matches/mw9_liv_ars_5981683.json", "r", encoding="utf-8") as f:
    liv_ars = json.load(fp=f)

events = liv_ars.get("content", {}).get("matchFacts", {}).get("events", {}).get("events", [])
for e in events:
    if e.get("type") == "Goal":
        print(f"  Goal: {e.get('player', {}).get('name')} {e.get('time')}' (Assist: {e.get('assist', {}).get('name')})")

pstats_ars = liv_ars.get("content", {}).get("playerStats", {})
print("\nArsenal Key Attackers vs Liverpool:")
for pid, pdata in pstats_ars.items():
    name = pdata.get("name", "")
    if any(k in name for k in ["Russo", "Fox", "Baum", "Williamson", "Catley", "Little"]):
        sd = {}
        for sec in pdata.get("stats", []):
            for sname, sinfo in sec.get("stats", {}).items():
                sd[sinfo.get("key", sname)] = sinfo.get("stat", {}).get("value", 0)
        print(f"  {name:<18} | Min: {sd.get('minutes_played', 0):<2} | Touches: {sd.get('touches', 0):<2} | BoxT: {sd.get('touches_opp_box', 0):<2} | Shots: {sd.get('total_shots', 0):<2} | xG: {sd.get('expected_goals', 0.0):<4} | Crosses: {sd.get('accurate_crosses', 0)}")

# -------------------------------------------------------------
# TASK 3: CHELSEA 1 - 1 EVERTON
# -------------------------------------------------------------
print("\n--- TASK 3: Chelsea 1 - 1 Everton & Everton Anomaly ---")
with open("data/raw/fotmob/matches/mw9_che_eve_5981686.json", "r", encoding="utf-8") as f:
    che_eve = json.load(fp=f)

eve_events = che_eve.get("content", {}).get("matchFacts", {}).get("events", {}).get("events", [])
for e in eve_events:
    if e.get("type") == "Goal":
        print(f"  Goal: {e.get('player', {}).get('name')} {e.get('time')}' ({e.get('goalType', 'regular')})")

for sec in che_eve.get("content", {}).get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
    for s in sec.get("stats", []):
        if s.get("title") in ["Expected goals (xG)", "Total shots", "Shots on target", "Big chances", "Ball possession"]:
            print(f"  {s.get('title')}: {s.get('stats')}")

# Check Everton's total goals and season record from league table
with open("_data/league_table.json", "r", encoding="utf-8") as f:
    lt = json.load(f)
for row in lt:
    if row.get("slug") == "everton" or "Everton" in row.get("squad", ""):
        print(f"\nEverton Standings: MP: {row.get('mp')}, W: {row.get('w')}, D: {row.get('d')}, L: {row.get('l')}, GF: {row.get('gf')}, GA: {row.get('ga')}, PTS: {row.get('pts')}")

# -------------------------------------------------------------
# TASK 4: SPURS (VIC PELOVA) VS BRIGHTON
# -------------------------------------------------------------
print("\n--- TASK 4: Tottenham vs Brighton & Vic Pelova ---")
with open("data/raw/fotmob/matches/mw9_tot_bha_5981689.json", "r", encoding="utf-8") as f:
    tot_bha = json.load(fp=f)

pstats_tot = tot_bha.get("content", {}).get("playerStats", {})
for pid, pdata in pstats_tot.items():
    name = pdata.get("name", "")
    if any(k in name for k in ["Pelova", "Gaupset", "Holdt", "Hanson", "Tandberg"]):
        sd = {}
        for sec in pdata.get("stats", []):
            for sname, sinfo in sec.get("stats", {}).items():
                sd[sinfo.get("key", sname)] = sinfo.get("stat", {}).get("value", 0)
        print(f"  {name:<18} | Min: {sd.get('minutes_played', 0):<2} | Touches: {sd.get('touches', 0):<2} | Passes: {sd.get('accurate_passes', 0)} | ChancesCreated: {sd.get('chances_created', 0)} | Dispossessed: {sd.get('dispossessed', 0)} | Tack+Rec: {sd.get('tackles', 0)}+{sd.get('recoveries', 0)}")

# -------------------------------------------------------------
# TASK 5: LONDON CITY LIONESSES & POPPY PATTINSON
# -------------------------------------------------------------
print("\n--- TASK 5: London City Lionesses vs Birmingham & Poppy Pattinson ---")
with open("data/raw/fotmob/matches/mw9_lcl_bir_5981684.json", "r", encoding="utf-8") as f:
    lcl_bir = json.load(fp=f)

pstats_lcl = lcl_bir.get("content", {}).get("playerStats", {})
for pid, pdata in pstats_lcl.items():
    name = pdata.get("name", "")
    if any(k in name for k in ["Pattinson", "Cascarino", "Geyoro", "Diani", "Lohmann", "Bartel"]):
        sd = {}
        for sec in pdata.get("stats", []):
            for sname, sinfo in sec.get("stats", {}).items():
                sd[sinfo.get("key", sname)] = sinfo.get("stat", {}).get("value", 0)
        print(f"  {name:<18} | Min: {sd.get('minutes_played', 0):<2} | Goals: {sd.get('goals', 0)} | Assists: {sd.get('assists', 0)} | Touches: {sd.get('touches', 0):<2} | BoxT: {sd.get('touches_opp_box', 0):<2} | ChancesCreated: {sd.get('chances_created', 0)} | Tack+Rec: {sd.get('tackles', 0)}+{sd.get('recoveries', 0)}")

# -------------------------------------------------------------
# TASK 6: CRYSTAL PALACE 3 - 2 CHARLTON & BETH ENGLAND
# -------------------------------------------------------------
print("\n--- TASK 6: Crystal Palace 3 - 2 Charlton & Beth England ---")
with open("data/raw/fotmob/matches/mw9_cry_cha_5981688.json", "r", encoding="utf-8") as f:
    cry_cha = json.load(fp=f)

pstats_pal = cry_cha.get("content", {}).get("playerStats", {})
for pid, pdata in pstats_pal.items():
    name = pdata.get("name", "")
    if any(k in name for k in ["England", "Lloyd-Smith", "Blanchard", "Hopcroft", "Everett"]):
        sd = {}
        for sec in pdata.get("stats", []):
            for sname, sinfo in sec.get("stats", {}).items():
                sd[sinfo.get("key", sname)] = sinfo.get("stat", {}).get("value", 0)
        print(f"  {name:<18} | Min: {sd.get('minutes_played', 0):<2} | Goals: {sd.get('goals', 0)} | Shots: {sd.get('total_shots', 0):<2} | xG: {sd.get('expected_goals', 0.0):<4} | BoxT: {sd.get('touches_opp_box', 0):<2} | Tack+Rec: {sd.get('tackles', 0)}+{sd.get('recoveries', 0)}")
