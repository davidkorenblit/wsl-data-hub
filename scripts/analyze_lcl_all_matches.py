import json
from pathlib import Path

MATCHES_DIR = Path("data/raw/fotmob/matches")

MATCH_FILES = [
    ("MW1", MATCHES_DIR / "mw1_lcl_mun_5981531.json"),
    ("MW2", MATCHES_DIR / "mw2_whu_lcl_5981634.json"),
    ("MW3", MATCHES_DIR / "mw3_cha_lcl_5981642.json"),
    ("MW4", MATCHES_DIR / "mw4_lcl_bha_5981649.json"),
    ("MW5", MATCHES_DIR / "mw5_tot_lcl_5981655.json"),
]

LCL_ID = 1075419

match_summaries = []

for round_name, fpath in MATCH_FILES:
    with open(fpath, "r", encoding="utf-8") as fp:
        d = json.load(fp)
    
    header = d.get("header", {})
    teams = header.get("teams", [])
    t0 = teams[0]
    t1 = teams[1]
    
    lcl_is_home = (t0.get("id") == LCL_ID)
    lcl_team = t0 if lcl_is_home else t1
    opp_team = t1 if lcl_is_home else t0
    
    lcl_score = lcl_team.get("score", 0)
    opp_score = opp_team.get("score", 0)
    opp_name = opp_team.get("name", "")
    
    content = d.get("content", {})
    all_stats = content.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", [])
    
    possession = 0.0
    xg_lcl = 0.0
    xg_opp = 0.0
    shots_lcl = 0
    shots_opp = 0
    sot_lcl = 0
    sot_opp = 0
    tackles_lcl = 0
    tackles_opp = 0
    itc_lcl = 0
    itc_opp = 0
    clearances_lcl = 0
    duels_won_lcl = 0
    duels_won_opp = 0
    
    for grp in all_stats:
        for item in grp.get("stats", []):
            title = item.get("title", "")
            vals = item.get("stats", [0, 0])
            if len(vals) < 2: continue
            v_lcl = vals[0] if lcl_is_home else vals[1]
            v_opp = vals[1] if lcl_is_home else vals[0]
            
            if title == "Ball possession":
                try: possession = float(str(v_lcl).replace("%", ""))
                except: pass
            elif title == "Expected goals (xG)" and v_lcl is not None:
                try:
                    xg_lcl = float(v_lcl)
                    xg_opp = float(v_opp)
                except: pass
            elif title == "Total shots":
                try:
                    shots_lcl = int(v_lcl)
                    shots_opp = int(v_opp)
                except: pass
            elif title == "Shots on target":
                try:
                    sot_lcl = int(v_lcl)
                    sot_opp = int(v_opp)
                except: pass
            elif title == "Tackles":
                try:
                    tackles_lcl = int(v_lcl)
                    tackles_opp = int(v_opp)
                except: pass
            elif title == "Interceptions":
                try:
                    itc_lcl = int(v_lcl)
                    itc_opp = int(v_opp)
                except: pass
            elif title == "Clearances":
                try:
                    clearances_lcl = int(v_lcl)
                except: pass
            elif title == "Duels won":
                try:
                    duels_won_lcl = int(v_lcl)
                    duels_won_opp = int(v_opp)
                except: pass

    match_summaries.append({
        "round": round_name,
        "opponent": opp_name,
        "is_home": lcl_is_home,
        "score": f"{lcl_score} - {opp_score}",
        "lcl_score": lcl_score,
        "opp_score": opp_score,
        "result": "W" if lcl_score > opp_score else ("L" if lcl_score < opp_score else "D"),
        "possession": possession,
        "xg_lcl": xg_lcl,
        "xg_opp": xg_opp,
        "shots_lcl": shots_lcl,
        "shots_opp": shots_opp,
        "sot_lcl": sot_lcl,
        "sot_opp": sot_opp,
        "tackles_lcl": tackles_lcl,
        "itc_lcl": itc_lcl,
        "clearances_lcl": clearances_lcl,
        "duels_won_lcl": duels_won_lcl,
        "clean_sheet": (opp_score == 0)
    })

print("=== COMPLETE LCL MATCH BREAKDOWN (WSL 2026/27) ===")
for m in match_summaries:
    print(f"{m['round']} | vs {m['opponent']:22} | Score: {m['score']:5} ({m['result']}) | Poss: {m['possession']}% | xG: {m['xg_lcl']:.2f}-{m['xg_opp']:.2f} | Shots: {m['shots_lcl']}-{m['shots_opp']} (SoT {m['sot_lcl']}-{m['sot_opp']}) | Tackles: {m['tackles_lcl']} | Interceptions: {m['itc_lcl']} | CS: {m['clean_sheet']}")

# Save summaries to a temporary json
with open("_data/lcl_matches_analyzed.json", "w", encoding="utf-8") as fp:
    json.dump(match_summaries, fp, indent=2, ensure_ascii=False)
