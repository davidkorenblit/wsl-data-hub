import json
from pathlib import Path
import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROJECT_ROOT = Path("c:/Users/david/wsl_data_for_posts/wsl-data-hub")

def load_scratch(name):
    p = PROJECT_ROOT / f"scratch_{name}.json"
    if p.exists():
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

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

print("=" * 70)
print(" 1. SPURS VS ARSENAL - UNDER THE PRESS")
print("=" * 70)
tot_ars = load_scratch("tot_ars")
if tot_ars:
    content = tot_ars.get("content", {})
    # Team stats
    stats_dict = {}
    for grp in content.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
        for s in grp.get("stats", []):
            stats_dict[s.get("title") or s.get("key")] = s.get("stats")
    print(f"Spurs vs Arsenal stats: Possession={stats_dict.get('Ball possession')}, Passes={stats_dict.get('Accurate passes')}, Long balls={stats_dict.get('Accurate long balls')}")
    print(f"Dispossessed: {stats_dict.get('Dispossessed')}, Tackles won: {stats_dict.get('Tackles won')}")
    
    # Check shotmap
    print("\n--- Spurs Shots ---")
    for s in content.get("shotmap", {}).get("shots", []):
        if "tottenham" in s.get("teamName", "").lower() or s.get("teamId") == 628117:
            print(f"  {s.get('playerName')} {s.get('min')}' | xG: {s.get('expectedGoals')} | type: {s.get('shotType')} | isGoal: {s.get('eventType') == 'Goal'}")
    
    print("\n--- Spurs Players Key Stats ---")
    pstats = content.get("playerStats", {})
    for pid, p in pstats.items():
        name = p.get("name", "")
        team = p.get("teamName", "")
        if "tottenham" in team.lower() or any(t in name.lower() for t in ["tandberg", "koga", "holdt", "gaupset", "blakstad", "pelova", "spence", "kop", "nilden", "vinberg", "dijkstra"]):
            flat = get_player_stats_flat(p)
            rating = p.get("rating", {}).get("num") if isinstance(p.get("rating"), dict) else p.get("rating")
            print(f"* {name} (Rating: {rating}):")
            for k in ["Minutes played", "Goals", "Assists", "Accurate passes", "Long balls", "Accurate long balls", 
                      "Passes into final third", "Touches", "Dispossessed", "Possession lost", "Tackles won", 
                      "Interceptions", "Clearances", "Ground duels won", "Aerial duels won", "Chances created"]:
                if k in flat:
                    print(f"    - {k}: {flat[k]}")

print("\n" + "=" * 70)
print(" 2. MAN UNITED VS MAN CITY - HINATA MIYAZAWA & MIDFIELD")
print("=" * 70)
mun_mci = load_scratch("mun_mci")
if mun_mci:
    content = mun_mci.get("content", {})
    pstats = content.get("playerStats", {})
    for pid, p in pstats.items():
        name = p.get("name", "")
        if any(t in name.lower() for t in ["miyazawa", "toone", "park", "terland", "naalsund", "janssen", "le tissier", "tullis"]):
            flat = get_player_stats_flat(p)
            rating = p.get("rating", {}).get("num") if isinstance(p.get("rating"), dict) else p.get("rating")
            print(f"* {name} (Rating: {rating}):")
            for k in ["Minutes played", "Goals", "Assists", "Accurate passes", "Passes into final third", 
                      "Chances created", "Touches", "Dispossessed", "Possession lost", "Tackles won", 
                      "Interceptions", "Recoveries", "Ground duels won", "Aerial duels won", "Defensive actions"]:
                if k in flat:
                    print(f"    - {k}: {flat[k]}")

print("\n" + "=" * 70)
print(" 3. CHELSEA VS CRYSTAL PALACE - WITHOUT JAMES & WALSH")
print("=" * 70)
cry_che = load_scratch("cry_che")
if cry_che:
    content = cry_che.get("content", {})
    pstats = content.get("playerStats", {})
    lineup = content.get("lineup", {})
    print("Chelsea starters & subs check for James / Walsh:")
    all_che_names = [p.get("name", "") for pid, p in pstats.items() if "chelsea" in p.get("teamName", "").lower()]
    print(f"Chelsea players in match: {', '.join(all_che_names)}")
    for pid, p in pstats.items():
        name = p.get("name", "")
        if any(t in name.lower() for t in ["malard", "baltimore", "nusken", "cuthbert", "kaptein", "carpenter", "james", "walsh", "hamano"]):
            flat = get_player_stats_flat(p)
            rating = p.get("rating", {}).get("num") if isinstance(p.get("rating"), dict) else p.get("rating")
            print(f"* {name} (Rating: {rating}):")
            for k in ["Minutes played", "Goals", "Assists", "Expected goals (xG)", "Total shots", "Accurate passes", 
                      "Passes into final third", "Chances created", "Touches", "Touches in opposition box", 
                      "Dispossessed", "Ground duels won", "Tackles won", "Interceptions"]:
                if k in flat:
                    print(f"    - {k}: {flat[k]}")
