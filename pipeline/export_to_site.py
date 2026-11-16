"""
WSL Data Platform - Serving / Export Layer
==========================================
Extracts the latest Gold analytics tables from Supabase PostgreSQL
and updates Jekyll site JSON datasets:
  - _data/league_table.json
  - assets/data/league_table.json
  - _data/wsl_recent_results.json
  - assets/data/wsl_recent_results.json
"""
import os
import sys
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SITE_DATA_DIR = PROJECT_ROOT / "_data"
ASSETS_DATA_DIR = PROJECT_ROOT / "assets" / "data"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("SiteExporter")

TEAMS_META: Dict[int, Dict[str, Any]] = {
    258661: {"slug": "chelsea", "name_en": "Chelsea", "name_he": "צ'לסי", "color": "#034694", "crest": "https://images.fotmob.com/image_resources/logo/teamlogo/258661_small.png"},
    231488: {"slug": "manchester-city", "name_en": "Manchester City", "name_he": "מנצ'סטר סיטי", "color": "#6CABDD", "crest": "https://images.fotmob.com/image_resources/logo/teamlogo/231488_small.png"},
    258657: {"slug": "arsenal", "name_en": "Arsenal", "name_he": "ארסנל", "color": "#EF0107", "crest": "https://images.fotmob.com/image_resources/logo/teamlogo/258657_small.png"},
    258665: {"slug": "liverpool", "name_en": "Liverpool", "name_he": "ליברפול", "color": "#C8102E", "crest": "https://images.fotmob.com/image_resources/logo/teamlogo/258665_small.png"},
    258658: {"slug": "birmingham-city", "name_en": "Birmingham City", "name_he": "ברמינגהאם סיטי", "color": "#0000FF", "crest": "https://images.fotmob.com/image_resources/logo/teamlogo/258658_small.png"},
    258663: {"slug": "everton", "name_en": "Everton", "name_he": "אברטון", "color": "#003399", "crest": "https://images.fotmob.com/image_resources/logo/teamlogo/258663_small.png"},
    231497: {"slug": "west-ham", "name_en": "West Ham United", "name_he": "ווסטהאם", "color": "#7A263A", "crest": "https://images.fotmob.com/image_resources/logo/teamlogo/231497_small.png"},
    231505: {"slug": "brighton", "name_en": "Brighton & Hove Albion", "name_he": "ברייטון", "color": "#0057B8", "crest": "https://images.fotmob.com/image_resources/logo/teamlogo/231505_small.png"},
    628117: {"slug": "tottenham", "name_en": "Tottenham Hotspur", "name_he": "טוטנהאם", "color": "#132257", "crest": "https://images.fotmob.com/image_resources/logo/teamlogo/628117_small.png"},
    954396: {"slug": "manchester-utd", "name_en": "Manchester United", "name_he": "מנצ'סטר יונייטד", "color": "#DA291C", "crest": "https://images.fotmob.com/image_resources/logo/teamlogo/954396_small.png"},
    614828: {"slug": "crystal-palace", "name_en": "Crystal Palace", "name_he": "קריסטל פאלאס", "color": "#1B449C", "crest": "https://images.fotmob.com/image_resources/logo/teamlogo/614828_small.png"},
    231494: {"slug": "aston-villa", "name_en": "Aston Villa", "name_he": "אסטון וילה", "color": "#670E36", "crest": "https://images.fotmob.com/image_resources/logo/teamlogo/231494_small.png"},
    231502: {"slug": "charlton-athletic", "name_en": "Charlton Athletic", "name_he": "צ'רלטון אתלטיק", "color": "#D40000", "crest": "https://images.fotmob.com/image_resources/logo/teamlogo/231502_small.png"},
    1075419: {"slug": "london-city-lionesses", "name_en": "London City Lionesses", "name_he": "לונדון סיטי ליונסס", "color": "#E91E63", "crest": "https://images.fotmob.com/image_resources/logo/teamlogo/1075419_small.png"},
    231508: {"slug": "leicester-city", "name_en": "Leicester City", "name_he": "לסטר סיטי", "color": "#003090", "crest": "https://images.fotmob.com/image_resources/logo/teamlogo/231508_small.png"},
}

HEBREW_DAYS = ["שני", "שלישי", "רביעי", "חמישי", "שישי", "שבת", "ראשון"]
HEBREW_MONTHS = ["", "בינואר", "בפברואר", "במרץ", "באפריל", "במאי", "ביוני", "ביולי", "באוגוסט", "בספטמבר", "באוקטובר", "בנובמבר", "בדצמבר"]


def export_recent_results_to_site() -> List[Dict[str, Any]]:
    """Extracts and formats recent matches from latest finished round for the homepage widget."""
    matches_file = SITE_DATA_DIR / "wsl_matches.json"
    if not matches_file.exists():
        logger.warning(f"{matches_file} does not exist. Skipping recent results export.")
        return []

    with open(matches_file, "r", encoding="utf-8") as f:
        matches = json.load(f)

    finished_rounds = set()
    for m in matches:
        if m.get("finished"):
            finished_rounds.add(m.get("round"))

    if not finished_rounds:
        logger.warning("No finished rounds found in wsl_matches.json.")
        return []

    latest_round = max(finished_rounds, key=lambda x: int(x) if str(x).isdigit() else 0)
    round_matches = [m for m in matches if str(m.get("round")) == str(latest_round) and m.get("finished")]
    logger.info(f"Exporting recent results for Round {latest_round} ({len(round_matches)} matches)...")

    enriched = []
    for m in round_matches:
        mid = int(m.get("id"))
        home_id = int(m.get("home_id", 0))
        away_id = int(m.get("away_id", 0))

        home_meta = TEAMS_META.get(home_id, {
            "slug": m.get("home", "").lower().replace(" (w)", "").replace(" ", "-"),
            "name_en": m.get("home", "").replace(" (W)", ""),
            "name_he": m.get("home", "").replace(" (W)", ""),
            "color": "#4B5563",
            "crest": f"https://images.fotmob.com/image_resources/logo/teamlogo/{home_id}_small.png"
        })
        away_meta = TEAMS_META.get(away_id, {
            "slug": m.get("away", "").lower().replace(" (w)", "").replace(" ", "-"),
            "name_en": m.get("away", "").replace(" (W)", ""),
            "name_he": m.get("away", "").replace(" (W)", ""),
            "color": "#4B5563",
            "crest": f"https://images.fotmob.com/image_resources/logo/teamlogo/{away_id}_small.png"
        })

        h_score = m.get("home_score", 0)
        a_score = m.get("away_score", 0)
        if h_score > a_score:
            winner = "home"
        elif a_score > h_score:
            winner = "away"
        else:
            winner = "draw"

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

        item = {
            "id": mid,
            "round": str(latest_round),
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
            "home_crest": home_meta.get("crest"),
            "home_score": h_score,

            "away_id": away_id,
            "away_name": away_meta["name_en"],
            "away_name_he": away_meta["name_he"],
            "away_slug": away_meta["slug"],
            "away_color": away_meta["color"],
            "away_crest": away_meta.get("crest"),
            "away_score": a_score,

            "home_xg": None,
            "away_xg": None,
            "home_shots": None,
            "away_shots": None,
            "home_sot": None,
            "away_sot": None,
            "home_possession": None,
            "away_possession": None,
            "home_scorers": [],
            "away_scorers": [],
            "has_deep_stats": False,
        }
        enriched.append(item)

    dest_site = SITE_DATA_DIR / "wsl_recent_results.json"
    with open(dest_site, "w", encoding="utf-8") as f:
        json.dump(enriched, f, indent=2, ensure_ascii=False)
    logger.info(f"✅ Updated {dest_site}")

    dest_assets = ASSETS_DATA_DIR / "wsl_recent_results.json"
    with open(dest_assets, "w", encoding="utf-8") as f:
        json.dump(enriched, f, indent=2, ensure_ascii=False)
    logger.info(f"✅ Updated {dest_assets}")

    return enriched


def export_gold_to_site():
    db_url = os.getenv("DATABASE_URL", "")
    if not db_url:
        raise ValueError("DATABASE_URL is missing in .env")

    clean_db_url = db_url.replace("?pgbouncer=true", "").replace("&pgbouncer=true", "")
    if clean_db_url.startswith("postgres://"):
        clean_db_url = clean_db_url.replace("postgres://", "postgresql+psycopg2://", 1)
    elif clean_db_url.startswith("postgresql://"):
        clean_db_url = clean_db_url.replace("postgresql://", "postgresql+psycopg2://", 1)
    if "sslmode" not in clean_db_url:
        separator = "&" if "?" in clean_db_url else "?"
        clean_db_url += f"{separator}sslmode=require"

    logger.info("Connecting to Supabase PostgreSQL to fetch Gold analytics...")
    engine = create_engine(clean_db_url)

    # 1. Fetch fct_league_standings
    query_standings = """
        SELECT
            league_rank as rk,
            team_name as squad,
            team_slug as slug,
            matches_played as mp,
            wins as w,
            draws as d,
            losses as l,
            goals_for as gf,
            goals_against as ga,
            goal_difference as gd,
            points as pts,
            season,
            points_per_match,
            goals_scored_per_match,
            goals_conceded_per_match
        FROM analytics_analytics.fct_league_standings
        ORDER BY league_rank ASC;
    """
    df_standings = pd.read_sql(query_standings, engine)
    standings_records = df_standings.to_dict(orient="records")

    logger.info(f"Retrieved {len(standings_records)} teams from Gold fct_league_standings.")

    # 2. Write to _data/league_table.json and assets/data/league_table.json
    SITE_DATA_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DATA_DIR.mkdir(parents=True, exist_ok=True)

    dest_site = SITE_DATA_DIR / "league_table.json"
    with open(dest_site, "w", encoding="utf-8") as f:
        json.dump(standings_records, f, indent=2, ensure_ascii=False)
    logger.info(f"✅ Updated {dest_site}")

    dest_assets = ASSETS_DATA_DIR / "league_table.json"
    with open(dest_assets, "w", encoding="utf-8") as f:
        json.dump(standings_records, f, indent=2, ensure_ascii=False)
    logger.info(f"✅ Updated {dest_assets}")

    # 3. Export recent match results for the homepage widget
    export_recent_results_to_site()

    print("🎉 Serving Layer: Site data successfully refreshed from Gold Database Marts & Fixtures!")


if __name__ == "__main__":
    export_gold_to_site()
