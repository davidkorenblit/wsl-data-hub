"""
WSL Data Platform - Historical Data Lake Backfill
=================================================
Scans all existing local raw JSON and CSV datasets across the project
and migrates them into organized columnar Parquet and JSON partitions
in the Supabase S3 Data Lake (Bronze & Silver Layers).
Includes idempotency checks to skip files already uploaded.
"""
import os
import sys
import json
import logging
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from wsl_lake.storage import DataLakeStorage

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("LakeBackfill")


def backfill_all_local_data():
    logger.info("🚀 Starting Comprehensive Data Lake Backfill...")
    lake = DataLakeStorage()
    raw_dir = PROJECT_ROOT / "data" / "raw"

    # Pre-fetch all existing keys in the Data Lake to prevent redundant re-uploads
    try:
        existing_keys = set(lake.list_objects())
        logger.info(f"🔍 Found {len(existing_keys)} existing objects already in the Data Lake.")
    except Exception as e:
        logger.warning(f"Could not retrieve existing keys list: {e}. Proceeding without skip cache.")
        existing_keys = set()

    uploaded_count = 0
    skipped_count = 0

    # 1. Backfill Squad Stats (CSVs -> Parquet in Lake)
    squads_dir = raw_dir / "squads"
    if squads_dir.exists():
        for csv_file in squads_dir.glob("*.csv"):
            key = f"bronze/squad_stats/{csv_file.stem}.parquet"
            if key in existing_keys:
                skipped_count += 1
                continue
            try:
                df = pd.read_csv(csv_file)
                lake.upload_parquet(df, key=key)
                uploaded_count += 1
                existing_keys.add(key)
            except Exception as e:
                logger.warning(f"Failed to backfill {csv_file.name}: {e}")

    # 2. Backfill Player FBref Stats (CSVs -> Parquet in Lake)
    players_dir = raw_dir / "players"
    if players_dir.exists():
        for csv_file in players_dir.glob("*.csv"):
            key = f"bronze/player_stats/{csv_file.stem}.parquet"
            if key in existing_keys:
                skipped_count += 1
                continue
            try:
                df = pd.read_csv(csv_file)
                lake.upload_parquet(df, key=key)
                uploaded_count += 1
                existing_keys.add(key)
            except Exception as e:
                logger.warning(f"Failed to backfill {csv_file.name}: {e}")

    # 3. Backfill FotMob Raw Teams JSONs
    fotmob_teams_dir = raw_dir / "fotmob" / "teams"
    if fotmob_teams_dir.exists():
        for json_file in fotmob_teams_dir.glob("*.json"):
            key = f"bronze/fotmob/teams/{json_file.name}"
            if key in existing_keys:
                skipped_count += 1
                continue
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                lake.upload_json(data, key=key)
                uploaded_count += 1
                existing_keys.add(key)
            except Exception as e:
                logger.warning(f"Failed to backfill {json_file.name}: {e}")

    # 4. Backfill FotMob Player Cache JSONs
    fotmob_players_dir = raw_dir / "fotmob" / "players" / "cache"
    if fotmob_players_dir.exists():
        for json_file in fotmob_players_dir.glob("*.json"):
            key = f"bronze/fotmob/players/{json_file.name}"
            if key in existing_keys:
                skipped_count += 1
                continue
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                lake.upload_json(data, key=key)
                uploaded_count += 1
                existing_keys.add(key)
            except Exception as e:
                logger.warning(f"Failed to backfill {json_file.name}: {e}")

    # 5. Backfill Existing Squad JSONs from _data/squads/
    site_squads_dir = PROJECT_ROOT / "_data" / "squads"
    if site_squads_dir.exists():
        for json_file in site_squads_dir.glob("*.json"):
            key = f"bronze/squads_registry/{json_file.name}"
            if key in existing_keys:
                skipped_count += 1
                continue
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                lake.upload_json(data, key=key)
                uploaded_count += 1
                existing_keys.add(key)
            except Exception as e:
                logger.warning(f"Failed to backfill {json_file.name}: {e}")

    logger.info(
        f"🎉 Backfill Complete! Uploaded {uploaded_count} new datasets, "
        f"skipped {skipped_count} already existing in the Cloud Data Lake."
    )
    return uploaded_count


if __name__ == "__main__":
    backfill_all_local_data()
