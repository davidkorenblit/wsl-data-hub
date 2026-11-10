"""
WSL Data Platform - Serving / Export Layer
==========================================
Extracts the latest Gold analytics tables from Supabase PostgreSQL
and updates Jekyll site JSON datasets (_data/league_table.json, etc.).
"""
import os
import sys
import json
import logging
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SITE_DATA_DIR = PROJECT_ROOT / "_data"
ASSETS_DATA_DIR = PROJECT_ROOT / "assets" / "data"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("SiteExporter")


def export_gold_to_site():
    db_url = os.getenv("DATABASE_URL", "")
    if not db_url:
        raise ValueError("DATABASE_URL is missing in .env")

    clean_db_url = db_url.replace("?pgbouncer=true", "").replace("&pgbouncer=true", "")
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

    print("🎉 Serving Layer: Site data successfully refreshed from Gold Database Marts!")


if __name__ == "__main__":
    export_gold_to_site()
