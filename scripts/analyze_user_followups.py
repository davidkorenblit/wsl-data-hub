import json
import glob
from pathlib import Path

print("=" * 70)
print("1. ARSENAL DEFENDERS GROUND DUELS & 1v1 STATS (MW1 - MW9)")
print("=" * 70)

ars_matches = sorted(glob.glob("data/raw/fotmob/matches/*ars*.json"))
def_stats = {"Leah Williamson": [], "Steph Catley": [], "Lotte Wubben-Moy": []}

for f in ars_matches:
    with open(f, "r", encoding="utf-8") as fp:
        d = json.load(fp)
    pstats = d.get("content", {}).get("playerStats", {})
    gen = d.get("general", {})
    mname = f"{gen.get('homeTeam', {}).get('name')} vs {gen.get('awayTeam', {}).get('name')}"
    
    for pid, pdata in pstats.items():
        name = pdata.get("name", "")
        for target in def_stats.keys():
            if target in name:
                sd = {}
                for sec in pdata.get("stats", []):
                    for sname, sinfo in sec.get("stats", {}).items():
                        sd[sinfo.get("key", sname)] = sinfo.get("stat", {}).get("value", 0)
                mins = sd.get("minutes_played", 0)
                if mins > 20:
                    g_won = sd.get("ground_duels_won", 0)
                    g_total = sd.get("ground_duels", sd.get("ground_duels_won", 0) + sd.get("ground_duels_lost", 0))
                    tack_won = sd.get("tackles_won", 0)
                    tack_total = sd.get("tackles", 0)
                    dribbled_past = sd.get("dribbled_past", 0)
                    def_stats[target].append({
                        "match": mname,
                        "mins": mins,
                        "ground_won": g_won,
                        "ground_total": g_total,
                        "tackles": tack_total,
                        "tackles_won": tack_won,
                        "dribbled_past": dribbled_past,
                        "recoveries": sd.get("recoveries", 0),
                        "interceptions": sd.get("interceptions", 0)
                    })

for player, records in def_stats.items():
    print(f"\n--- {player} ---")
    tot_mins = sum(r['mins'] for r in records)
    tot_g_won = sum(r['ground_won'] for r in records)
    tot_g_tot = sum(r['ground_total'] for r in records)
    tot_dr_past = sum(r['dribbled_past'] for r in records)
    tot_tack = sum(r['tackles'] for r in records)
    tot_tack_won = sum(r['tackles_won'] for r in records)
    tot_rec = sum(r['recoveries'] for r in records)
    pct = (tot_g_won / tot_g_tot * 100) if tot_g_tot > 0 else 0
    tack_pct = (tot_tack_won / tot_tack * 100) if tot_tack > 0 else 0
    print(f"Total Matches: {len(records)} | Total Mins: {tot_mins}")
    print(f"Ground Duels: {tot_g_won}/{tot_g_tot} ({pct:.1f}%) | Dribbled Past: {tot_dr_past}")
    print(f"Tackles: {tot_tack_won}/{tot_tack} ({tack_pct:.1f}%) | Recoveries: {tot_rec}")
    for r in records[-4:]:
        print(f"  {r['match']:<35} | Mins: {r['mins']:<2} | Ground: {r['ground_won']}/{r['ground_total']} | DrPast: {r['dribbled_past']} | Rec: {r['recoveries']}")

# =====================================================================
# 2. WEST HAM VS LCL (LONDON CITY LIONESSES) - ASSEYI & ZELEM
# =====================================================================
print("\n" + "=" * 70)
print("2. WEST HAM VS LONDON CITY LIONESSES (MW2)")
print("=" * 70)
with open("data/raw/fotmob/matches/mw2_whu_lcl_5981634.json", "r", encoding="utf-8") as fp:
    whu_lcl = json.load(fp)

whu_lcl_pstats = whu_lcl.get("content", {}).get("playerStats", {})
for pid, pdata in whu_lcl_pstats.items():
    name = pdata.get("name", "")
    if any(k in name for k in ["Asseyi", "Zelem", "Gago", "Piubel"]):
        sd = {}
        for sec in pdata.get("stats", []):
            for sname, sinfo in sec.get("stats", {}).items():
                sd[sinfo.get("key", sname)] = sinfo.get("stat", {}).get("value", 0)
        print(f"  {name:<18} | Mins: {sd.get('minutes_played', 0):<2} | Touches: {sd.get('touches', 0):<2} | Passes: {sd.get('accurate_passes', 0)}/{sd.get('total_passes', 0)} | Final3rdPasses: {sd.get('passes_into_final_third', 0)} | BoxT: {sd.get('touches_opp_box', 0):<2} | Shots: {sd.get('total_shots', 0)}")

# =====================================================================
# 3. VIC PELOVA ACROSS BIG MATCHES VS SMALL MATCHES
# =====================================================================
print("\n" + "=" * 70)
print("3. VIC PELOVA: BIG MATCHES (Chelsea, Arsenal, LCL, Brighton) VS SMALL MATCHES")
print("=" * 70)

tot_matches = sorted(glob.glob("data/raw/fotmob/matches/*tot*.json"))
for f in tot_matches:
    with open(f, "r", encoding="utf-8") as fp:
        d = json.load(fp)
    gen = d.get("general", {})
    mname = f"{gen.get('homeTeam', {}).get('name')} vs {gen.get('awayTeam', {}).get('name')}"
    pstats = d.get("content", {}).get("playerStats", {})
    for pid, pdata in pstats.items():
        if "Pelova" in pdata.get("name", ""):
            sd = {}
            for sec in pdata.get("stats", []):
                for sname, sinfo in sec.get("stats", {}).items():
                    sd[sinfo.get("key", sname)] = sinfo.get("stat", {}).get("value", 0)
            mins = sd.get("minutes_played", 0)
            if mins > 0:
                t90 = (sd.get('touches', 0) / mins) * 90
                print(f"  {mname:<40} | Min: {mins:<2} | Touches: {sd.get('touches', 0):<2} (Per90: {t90:<4.1f}) | Passes: {sd.get('accurate_passes', 0):<2}/{sd.get('total_passes', 0):<2} | Final3rd: {sd.get('passes_into_final_third', 0)} | Chances: {sd.get('chances_created', 0)} | Disposs: {sd.get('dispossessed', 0)}")

