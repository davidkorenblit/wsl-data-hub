"""
Tottenham Hotspur Women & Victoria Pelova Data Pipeline
======================================================
1. Fetches current squad for 2026/2027 (including new signings).
2. Fetches detailed profile & advanced metrics for key attacking stars:
   - Olivia Holdt (Tottenham 2025/2026)
   - Signe Gaupset (Tottenham 2025/2026)
   - Cathinka Tandberg (Tottenham 2025/2026)
   - Julie Blakstad (Tottenham 2025/2026)
   - Victoria Pelova (Arsenal 2025/2026 -> Tottenham 2026/2027)
   - Kirsty Hanson (Aston Villa -> Tottenham 2026/2027)
3. Persists full data to `_data/tottenham_advanced_attack.json` and `_data/transfers/tottenham.json`.
"""

import json
import requests
from pathlib import Path
from typing import Dict, Any, List

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

PLAYERS = [
    {"id": 1030313, "name": "Olivia Holdt", "role_desc": "קשרית / שחקנית כנף / חופשית", "club_25_26": "Tottenham Hotspur"},
    {"id": 1285343, "name": "Signe Gaupset", "role_desc": "קשרית התקפית / פליימייקרית", "club_25_26": "Tottenham Hotspur / Brann"},
    {"id": 1140227, "name": "Cathinka Tandberg", "role_desc": "חלוצה מרכזית / פינישרית", "club_25_26": "Tottenham Hotspur"},
    {"id": 1031793, "name": "Julie Blakstad", "role_desc": "מגנת כנף / שחקנית אגף שלמה", "club_25_26": "Tottenham Hotspur"},
    {"id": 1055898, "name": "Victoria Pelova", "role_desc": "קשרית יצירתית / 8-10 (רכש חדש מארסנל)", "club_25_26": "Arsenal"},
    {"id": 1082557, "name": "Kirsty Hanson", "role_desc": "שחקנית כנף / דריבליסטית (רכש מאסטון וילה)", "club_25_26": "Aston Villa"},
    {"id": 1215012, "name": "Caitlin Dijkstra", "role_desc": "בלמית בינלאומית (רכש מוולפסבורג)", "club_25_26": "Wolfsburg"},
    {"id": 1214575, "name": "Alice Sombath", "role_desc": "בלמית / מגנת (רכש מליון)", "club_25_26": "Lyon"}
]

def fetch_player_data(player_id: int) -> Dict[str, Any]:
    url = f"https://www.fotmob.com/api/data/playerData?id={player_id}"
    res = requests.get(url, headers=HEADERS, timeout=15)
    res.raise_for_status()
    return res.json()

def process_player(meta: Dict[str, Any], raw_data: Dict[str, Any]) -> Dict[str, Any]:
    name = raw_data.get("name", meta["name"])
    primary_pos = raw_data.get("positionDescription", {}).get("primaryPosition", {}).get("label", "Midfielder")
    
    traits = []
    for t in raw_data.get("traits", {}).get("items", []):
        traits.append({
            "title": t.get("title"),
            "percentile": int(round(t.get("value", 0) * 100))
        })
        
    stats_sections = []
    season_groups = raw_data.get("firstSeasonStats", {}).get("statsSection", {}).get("items", [])
    for group in season_groups:
        grp_title = group.get("title")
        items = []
        for stat in group.get("items", []):
            items.append({
                "metric": stat.get("title"),
                "stat_value": stat.get("statValue"),
                "per_90": round(float(stat.get("per90", 0)), 2) if stat.get("per90") is not None else None,
                "percentile_rank": round(float(stat.get("percentileRankPer90", 0)), 1) if stat.get("percentileRankPer90") is not None else None
            })
        stats_sections.append({
            "section": grp_title,
            "stats": items
        })
        
    return {
        "id": meta["id"],
        "name": name,
        "role_desc": meta["role_desc"],
        "club_25_26": meta["club_25_26"],
        "primary_position": primary_pos,
        "traits": traits,
        "stats_sections": stats_sections
    }

def main():
    print("=== Fetching Advanced Player Data for Spurs & Key Signings ===")
    results = []
    
    for p in PLAYERS:
        print(f"Fetching {p['name']} (ID: {p['id']})...")
        try:
            raw = fetch_player_data(p["id"])
            processed = process_player(p, raw)
            results.append(processed)
            print(f" -> OK: {len(processed['traits'])} traits, {len(processed['stats_sections'])} stat groups.")
        except Exception as e:
            print(f" -> Error fetching {p['name']}: {e}")
            
    # Save advanced attack data
    out_file = Path("_data/tottenham_advanced_attack.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved all player data -> {out_file}")

    # Build comprehensive transfers file
    transfers_data = {
        "team": "Tottenham Hotspur Women",
        "season_completed": "2025/26",
        "season_new": "2026/27",
        "summary": {
            "total_new_signings": 6,
            "total_departures": 5,
            "headline": "עידן מרטין הו יוצא לדרך: מהפכת מנהיגות, קישור איכותי מארסנל וחיזוק צעיר ורב-גוני"
        },
        "transfers_in": [
            {
                "player": "Victoria Pelova",
                "name_he": "ויקטוריה פלובה",
                "pos": "MF",
                "from": "Arsenal",
                "nation": "NED",
                "role": "קשרית התקפית יצירתית, מנהיגת קישור, שליטה בקצב וראיית משחק עילאית"
            },
            {
                "player": "Caitlin Dijkstra",
                "name_he": "קייטלין דייקסטרה",
                "pos": "DF",
                "from": "VfL Wolfsburg",
                "nation": "NED",
                "role": "בלמת נבחרת הולנד, ניסיון בינלאומי, יציבות ובנייה מאחור"
            },
            {
                "player": "Alice Sombath",
                "name_he": "אליס סומבאת",
                "pos": "DF",
                "from": "Lyon",
                "nation": "FRA",
                "role": "שחקנית הגנה פיזית ומהירה מליון, גמישות בכל עמדות ההגנה"
            },
            {
                "player": "Kirsty Hanson",
                "name_he": "קירסטי הנסון",
                "pos": "FW/MF",
                "from": "Aston Villa",
                "nation": "SCO",
                "role": "שחקנית כנף ישירה, דריבל מסוכן ואספקת כדורים לרחבה"
            },
            {
                "player": "Selma Panengstuen",
                "name_he": "סלמה פננגסטואן",
                "pos": "GK",
                "from": "Kolbotn",
                "nation": "NOR",
                "role": "שוערת נורווגית צעירה ומבטיחה לעיבוי עמדת השוערות לצד ליזה קופ"
            },
            {
                "player": "Shekiera Martinez",
                "name_he": "שקירה מרטינז",
                "pos": "FW",
                "from": "Eintracht Frankfurt / West Ham",
                "nation": "GER",
                "role": "חלוצה מרכזית בעלת נוכחות ומהירות ברחבה"
            }
        ],
        "transfers_out": [
            {
                "player": "Bethany England",
                "name_he": "בת' אנגלנד",
                "pos": "FW",
                "to": "Crystal Palace",
                "impact": "קפטנית ומנהיגת הקבוצה בשנים האחרונות. עזיבה מסיבית שיוצרת חלל מנהיגותי"
            },
            {
                "player": "Molly Bartrip",
                "name_he": "מולי בארטריפ",
                "pos": "DF",
                "to": "Crystal Palace",
                "impact": "עמוד התווך של ההגנה וסגנית הקפטנית, עברה יחד עם בת' לפאלאס"
            },
            {
                "player": "Martha Thomas",
                "name_he": "מרתה תומאס",
                "pos": "FW/MF",
                "to": "עזיבה / העברה",
                "impact": "חלוצה/קשרית התקפית ורסטילית"
            },
            {
                "player": "Kit Graham",
                "name_he": "קיט גרהאם",
                "pos": "MF",
                "to": "עזיבה",
                "impact": "קשרית ותיקה בסגל"
            },
            {
                "player": "Charlotte Grant",
                "name_he": "שרלוט גרנט",
                "pos": "DF",
                "to": "עזיבה",
                "impact": "מגנת נבחרת אוסטרליה"
            }
        ]
    }
    
    transfers_path = Path("_data/transfers/tottenham.json")
    with open(transfers_path, "w", encoding="utf-8") as f:
        json.dump(transfers_data, f, ensure_ascii=False, indent=2)
    print(f"Saved Tottenham transfers -> {transfers_path}")

if __name__ == "__main__":
    main()
