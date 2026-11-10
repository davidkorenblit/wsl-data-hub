#!/usr/bin/env python3
"""
WSL Data Platform - Unified Ingestion Engine (Extract & Load)
============================================================
Pulls raw fixtures, match results, and standings from FotMob API.
Validates records with Pydantic contracts and persists them into
the Cloudflare / Supabase S3 Data Lake (Bronze Layer in Parquet & JSON).

Usage:
    python pipeline/ingest.py
    python pipeline/ingest.py --season 2026/2027
    python pipeline/ingest.py --season 2025/2026 --no-lake
"""

import os
import sys
import logging
import argparse
from pathlib import Path
from typing import Dict, Any, List, Optional
import pandas as pd

# Add project root to sys.path so imports work smoothly
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from fotmob_api_client import FotMobAPIClient, TEAM_ID_TO_SLUG
from wsl_lake.storage import DataLakeStorage
from pipeline.schemas import MatchRecord, StandingRecord

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("IngestEngine")


def sanitize_season(season_str: str) -> str:
    """Converts '2026/2027' -> '2026_2027' for safe lake partition paths."""
    return season_str.replace("/", "_").replace("-", "_")


def run_ingest(
    season: str = "2026/2027",
    league_id: int = 9227,
    upload_lake: bool = True,
    sync_local_site: bool = True,
):
    season_safe = sanitize_season(season)
    logger.info(f"⚽ Starting WSL Ingestion Pipeline | Season: {season} (League ID: {league_id})")

    # 1. Fetch raw data from FotMob API
    client = FotMobAPIClient()
    logger.info("Fetching raw league payload from FotMob API...")
    raw_payload = client.fetch_league_raw(league_id=league_id, season=season)

    if not raw_payload:
        logger.error("Failed to retrieve league payload from FotMob API. Aborting.")
        sys.exit(1)

    # 2. Extract and Validate League Standings
    raw_table = client.parse_league_table(raw_payload)
    valid_standings: List[Dict[str, Any]] = []
    for row in raw_table:
        try:
            record = StandingRecord(
                rk=row["rk"],
                squad=row["squad"],
                slug=row["slug"],
                mp=row["mp"],
                w=row["w"],
                d=row["d"],
                l=row["l"],
                gf=row["gf"],
                ga=row["ga"],
                gd=row["gd"],
                pts=row["pts"],
                season=season,
            )
            valid_standings.append(record.model_dump())
        except Exception as e:
            logger.warning(f"Standings validation error for {row.get('squad')}: {e}")

    logger.info(f"Validated {len(valid_standings)} team rows for league standings.")
    df_standings = pd.DataFrame(valid_standings)

    # 3. Extract and Validate Matches & Fixtures
    raw_matches = client.parse_league_matches(raw_payload)
    valid_matches: List[Dict[str, Any]] = []
    for m in raw_matches:
        try:
            match_rec = MatchRecord(
                id=m["id"],
                round=m.get("round"),
                date=m.get("date"),
                home=m["home"],
                home_id=m.get("home_id"),
                home_score=m.get("home_score"),
                away=m["away"],
                away_id=m.get("away_id"),
                away_score=m.get("away_score"),
                score=m.get("score"),
                finished=m.get("finished", False),
                started=m.get("started", False),
                reason=m.get("reason"),
                season=season,
            )
            valid_matches.append(match_rec.model_dump())
        except Exception as e:
            logger.warning(f"Match validation error for match ID {m.get('id')}: {e}")

    logger.info(f"Validated {len(valid_matches)} total matches/fixtures.")
    df_matches = pd.DataFrame(valid_matches)

    # 4. Upload to Data Lake (Bronze Layer)
    if upload_lake:
        logger.info("Connecting to Data Lake...")
        try:
            lake = DataLakeStorage()

            # 4a. Upload Raw JSON Snapshot (Immutable Raw Bronze)
            raw_json_key = f"bronze/fotmob/season={season_safe}/raw_league_{league_id}.json"
            lake.upload_json(raw_payload, key=raw_json_key)

            # 4b. Upload Standings as Columnar Parquet
            standings_key = f"bronze/standings/season={season_safe}/standings.parquet"
            lake.upload_parquet(df_standings, key=standings_key)

            # 4c. Upload Matches as Columnar Parquet
            matches_key = f"bronze/matches/season={season_safe}/matches.parquet"
            lake.upload_parquet(df_matches, key=matches_key)

            logger.info("🎉 All Bronze datasets successfully written to Data Lake!")
        except Exception as e:
            logger.error(f"Failed to upload datasets to Data Lake: {e}")
            raise e
    else:
        logger.info("Skipping Lake upload (--no-lake specified).")

    # 5. Backward compatibility: update local site files if requested
    if sync_local_site:
        import json
        site_data_dir = PROJECT_ROOT / "_data"
        site_data_dir.mkdir(parents=True, exist_ok=True)

        if valid_standings:
            with open(site_data_dir / "league_table.json", "w", encoding="utf-8") as f:
                json.dump(valid_standings, f, indent=2, ensure_ascii=False)
            logger.info(f"Updated local {site_data_dir / 'league_table.json'}")

        if valid_matches:
            with open(site_data_dir / "wsl_matches.json", "w", encoding="utf-8") as f:
                json.dump(valid_matches, f, indent=2, ensure_ascii=False)
            logger.info(f"Updated local {site_data_dir / 'wsl_matches.json'}")

    logger.info("✅ Ingestion Pipeline Finished Successfully!")
    return {
        "standings_count": len(valid_standings),
        "matches_count": len(valid_matches),
    }


def main():
    parser = argparse.ArgumentParser(description="WSL Data Platform Ingestion Engine")
    parser.add_argument(
        "--season",
        type=str,
        default="2026/2027",
        help="Target season to ingest (e.g. 2026/2027 or 2025/2026)",
    )
    parser.add_argument(
        "--league-id",
        type=int,
        default=9227,
        help="FotMob League ID for WSL (default: 9227)",
    )
    parser.add_argument(
        "--no-lake",
        action="store_true",
        help="Do not upload to remote Data Lake (local validation only)",
    )
    parser.add_argument(
        "--no-site-sync",
        action="store_true",
        help="Do not update local _data/ files",
    )
    args = parser.parse_args()

    run_ingest(
        season=args.season,
        league_id=args.league_id,
        upload_lake=not args.no_lake,
        sync_local_site=not args.no_site_sync,
    )


if __name__ == "__main__":
    main()
