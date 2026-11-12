"""
Fetch Chelsea Defense Deep Dive Data
====================================
Fetches detailed FotMob traits, stats sections, percentiles, and transfer activity
for Chelsea's backline:
- Veerle Buurman (1648650)
- Lucy Bronze (646031)
- Naomi Girma (1356262)
- Ellie Carpenter (773361)
- Sandy Baltimore (851315)
- Kadeisha Buchanan (646129)
"""

import json
import requests
from pathlib import Path

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

TARGETS = [
    {"id": 1648650, "name": "Veerle Buurman", "role_desc": "בלמת צעירה (הולנד) / בילד-אפ וניהול מסירה"},
    {"id": 646031, "name": "Lucy Bronze", "role_desc": "מגינה/בלמת שלישית / יציאה ללחץ ומסירה מקדמת"},
    {"id": 1356262, "name": "Naomi Girma", "role_desc": "בלמת מרכזית / קריאת משחק"},
    {"id": 773361, "name": "Ellie Carpenter", "role_desc": "מגינת כנף ימין סילונית / שורפת קו"},
    {"id": 851315, "name": "Sandy Baltimore", "role_desc": "שחקנית כנף/מגינת שמאל תוקפת"}
]

def fetch_player(player_id: int):
    url = f"https://www.fotmob.com/api/data/playerData?id={player_id}"
    res = requests.get(url, headers=HEADERS, timeout=15)
    res.raise_for_status()
    return res.json()

def parse_player(meta, raw):
    name = raw.get("name", meta["name"])
    pos_desc = raw.get("positionDescription", {})
    primary_pos = pos_desc.get("primaryPosition", {}).get("label", "Defender")
    
    traits = []
    for t in raw.get("traits", {}).get("items", []):
        traits.append({
            "title": t.get("title"),
            "percentile": int(round(t.get("value", 0) * 100))
        })
        
    stats_sections = []
    for sec in raw.get("firstSeasonStats", {}).get("statsSection", {}).get("items", []):
        sec_title = sec.get("title")
        items = []
        for item in sec.get("items", []):
            items.append({
                "metric": item.get("title"),
                "stat_value": item.get("statValue"),
                "per_90": round(float(item.get("per90", 0)), 2) if item.get("per90") is not None else None,
                "percentile_rank": round(float(item.get("percentileRankPer90", 0)), 1) if item.get("percentileRankPer90") is not None else None
            })
        stats_sections.append({"section": sec_title, "stats": items})
        
    return {
        "id": meta["id"],
        "name": name,
        "role_desc": meta["role_desc"],
        "primary_position": primary_pos,
        "traits": traits,
        "stats_sections": stats_sections
    }

def main():
    print("=== Fetching Chelsea Defensive Profiles from FotMob ===")
    results = []
    for t in TARGETS:
        print(f"Fetching {t['name']} (ID: {t['id']})...")
        try:
            raw = fetch_player(t["id"])
            p = parse_player(t, raw)
            results.append(p)
            print(f" -> OK: {len(p['traits'])} traits, {len(p['stats_sections'])} sections.")
        except Exception as e:
            print(f" -> Error: {e}")
            
    out_file = Path("_data/chelsea_defense_deep_dive.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Saved -> {out_file}")

if __name__ == "__main__":
    main()
