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
    if clean_db_url.startswith("postgres://"):
        clean_db_url = clean_db_url.replace("postgres://", "postgresql+psycopg2://", 1)
    elif clean_db_url.startswith("postgresql://"):
        clean_db_url = clean_db_url.replace("postgresql://", "postgresql+psycopg2://", 1)
    if "sslmode" not in clean_db_url:
        separator = "&" if "?" in clean_db_url else "?"
        clean_db_url += f"{separator}sslmode=require"

    logger.info("Connecting to Data Lake...")
    lake = DataLakeStorage()

    # 1. Download Parquet from Data Lake
    datasets = [
        ("standings", f"bronze/standings/season={season_safe}/standings.parquet", True),
        ("matches", f"bronze/matches/season={season_safe}/matches.parquet", True),
        ("match_player_stats", f"bronze/match_player_stats/season={season_safe}/match_player_stats.parquet", False),
        ("shots", f"bronze/shots/season={season_safe}/shots.parquet", False),
    ]

    loaded_dfs = {}
    for table_name, key, required in datasets:
        logger.info(f"Downloading {key} from Data Lake...")
        try:
            loaded_dfs[table_name] = lake.download_parquet(key=key)
        except Exception as e:
            if required:
                raise
            logger.warning(f"Optional dataset {key} not found in Lake yet ({e}); skipping.")

    # 2. Connect to Supabase Postgres
    logger.info("Connecting to Supabase PostgreSQL...")
    engine = create_engine(clean_db_url)

    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS raw;"))
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS analytics;"))
        for table_name in loaded_dfs:
            # Truncate existing tables so dependent views (dbt staging) aren't dropped
            conn.execute(text(f"""
                DO $$
                BEGIN
                    IF EXISTS (SELECT FROM pg_tables WHERE schemaname = 'raw' AND tablename = '{table_name}') THEN
                        TRUNCATE TABLE raw.{table_name};
                    END IF;
                END $$;
            """))

    # 3. Load into 'raw' schema
    for table_name, df in loaded_dfs.items():
        logger.info(f"Writing {len(df)} rows to raw.{table_name}...")
        df.to_sql(table_name, engine, schema="raw", if_exists="append", index=False)

    logger.info("🎉 Raw data successfully placed onto the 'raw' shelf in PostgreSQL!")


if __name__ == "__main__":
    load_lake_to_raw_db()
