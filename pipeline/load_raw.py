"""
WSL Data Platform - Lake to Warehouse Raw Loader
================================================
Reads raw Bronze Parquet datasets from the Data Lake and loads them
into the PostgreSQL 'raw' schema in Supabase.
"""
import os
import sys
import logging
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from wsl_lake.storage import DataLakeStorage

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("RawLoader")


def load_lake_to_raw_db(season: str = "2026/2027"):
    season_safe = season.replace("/", "_").replace("-", "_")
    db_url = os.getenv("DATABASE_URL", "")
    if not db_url:
        raise ValueError("DATABASE_URL is missing in .env")

    # Sanitize for psycopg2/SQLAlchemy: strip pgbouncer parameter which is rejected by libpq
    clean_db_url = db_url.replace("?pgbouncer=true", "").replace("&pgbouncer=true", "")
    if "sslmode" not in clean_db_url:
        separator = "&" if "?" in clean_db_url else "?"
        clean_db_url += f"{separator}sslmode=require"

    logger.info("Connecting to Data Lake...")
    lake = DataLakeStorage()

    # 1. Download Parquet from Data Lake
    standings_key = f"bronze/standings/season={season_safe}/standings.parquet"
    matches_key = f"bronze/matches/season={season_safe}/matches.parquet"

    logger.info(f"Downloading {standings_key} from Data Lake...")
    df_standings = lake.download_parquet(key=standings_key)

    logger.info(f"Downloading {matches_key} from Data Lake...")
    df_matches = lake.download_parquet(key=matches_key)

    # 2. Connect to Supabase Postgres
    logger.info("Connecting to Supabase PostgreSQL...")
    engine = create_engine(clean_db_url)

    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS raw;"))
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS analytics;"))
        # Truncate existing tables so dependent views (dbt staging) aren't dropped
        conn.execute(text("""
            DO $$
            BEGIN
                IF EXISTS (SELECT FROM pg_tables WHERE schemaname = 'raw' AND tablename = 'standings') THEN
                    TRUNCATE TABLE raw.standings;
                END IF;
                IF EXISTS (SELECT FROM pg_tables WHERE schemaname = 'raw' AND tablename = 'matches') THEN
                    TRUNCATE TABLE raw.matches;
                END IF;
            END $$;
        """))

    # 3. Load into 'raw' schema
    logger.info(f"Writing {len(df_standings)} rows to raw.standings...")
    df_standings.to_sql("standings", engine, schema="raw", if_exists="append", index=False)

    logger.info(f"Writing {len(df_matches)} rows to raw.matches...")
    df_matches.to_sql("matches", engine, schema="raw", if_exists="append", index=False)

    logger.info("🎉 Raw data successfully placed onto the 'raw' shelf in PostgreSQL!")


if __name__ == "__main__":
    load_lake_to_raw_db()
