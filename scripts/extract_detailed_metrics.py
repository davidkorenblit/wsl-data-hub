import json

def load(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

# 1. Toko Koga Deep Dive
tot = load("scratch_tot_avl.json")
pstats_tot = tot.get("content", {}).get("playerStats", {})
for pid, pdata in pstats_tot.items():
    if "koga" in pdata.get("name", "").lower():
        print("=== TOKO KOGA FULL STATS ===")
        for cat in pdata.get("stats", []):
            print(f"[{cat.get('title')}]")
            for k, v in cat.get("stats", {}).items():
                st = v.get("stat", {})
                print(f"  {k}: {st.get('value')} (total: {st.get('total')})")

# 2. Andrea Medina Deep Dive
mun = load("scratch_mun_whu.json")
pstats_mun = mun.get("content", {}).get("playerStats", {})
for pid, pdata in pstats_mun.items():
    if "medina" in pdata.get("name", "").lower():
        print("\n=== ANDREA MEDINA STATS VS WEST HAM ===")
        for cat in pdata.get("stats", []):
            print(f"[{cat.get('title')}]")
            for k, v in cat.get("stats", {}).items():
                st = v.get("stat", {})
                print(f"  {k}: {st.get('value')} (total: {st.get('total')})")

# Also Maya Le Tissier
for pid, pdata in pstats_mun.items():
    if "tissier" in pdata.get("name", "").lower():
        print("\n=== MAYA LE TISSIER STATS VS WEST HAM ===")
        for cat in pdata.get("stats", []):
            print(f"[{cat.get('title')}]")
            for k, v in cat.get("stats", {}).items():
                st = v.get("stat", {})
                print(f"  {k}: {st.get('value')} (total: {st.get('total')})")

# 3. Chelsea Goal Breakdown (Min 39 Thompson)
che = load("scratch_che_ars.json")
shotmap = che.get("content", {}).get("shotmap", {}).get("shots", [])
for shot in shotmap:
    if shot.get("eventType") == "Goal" or shot.get("playerName") == "Alyssa Thompson":
        print("\n=== CHELSEA GOAL SHOTMAP DETAILS ===")
        print(f"Player: {shot.get('playerName')}, Min: {shot.get('min')}, xG: {shot.get('expectedGoals')}, xGOT: {shot.get('expectedGoalsOnTarget')}, situation: {shot.get('situation')}, shotType: {shot.get('shotType')}")

# Liveticker around min 39
print("\n=== LIVETICKER AROUND MIN 39 ===")
liveticker = che.get("content", {}).get("liveticker", {}).get("teams", [])
for t in che.get("content", {}).get("liveticker", {}).get("events", []):
    m = t.get("time")
    if m and 35 <= m <= 41:
        print(f"Min {m}: {t.get('text')}")
