import json
from pathlib import Path

# Match sources
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

# MW8 match detailed data
mw8_path = Path("data/raw/fotmob/matches/mw8_bir_tot_5981678.json")
with open(mw8_path, "r", encoding="utf-8") as f:
    d8 = json.load(f)

ps8 = d8.get("content", {}).get("playerStats", {})
lineup8 = d8.get("content", {}).get("lineup", {}).get("awayTeam", {})
starters8 = lineup8.get("starters", [])
subs8 = lineup8.get("subs", [])

mw8_players = []
for p in starters8 + subs8:
    pid = str(p.get("id"))
    st = ps8.get(pid, {})
    pname = p.get("name")
    is_starter = p in starters8
    
    mins = 0
    dispossessed = 0
    duels_lost = 0
    duels_won = 0
    dribbles = 0
    rating = None
    
    for grp in st.get("stats", []):
        s_dict = grp.get("stats", {})
        if "Minutes played" in s_dict:
            mins = s_dict["Minutes played"].get("stat", {}).get("value")
        if "Dispossessed" in s_dict:
            dispossessed = s_dict["Dispossessed"].get("stat", {}).get("value")
        if "Duels lost" in s_dict:
            duels_lost = s_dict["Duels lost"].get("stat", {}).get("value")
        if "Duels won" in s_dict:
            duels_won = s_dict["Duels won"].get("stat", {}).get("value")
        if "Successful dribbles" in s_dict:
            dribbles = s_dict["Successful dribbles"].get("stat", {}).get("value")
        if "FotMob rating" in s_dict:
            rating = s_dict["FotMob rating"].get("stat", {}).get("value")
            
    total_d = (duels_won or 0) + (duels_lost or 0)
    win_pct = round(duels_won / total_d * 100) if total_d > 0 else 0
    
    mw8_players.append({
        "player": pname,
        "role": "Starter" if is_starter else "Sub",
        "minutes": mins or 0,
        "dispossessed": dispossessed or 0,
        "duels_lost": duels_lost or 0,
        "duels_won": duels_won or 0,
        "total_duels": total_d,
        "duels_win_pct": win_pct,
        "dribbles": dribbles or 0,
        "fotmob_rating": rating
    })

# Season Aggregation for attackers & midfielders
TARGETS = [
    "Julie Blakstad",
    "Drew Spence",
    "Matilda Vinberg",
    "Cathinka Tandberg",
    "Shekiera Martinez",
    "Kirsty Hanson",
    "Signe Gaupset",
    "Victoria Pelova",
    "Olivia Holdt",
    "Eveliina Summanen",
    "Matilda Nildén"
]

season_records = {name: [] for name in TARGETS}

for mw, label, fpath in matches_info:
    p = Path(fpath)
    if not p.exists():
        continue
    with open(p, "r", encoding="utf-8") as f:
        d = json.load(f)
    home_name = d.get("general", {}).get("homeTeam", {}).get("name")
    spurs_side = "homeTeam" if "Tottenham" in home_name else "awayTeam"
    ps = d.get("content", {}).get("playerStats", {})
    all_p = d.get("content", {}).get("lineup", {}).get(spurs_side, {}).get("starters", []) + \
            d.get("content", {}).get("lineup", {}).get(spurs_side, {}).get("subs", [])
    id_map = {str(pl.get("id")): pl.get("name") for pl in all_p}
    
    for pid, st in ps.items():
        pname = id_map.get(pid, "")
        for t in TARGETS:
            if t.lower() in pname.lower():
                mins = 0
                disp = 0
                lost = 0
                won = 0
                drib = 0
                rat = None
                for grp in st.get("stats", []):
                    sd = grp.get("stats", {})
                    if "Minutes played" in sd:
                        mins = sd["Minutes played"].get("stat", {}).get("value")
                    if "Dispossessed" in sd:
                        disp = sd["Dispossessed"].get("stat", {}).get("value")
                    if "Duels lost" in sd:
                        lost = sd["Duels lost"].get("stat", {}).get("value")
                    if "Duels won" in sd:
                        won = sd["Duels won"].get("stat", {}).get("value")
                    if "Successful dribbles" in sd:
                        drib = sd["Successful dribbles"].get("stat", {}).get("value")
                    if "FotMob rating" in sd:
                        rat = sd["FotMob rating"].get("stat", {}).get("value")
                        
                season_records[t].append({
                    "round": mw,
                    "match": label,
                    "minutes": mins or 0,
                    "dispossessed": disp or 0,
                    "duels_lost": lost or 0,
                    "duels_won": won or 0,
                    "total_duels": (won or 0) + (lost or 0),
                    "dribbles": drib or 0,
                    "rating": rat
                })

season_summary = []
for name, m_list in season_records.items():
    if not m_list:
        continue
    tot_mins = sum(m['minutes'] for m in m_list)
    tot_disp = sum(m['dispossessed'] for m in m_list)
    tot_lost = sum(m['duels_lost'] for m in m_list)
    tot_won = sum(m['duels_won'] for m in m_list)
    tot_drib = sum(m['dribbles'] for m in m_list)
    total_d = tot_won + tot_lost
    win_pct = round(tot_won / total_d * 100) if total_d > 0 else 0
    per90_disp = round(tot_disp / (tot_mins / 90), 2) if tot_mins >= 45 else 0
    per90_lost = round(tot_lost / (tot_mins / 90), 2) if tot_mins >= 45 else 0
    
    season_summary.append({
        "player": name,
        "appearances": len(m_list),
        "total_minutes": tot_mins,
        "dispossessed_total": tot_disp,
        "dispossessed_per_90": per90_disp,
        "duels_lost_total": tot_lost,
        "duels_won_total": tot_won,
        "total_duels": total_d,
        "duels_win_pct": win_pct,
        "duels_lost_per_90": per90_lost,
        "successful_dribbles": tot_drib,
        "match_log": m_list
    })

# Sort summary by dispossessed per 90
season_summary.sort(key=lambda x: (x['total_minutes'] >= 100, x['dispossessed_per_90']))

data_output = {
    "metadata": {
        "title": "Tottenham Hotspur - Attackers & Midfielders Dispossessed & Duels Analysis",
        "description": "Comprehensive tracking of dispossessed turnovers, duels lost/won, and dribbles across Matchweeks 1 to 8 of the 2026/27 WSL season.",
        "season": "2026/27",
        "rounds_analyzed": "MW1 to MW8",
        "generated_at": "2026-11-03"
    },
    "season_summary_attack_and_midfield": season_summary,
    "mw8_birmingham_all_players": mw8_players
}

out_file = Path("_data/spurs_turnovers_and_duels_season.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(data_output, f, ensure_ascii=False, indent=2)

print(f"Successfully saved {out_file} ({len(season_summary)} players, {len(mw8_players)} in MW8 match).")

