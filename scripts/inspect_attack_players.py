import json
import requests
from pathlib import Path

# 1. Alexia Putellas
fp = Path(r"c:\Users\david\wsl_data_for_posts\wsl-data-hub\data\raw\fotmob\players\player_462289_alexia_putellas.json")
with open(fp, "r", encoding="utf-8") as f:
    alexia = json.load(f)

print("=== ALEXIA PUTELLAS ===")
traits = alexia.get("traits", {})
if traits:
    for t in traits.get("items", []):
        print(f"  * {t.get('title')}: {int(t.get('value', 0)*100)}th percentile")

first_sec = alexia.get("firstSeasonStats", {}).get("statsSection", {})
for g in first_sec.get("items", []):
    print(f"\nGroup: {g.get('title')}")
    for item in g.get("items", []):
        t = item.get("title")
        p90 = round(float(item.get("per90", 0)), 2)
        pct = round(float(item.get("percentileRankPer90", 0)), 1)
        print(f"   - {t}: Per90={p90} | Pct={pct}%")

# 2. Kadidiatou Diani search
headers = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
r = requests.get("https://www.fotmob.com/api/data/search/suggest?term=Diani", headers=headers).json()
print("\n=== DIANI SEARCH ===")
diani_id = None
for group in r:
    for s in group.get("suggestions", []):
        stype = s.get("type")
        sid = s.get("id")
        sname = s.get("name")
        steam = s.get("teamName")
        print(f"  [{stype}] ID: {sid}, Name: {sname}, Team: {steam}")
        if "diani" in str(sname).lower() and stype == "player":
            diani_id = sid

if diani_id:
    p_url = f"https://www.fotmob.com/api/data/playerData?id={diani_id}"
    p_res = requests.get(p_url, headers=headers).json()
    print("\n=== DIANI METRICS ===")
    d_traits = p_res.get("traits", {})
    if d_traits:
        for t in d_traits.get("items", []):
            print(f"  * {t.get('title')}: {int(t.get('value', 0)*100)}th percentile")
    d_sec = p_res.get("firstSeasonStats", {}).get("statsSection", {})
    for g in d_sec.get("items", []):
        print(f"\nGroup: {g.get('title')}")
        for item in g.get("items", []):
            t = item.get("title")
            p90 = round(float(item.get("per90", 0)), 2)
            pct = round(float(item.get("percentileRankPer90", 0)), 1)
            print(f"   - {t}: Per90={p90} | Pct={pct}%")
