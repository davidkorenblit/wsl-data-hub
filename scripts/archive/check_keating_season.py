import json
from pathlib import Path

# Search all Liverpool matches in data/raw/fotmob/matches
keating_season = []
for p in sorted(Path("data/raw/fotmob/matches").glob("*.json")):
    try:
        d = json.load(open(p, "r", encoding="utf-8"))
        home = d.get("general", {}).get("homeTeam", {}).get("name")
        away = d.get("general", {}).get("awayTeam", {}).get("name")
        if "Liverpool" in home or "Liverpool" in away:
            liv_side = "homeTeam" if "Liverpool" in home else "awayTeam"
            opp_name = away if liv_side == "homeTeam" else home
            score = f"{d.get('header', {}).get('teams', [{}])[0].get('score')} - {d.get('header', {}).get('teams', [{}])[1].get('score')}"
            ps = d.get("content", {}).get("playerStats", {})
            lineup = d.get("content", {}).get("lineup", {}).get(liv_side, {})
            all_p = lineup.get("starters", []) + lineup.get("subs", [])
            id_map = {str(pl.get("id")): pl.get("name") for pl in all_p}
            for pid, st in ps.items():
                pname = id_map.get(pid, "")
                if "Keating" in pname:
                    st_dict = {}
                    for g in st.get("stats", []):
                        for k, v in g.get("stats", {}).items():
                            val = v.get("stat", {}).get("value") if isinstance(v, dict) else v
                            st_dict[k] = val
                    keating_season.append({
                        "file": p.name,
                        "match": f"{home} vs {away} ({score})",
                        "mins": st_dict.get("Minutes played"),
                        "goals_conceded": st_dict.get("Goals conceded"),
                        "saves": st_dict.get("Saves"),
                        "xgot_faced": st_dict.get("xGOT faced"),
                        "goals_prevented": st_dict.get("Goals prevented"),
                        "rating": st_dict.get("FotMob rating")
                    })
    except Exception:
        pass

print("=== KHIARA KEATING SEASON STATS ===")
for k in keating_season:
    print(k)

