import json
from pathlib import Path

MATCHES_DIR = Path("data/raw/fotmob/matches")

MANUTD_ID = 954396

MATCH_FILES = [
    ("MW1", "London City Lionesses (A)", MATCHES_DIR / "mw1_lcl_mun_5981531.json"),
    ("MW2", "Chelsea (H)", MATCHES_DIR / "match_5981635.json"),
    ("MW3", "Arsenal (A)", MATCHES_DIR / "mw3_mun_ars_5981644.json"),
    ("MW4", "West Ham United (H)", MATCHES_DIR / "mw4_mun_whu_5981650.json"),
    ("MW5", "Liverpool (H)", MATCHES_DIR / "mw5_mun_liv_5981656.json"),
]

match_summaries = []
letissier_stats = []

for round_name, opp_label, fpath in MATCH_FILES:
    with open(fpath, "r", encoding="utf-8") as fp:
        d = json.load(fp)
    
    header = d.get("header", {})
    teams = header.get("teams", [])
    t0 = teams[0]
    t1 = teams[1]
    
    mu_is_home = (t0.get("id") == MANUTD_ID)
    mu_team = t0 if mu_is_home else t1
    opp_team = t1 if mu_is_home else t0
    
    mu_score = mu_team.get("score", 0)
    opp_score = opp_team.get("score", 0)
    opp_name = opp_team.get("name", "")
    
    content = d.get("content", {})
    all_stats = content.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", [])
    
    possession = 0.0
    xg_mu = 0.0
    xg_opp = 0.0
    shots_mu = 0
    shots_opp = 0
    sot_mu = 0
    sot_opp = 0
    shots_box_opp = 0
    tackles_mu = 0
    itc_mu = 0
    clearances_mu = 0
    blocks_mu = 0
    duels_won_mu = 0
    passes_acc_mu = ""
    
    for grp in all_stats:
        for item in grp.get("stats", []):
            title = item.get("title", "")
            vals = item.get("stats", [0, 0])
            if len(vals) < 2: continue
            v_mu = vals[0] if mu_is_home else vals[1]
            v_opp = vals[1] if mu_is_home else vals[0]
            
            if title == "Ball possession":
                try: possession = float(str(v_mu).replace("%", ""))
                except: pass
            elif title == "Expected goals (xG)" and v_mu is not None:
                try:
                    xg_mu = float(v_mu)
                    xg_opp = float(v_opp)
                except: pass
            elif title == "Total shots":
                try:
                    shots_mu = int(v_mu)
                    shots_opp = int(v_opp)
                except: pass
            elif title == "Shots on target":
                try:
                    sot_mu = int(v_mu)
                    sot_opp = int(v_opp)
                except: pass
            elif title == "Shots inside box":
                try:
                    shots_box_opp = int(v_opp)
                except: pass
            elif title == "Tackles":
                try:
                    tackles_mu = int(v_mu)
                except: pass
            elif title == "Interceptions":
                try:
                    itc_mu = int(v_mu)
                except: pass
            elif title == "Clearances":
                try:
                    clearances_mu = int(v_mu)
                except: pass
            elif title == "Blocks":
                try:
                    blocks_mu = int(v_mu)
                except: pass
            elif title == "Duels won":
                try:
                    duels_won_mu = int(v_mu)
                except: pass
            elif title == "Accurate passes":
                try:
                    passes_acc_mu = str(v_mu)
                except: pass

    match_summaries.append({
        "round": round_name,
        "opponent": opp_label,
        "opp_name": opp_name,
        "score": f"{mu_score} - {opp_score}",
        "mu_goals": mu_score,
        "opp_goals": opp_score,
        "result": "W" if mu_score > opp_score else ("L" if mu_score < opp_score else "D"),
        "possession": possession,
        "xg_mu": xg_mu,
        "xg_opp": xg_opp,
        "shots_mu": shots_mu,
        "shots_opp": shots_opp,
        "sot_mu": sot_mu,
        "sot_opp": sot_opp,
        "shots_box_opp": shots_box_opp,
        "tackles_mu": tackles_mu,
        "itc_mu": itc_mu,
        "clearances_mu": clearances_mu,
        "blocks_mu": blocks_mu,
        "duels_won_mu": duels_won_mu,
        "passes_acc_mu": passes_acc_mu,
        "clean_sheet": (opp_score == 0)
    })
    
    # Maya Le Tissier player stats
    pstats = content.get("playerStats", {})
    for pid, pdata in pstats.items():
        pname = pdata.get("name", "")
        if "tissier" in pname.lower():
            p_map = {"round": round_name, "opponent": opp_label, "name": pname}
            for cat in pdata.get("stats", []):
                for sk, sv in cat.get("stats", {}).items():
                    st = sv.get("stat", {})
                    p_map[sk] = st.get("value", 0)
                    if "total" in st:
                        p_map[f"{sk}_total"] = st.get("total", 0)
            letissier_stats.append(p_map)
            break

print("=" * 80)
print("MANCHESTER UNITED - MATCH BY MATCH DEFENSIVE EVOLUTION")
print("=" * 80)
for m in match_summaries:
    print(f"{m['round']} | {m['opponent']:25} | Score: {m['score']:5} ({m['result']}) | Poss: {m['possession']}% | xGA: {m['xg_opp']:.2f} | Shots Against: {m['shots_opp']} (SoT {m['sot_opp']}, Box {m['shots_box_opp']}) | Clear: {m['clearances_mu']} | Itc: {m['itc_mu']} | Tackles: {m['tackles_mu']} | Blocks: {m['blocks_mu']}")

print("\n" + "=" * 80)
print("MAYA LE TISSIER - MATCH BY MATCH DEFENSIVE & LEADERSHIP PROFILE")
print("=" * 80)
for lt in letissier_stats:
    min_pl = lt.get("Minutes played", 0)
    clr = lt.get("Clearances", 0)
    itc = lt.get("Interceptions", 0)
    rec = lt.get("Recoveries", 0)
    blk = lt.get("Blocks", 0)
    tackles_w = lt.get("Tackles won", 0)
    g_won = lt.get("Ground duels won", 0)
    g_tot = lt.get("Ground duels won_total", 0)
    a_won = lt.get("Aerial duels won", 0)
    a_tot = lt.get("Aerial duels won_total", 0)
    p_acc = lt.get("Accurate passes", 0)
    p_tot = lt.get("Accurate passes_total", 0)
    rating = lt.get("FotMob rating", 0)
    print(f"{lt['round']} | {lt['opponent']:25} | Min: {min_pl} | Clear: {clr} | Itc: {itc} | Rec: {rec} | Blk: {blk} | Duels: G {g_won}/{g_tot}, A {a_won}/{a_tot} | Pass: {p_acc}/{p_tot} | Rate: {rating}")

# Phase Comparisons: Before Arsenal (MW1-2) vs Arsenal & After (MW3-5)
before_matches = match_summaries[:2]
arsenal_match = match_summaries[2]
after_matches = match_summaries[2:] # MW3, MW4, MW5

print("\n" + "=" * 80)
print("AGGREGATE COMPARISON: BEFORE ARSENAL (MW1-2) VS ARSENAL ONWARDS (MW3-5)")
print("=" * 80)

def agg_phase(matches, label):
    n = len(matches)
    gc = sum(m["opp_goals"] for m in matches)
    xga = sum(m["xg_opp"] for m in matches)
    shots_a = sum(m["shots_opp"] for m in matches)
    sot_a = sum(m["sot_opp"] for m in matches)
    clr = sum(m["clearances_mu"] for m in matches)
    itc = sum(m["itc_mu"] for m in matches)
    tck = sum(m["tackles_mu"] for m in matches)
    blk = sum(m["blocks_mu"] for m in matches)
    cs = sum(1 for m in matches if m["clean_sheet"])
    print(f"[{label}] ({n} Matches):")
    print(f"  Goals Conceded: {gc} (avg {gc/n:.2f}/match)")
    print(f"  xGA: {xga:.2f} (avg {xga/n:.2f}/match)")
    print(f"  Shots Conceded: {shots_a} (avg {shots_a/n:.1f}/match), SoT: {sot_a} (avg {sot_a/n:.1f}/match)")
    print(f"  Clearances: {clr} (avg {clr/n:.1f}/match)")
    print(f"  Interceptions: {itc} (avg {itc/n:.1f}/match)")
    print(f"  Tackles: {tck} (avg {tck/n:.1f}/match)")
    print(f"  Blocks: {blk} (avg {blk/n:.1f}/match)")
    print(f"  Clean Sheets: {cs}/{n}")

agg_phase(before_matches, "BEFORE ARSENAL (MW1-2: LCL & Chelsea)")
print("")
agg_phase([arsenal_match], "THE ARSENAL MATCH (MW3: Emirates 1-1)")
print("")
agg_phase(after_matches, "FROM ARSENAL ONWARDS (MW3-5: Arsenal, West Ham, Liverpool)")

# Export to _data
output = {
    "matches": match_summaries,
    "maya_le_tissier": letissier_stats
}
with open("_data/manutd_mw5_deep_analysis.json", "w", encoding="utf-8") as fp:
    json.dump(output, fp, indent=2, ensure_ascii=False)
print("\nSaved _data/manutd_mw5_deep_analysis.json successfully.")
