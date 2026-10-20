#!/usr/bin/env python3
"""
Enrich WSL Recent Results Data
==============================
Parses match facts, xG, shots, possession, and goal scorers from FotMob
cache/scratch files and generates enriched JSON for Jekyll front-end presentation.
"""

import json
from pathlib import Path
from datetime import datetime
import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SCRIPTS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPTS_DIR.parent
SITE_DATA_DIR = PROJECT_ROOT / "_data"
ASSETS_DATA_DIR = PROJECT_ROOT / "assets" / "data"
RAW_MATCHES_DIR = PROJECT_ROOT / "data" / "raw" / "fotmob" / "matches"

# Metadata mapping for teams
TEAMS_META = {
    258661: {"slug": "chelsea", "name_en": "Chelsea", "name_he": "צ'לסי", "color": "#034694"},
    231488: {"slug": "manchester-city", "name_en": "Manchester City", "name_he": "מנצ'סטר סיטי", "color": "#6CABDD"},
    258657: {"slug": "arsenal", "name_en": "Arsenal", "name_he": "ארסנל", "color": "#EF0107"},
    258665: {"slug": "liverpool", "name_en": "Liverpool", "name_he": "ליברפול", "color": "#C8102E"},
    258658: {"slug": "birmingham-city", "name_en": "Birmingham City", "name_he": "ברמינגהאם סיטי", "color": "#0000FF"},
    258663: {"slug": "everton", "name_en": "Everton", "name_he": "אברטון", "color": "#003399"},
    231497: {"slug": "west-ham", "name_en": "West Ham United", "name_he": "ווסטהאם", "color": "#7A263A"},
    231505: {"slug": "brighton", "name_en": "Brighton & Hove Albion", "name_he": "ברייטון", "color": "#0057B8"},
    628117: {"slug": "tottenham", "name_en": "Tottenham Hotspur", "name_he": "טוטנהאם", "color": "#132257"},
    954396: {"slug": "manchester-utd", "name_en": "Manchester United", "name_he": "מנצ'סטר יונייטד", "color": "#DA291C"},
    614828: {"slug": "crystal-palace", "name_en": "Crystal Palace", "name_he": "קריסטל פאלאס", "color": "#1B449C"},
    231494: {"slug": "aston-villa", "name_en": "Aston Villa", "name_he": "אסטון וילה", "color": "#670E36"},
    231502: {"slug": "charlton-athletic", "name_en": "Charlton Athletic", "name_he": "צ'רלטון אתלטיק", "color": "#D40000"},
    1075419: {"slug": "london-city-lionesses", "name_en": "London City Lionesses", "name_he": "לונדון סיטי ליונסס", "color": "#E91E63"},
    231508: {"slug": "leicester-city", "name_en": "Leicester City", "name_he": "לסטר סיטי", "color": "#003090"},
}

HEBREW_DAYS = ["שני", "שלישי", "רביעי", "חמישי", "שישי", "שבת", "ראשון"]
HEBREW_MONTHS = ["", "בינואר", "בפברואר", "במרץ", "באפריל", "במאי", "ביוני", "ביולי", "באוגוסט", "בספטמבר", "באוקטובר", "בנובמבר", "בדצמבר"]


def find_match_detail_file(match_id: int):
    # Check project root scratch files
    for p in PROJECT_ROOT.glob("scratch_*.json"):
        try:
            with open(p, "r", encoding="utf-8") as f:
                d = json.load(f)
                if d.get("general", {}).get("matchId") == match_id or d.get("header", {}).get("matchId") == match_id:
                    return d
        except Exception:
            continue
    # Check raw matches directory
    for p in RAW_MATCHES_DIR.glob(f"*{match_id}*.json"):
        try:
            with open(p, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            continue
    return None


def parse_details_from_raw(raw_detail: dict):
    content = raw_detail.get("content", {})
    facts = content.get("matchFacts", {})
    events = facts.get("events", {}).get("events", [])
    
    home_scorers_dict = {}
    away_scorers_dict = {}
    
    for e in events:
        if e.get("type") == "Goal":
            scorer = e.get("player", {}).get("name", "Unknown")
            minute = str(e.get("time", "")) + "'"
            is_og = e.get("ownGoal", False)
            if is_og:
                scorer += " (ע\"ע)"
            
            is_home = e.get("isHome", True)
            target_dict = home_scorers_dict if is_home else away_scorers_dict
            
            if scorer in target_dict:
                target_dict[scorer].append(minute)
            else:
                target_dict[scorer] = [minute]
                
    home_scorers = [{"name": name, "minute": ", ".join(mins)} for name, mins in home_scorers_dict.items()]
    away_scorers = [{"name": name, "minute": ", ".join(mins)} for name, mins in away_scorers_dict.items()]
    
    stats_map = {}
    for grp in content.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
        for s in grp.get("stats", []):
            stats_map[s.get("title") or s.get("key")] = s.get("stats")
            
    xg = stats_map.get("Expected goals (xG)", [None, None])
    shots = stats_map.get("Total shots", [None, None])
    sot = stats_map.get("Shots on target", [None, None])
    poss = stats_map.get("Ball possession", [None, None])
    
    return {
        "home_xg": str(xg[0]) if xg[0] is not None else None,
        "away_xg": str(xg[1]) if xg[1] is not None else None,
        "home_shots": shots[0] if shots[0] is not None else None,
        "away_shots": shots[1] if shots[1] is not None else None,
        "home_sot": sot[0] if sot[0] is not None else None,
        "away_sot": sot[1] if sot[1] is not None else None,
        "home_possession": poss[0] if poss[0] is not None else None,
        "away_possession": poss[1] if poss[1] is not None else None,
        "home_scorers": home_scorers,
        "away_scorers": away_scorers,
        "has_deep_stats": True
    }


def enrich_matchweek():
    recent_path = SITE_DATA_DIR / "wsl_recent_results.json"
    if not recent_path.exists():
        print(f"[!] {recent_path} does not exist.")
        return
        
    with open(recent_path, "r", encoding="utf-8") as f:
        matches = json.load(f)
        
    enriched = []
    for m in matches:
        mid = int(m.get("id"))
        home_id = int(m.get("home_id", 0))
        away_id = int(m.get("away_id", 0))
        
        home_meta = TEAMS_META.get(home_id, {
            "slug": m.get("home", "").lower().replace(" (w)", "").replace(" ", "-"),
            "name_en": m.get("home", "").replace(" (W)", ""),
            "name_he": m.get("home", "").replace(" (W)", ""),
            "color": "#4B5563"
        })
        away_meta = TEAMS_META.get(away_id, {
            "slug": m.get("away", "").lower().replace(" (w)", "").replace(" ", "-"),
            "name_en": m.get("away", "").replace(" (W)", ""),
            "name_he": m.get("away", "").replace(" (W)", ""),
            "color": "#4B5563"
        })
        
        # Determine winner
        h_score = m.get("home_score", 0)
        a_score = m.get("away_score", 0)
        if h_score > a_score:
            winner = "home"
        elif a_score > h_score:
            winner = "away"
        else:
            winner = "draw"
            
        # Format Date
        date_str = m.get("date", "")
        formatted_he = ""
        formatted_en = ""
        time_str = ""
        if date_str:
            try:
                dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                day_name_he = HEBREW_DAYS[dt.weekday()]
                formatted_he = f"יום {day_name_he}, {dt.day} {HEBREW_MONTHS[dt.month]}"
                formatted_en = dt.strftime("%A, %b %d")
                time_str = dt.strftime("%H:%M")
            except Exception:
                pass
                
        is_lcl = (home_meta["slug"] == "london-city-lionesses" or away_meta["slug"] == "london-city-lionesses")
        
        # Deep details
        raw_detail = find_match_detail_file(mid)
        deep_stats = parse_details_from_raw(raw_detail) if raw_detail else {
            "home_xg": None, "away_xg": None,
            "home_shots": None, "away_shots": None,
            "home_sot": None, "away_sot": None,
            "home_possession": None, "away_possession": None,
            "home_scorers": [], "away_scorers": [],
            "has_deep_stats": False
        }
        
        item = {
            "id": mid,
            "round": m.get("round"),
            "date": date_str,
            "date_formatted_he": formatted_he,
            "date_formatted_en": formatted_en,
            "time": time_str,
            "score": m.get("score"),
            "finished": m.get("finished", True),
            "reason": m.get("reason", "FT"),
            "winner": winner,
            "is_lcl": is_lcl,
            
            "home_id": home_id,
            "home_name": home_meta["name_en"],
            "home_name_he": home_meta["name_he"],
            "home_slug": home_meta["slug"],
            "home_color": home_meta["color"],
            "home_crest": f"https://images.fotmob.com/image_resources/logo/teamlogo/{home_id}_small.png",
            "home_score": h_score,
            
            "away_id": away_id,
            "away_name": away_meta["name_en"],
            "away_name_he": away_meta["name_he"],
            "away_slug": away_meta["slug"],
            "away_color": away_meta["color"],
            "away_crest": f"https://images.fotmob.com/image_resources/logo/teamlogo/{away_id}_small.png",
            "away_score": a_score,
            
            **deep_stats
        }
        enriched.append(item)
        
    # Save enriched results
    with open(recent_path, "w", encoding="utf-8") as f:
        json.dump(enriched, f, ensure_ascii=False, indent=2)
        
    with open(ASSETS_DATA_DIR / "wsl_recent_results.json", "w", encoding="utf-8") as f:
        json.dump(enriched, f, ensure_ascii=False, indent=2)
        
    print(f"✓ Enriched {len(enriched)} matches with deep stats, xG, scorers, and club styling.")


if __name__ == "__main__":
    enrich_matchweek()
