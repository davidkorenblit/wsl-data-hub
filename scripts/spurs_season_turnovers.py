import json
from pathlib import Path

matches_info = [
    ("MW1", "vs West Ham (3-1)", "data/raw/fotmob/matches/mw1_tot_whu_5981534.json"),
    ("MW2", "at Liverpool (1-1)", "data/raw/fotmob/matches/mw2_liv_tot_5981638.json"),
    ("MW3", "at Crystal Palace (7-0)", "data/raw/fotmob/matches/mw3_cry_tot_5981646.json"),
    ("MW4", "vs Aston Villa (4-0)", "data/raw/fotmob/matches/mw4_tot_avl_5981653.json"),
    ("MW5", "vs LCL (1-6)", "data/raw/fotmob/matches/mw5_tot_lcl_5981655.json"),
    ("MW6", "at Chelsea (2-6)", "data/raw/fotmob/matches/mw6_che_tot_5981665.json"),
    ("MW7", "vs Arsenal (1-2)", "data/raw/fotmob/matches/mw7_tot_ars_5981675.json"),
    ("MW8", "at Birmingham (4-1)", "data/raw/fotmob/matches/mw8_bir_tot_5981678.json"),
]

TARGETS = ["Signe Gaupset", "Matilda Vinberg", "Victoria Pelova", "Olivia Holdt"]

# We will collect per match and season totals
season_stats = {name: [] for name in TARGETS}

for mw, label, fpath in matches_info:
    p = Path(fpath)
    if not p.exists():
        print(f"File missing: {fpath}")
        continue
    with open(p, "r", encoding="utf-8") as f:
        d = json.load(f)
    
    # Identify Spurs side
    home_name = d.get("general", {}).get("homeTeam", {}).get("name")
    spurs_side = "homeTeam" if "Tottenham" in home_name else "awayTeam"
    
    ps = d.get("content", {}).get("playerStats", {})
    lineup = d.get("content", {}).get("lineup", {}).get(spurs_side, {})
    all_players = lineup.get("starters", []) + lineup.get("subs", [])
    
    id_to_name = {str(pl.get("id")): pl.get("name") for pl in all_players}
    
    for pid, stats in ps.items():
        pname = id_to_name.get(pid)
        for target in TARGETS:
            if target in str(pname):
                # extract stats
                mins = 0
                dispossessed = 0
                duels_lost = 0
                duels_won = 0
                dribbles_succ = 0
                dribbles_att = 0
                rating = None
                
                for grp in stats.get("stats", []):
                    st = grp.get("stats", {})
                    if "Minutes played" in st:
                        v = st["Minutes played"]
                        mins = v.get("stat", {}).get("value") if isinstance(v, dict) else v
                    if "Dispossessed" in st:
                        v = st["Dispossessed"]
                        dispossessed = v.get("stat", {}).get("value") if isinstance(v, dict) else v
                    if "Duels lost" in st:
                        v = st["Duels lost"]
                        duels_lost = v.get("stat", {}).get("value") if isinstance(v, dict) else v
                    if "Duels won" in st:
                        v = st["Duels won"]
                        duels_won = v.get("stat", {}).get("value") if isinstance(v, dict) else v
                    if "Successful dribbles" in st:
                        v = st["Successful dribbles"]
                        dribbles_succ = v.get("stat", {}).get("value") if isinstance(v, dict) else v
                    if "FotMob rating" in st:
                        v = st["FotMob rating"]
                        rating = v.get("stat", {}).get("value") if isinstance(v, dict) else v
                        
                season_stats[target].append({
                    "mw": mw,
                    "label": label,
                    "mins": mins or 0,
                    "dispossessed": dispossessed or 0,
                    "duels_lost": duels_lost or 0,
                    "duels_won": duels_won or 0,
                    "total_duels": (duels_won or 0) + (duels_lost or 0),
                    "dribbles_succ": dribbles_succ or 0,
                    "rating": rating
                })

print("=" * 110)
print(" 📊 SPURS CORE 4: SEASON BREAKDOWN (DISPOSSESSED, DUELS, TURNOVERS)")
print("=" * 110)

for target in TARGETS:
    records = season_stats[target]
    print(f"\n🌟 {target.upper()} ({len(records)} appearances in 8 games)")
    print(f"{'Round':<6} {'Match':<26} {'Min':<6} {'Dispossessed':<14} {'Duels Lost':<12} {'Duels Won':<12} {'Win %':<8} {'Dribbles':<10} {'Rating':<6}")
    print("-" * 102)
    tot_mins = 0
    tot_disp = 0
    tot_lost = 0
    tot_won = 0
    tot_drib = 0
    for r in records:
        tot_mins += r['mins']
        tot_disp += r['dispossessed']
        tot_lost += r['duels_lost']
        tot_won += r['duels_won']
        tot_drib += r['dribbles_succ']
        t_duels = r['total_duels']
        pct = f"{round(r['duels_won']/t_duels*100)}%" if t_duels > 0 else "-"
        print(f"{r['mw']:<6} {r['label']:<26} {r['mins']:<6} {r['dispossessed']:<14} {r['duels_lost']:<12} {r['duels_won']:<12} {pct:<8} {r['dribbles_succ']:<10} {str(r['rating']):<6}")
    
    tot_duels = tot_won + tot_lost
    tot_pct = f"{round(tot_won/tot_duels*100)}%" if tot_duels > 0 else "-"
    per_90_disp = round(tot_disp / (tot_mins / 90), 2) if tot_mins > 0 else 0
    per_90_lost = round(tot_lost / (tot_mins / 90), 2) if tot_mins > 0 else 0
    print("-" * 102)
    print(f"{'TOTAL':<33} {tot_mins:<6} {tot_disp:<14} {tot_lost:<12} {tot_won:<12} {tot_pct:<8} {tot_drib:<10}")
    print(f"👉 Per 90 Stats: {per_90_disp} Dispossessed / 90 | {per_90_lost} Duels Lost / 90")

