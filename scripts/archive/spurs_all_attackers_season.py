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

# All attack & midfield players
ATTACK_MID_TARGETS = [
    "Kirsty Hanson",
    "Cathinka Tandberg",
    "Signe Gaupset",
    "Matilda Vinberg",
    "Victoria Pelova",
    "Olivia Holdt",
    "Julie Blakstad",
    "Drew Spence",
    "Shekiera Martinez",
    "Matilda Nildén",
    "Jessica Naz",
    "Lenna Gunning-Williams",
    "Eveliina Summanen"
]

player_data = {name: [] for name in ATTACK_MID_TARGETS}

for mw, label, fpath in matches_info:
    p = Path(fpath)
    if not p.exists():
        continue
    with open(p, "r", encoding="utf-8") as f:
        d = json.load(f)
        
    home_name = d.get("general", {}).get("homeTeam", {}).get("name")
    spurs_side = "homeTeam" if "Tottenham" in home_name else "awayTeam"
    
    ps = d.get("content", {}).get("playerStats", {})
    lineup = d.get("content", {}).get("lineup", {}).get(spurs_side, {})
    all_players = lineup.get("starters", []) + lineup.get("subs", [])
    id_to_name = {str(pl.get("id")): pl.get("name") for pl in all_players}
    
    for pid, stats in ps.items():
        pname = id_to_name.get(pid, "")
        for target in ATTACK_MID_TARGETS:
            if target.lower() in pname.lower():
                mins = 0
                dispossessed = 0
                duels_lost = 0
                duels_won = 0
                dribbles = 0
                
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
                        dribbles = v.get("stat", {}).get("value") if isinstance(v, dict) else v
                        
                player_data[target].append({
                    "mw": mw,
                    "mins": mins or 0,
                    "dispossessed": dispossessed or 0,
                    "duels_lost": duels_lost or 0,
                    "duels_won": duels_won or 0,
                    "dribbles": dribbles or 0
                })

# Summary table
results = []
for name, matches in player_data.items():
    if not matches:
        continue
    tot_mins = sum(m['mins'] for m in matches)
    tot_disp = sum(m['dispossessed'] for m in matches)
    tot_lost = sum(m['duels_lost'] for m in matches)
    tot_won = sum(m['duels_won'] for m in matches)
    tot_drib = sum(m['dribbles'] for m in matches)
    tot_duels = tot_won + tot_lost
    win_pct = round(tot_won / tot_duels * 100) if tot_duels > 0 else 0
    
    per90_disp = round(tot_disp / (tot_mins / 90), 2) if tot_mins >= 45 else 0
    per90_lost = round(tot_lost / (tot_mins / 90), 2) if tot_mins >= 45 else 0
    
    results.append({
        "name": name,
        "apps": len(matches),
        "mins": tot_mins,
        "disp": tot_disp,
        "per90_disp": per90_disp,
        "lost": tot_lost,
        "won": tot_won,
        "tot_duels": tot_duels,
        "win_pct": win_pct,
        "per90_lost": per90_lost,
        "dribbles": tot_drib
    })

# Sort by per90_disp descending
results.sort(key=lambda x: (x['mins'] > 100, -x['per90_disp']), reverse=True)

print("=" * 115)
print(" ⚽ SPURS ATTACK & MIDFIELD: FULL SEASON COMPARISON (MW1-MW8)")
print("=" * 115)
print(f"{'Player':<24} {'Apps':<5} {'Mins':<6} {'Disp':<6} {'Disp/90':<9} {'Duels Lost':<11} {'Won':<6} {'Win %':<7} {'Lost/90':<9} {'Dribbles':<8}")
print("-" * 115)

for r in results:
    print(f"{r['name']:<24} {r['apps']:<5} {r['mins']:<6} {r['disp']:<6} {r['per90_disp']:<9} {r['lost']:<11} {r['won']:<6} {r['win_pct']:<5}% {r['per90_lost']:<9} {r['dribbles']:<8}")

print("=" * 115)

