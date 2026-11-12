#!/usr/bin/env python3
"""
WSL Data Platform - Master End-to-End Pipeline Runner
====================================================
Orchestrates the entire Data Engineering lifecycle in a single command:
1. Ingest (Extract from API -> Load to Data Lake as Parquet/JSON)
2. Load Raw (Data Lake -> Supabase PostgreSQL 'raw' schema)
3. Transform (dbt build -> Star Schema Facts & Dims + Data Quality Tests)
4. Serve (Gold Database -> Jekyll Site JSONs)

Usage:
    python run_pipeline.py
    python run_pipeline.py --season 2026/2027
"""

import sys
import time
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pipeline.ingest import run_ingest
from pipeline.ingest_match_details import run_match_details_ingest
from pipeline.load_raw import load_lake_to_raw_db
from pipeline.export_to_site import export_gold_to_site
from pipeline.setup_dbt_profile import *


def main():
    start_time = time.time()
    print("=" * 65)
    print("  ⚽ WSL DATA PLATFORM · END-TO-END PIPELINE ORCHESTRATOR")
    print("=" * 65)

    # 1. Ingestion Engine (Extract & Load to Data Lake)
    print("\n[Step 1/4] Ingesting live data from FotMob API into Data Lake...")
    run_ingest(season="2026/2027", upload_lake=True, sync_local_site=True)
    run_match_details_ingest(season="2026/2027", upload_lake=True)

    # 2. Raw Loader (Data Lake -> Postgres raw schema)
    print("\n[Step 2/4] Loading Lake Parquet datasets into Supabase PostgreSQL 'raw'...")
    load_lake_to_raw_db(season="2026/2027")

    # 3. Transformations with dbt (Raw -> Staging -> Gold Facts & Dims + Tests)
    print("\n[Step 3/4] Running dbt build (Transformations & Data Quality Tests)...")
    dbt_dir = PROJECT_ROOT / "dbt_wsl"
    cmd = [sys.executable, "-m", "dbt.cli.main", "build", "--profiles-dir", "."]
    result = subprocess.run(cmd, cwd=str(dbt_dir))
    if result.returncode != 0:
        print("❌ dbt build failed. Halting pipeline.")
        sys.exit(result.returncode)

    # 4. Serving Layer (Gold Database -> Jekyll Site)
    print("\n[Step 4/4] Refreshing Jekyll site datasets from Gold analytics...")
    export_gold_to_site()

    elapsed = round(time.time() - start_time, 2)
    print("\n" + "=" * 65)
    print(f"  🎉 PIPELINE EXECUTION COMPLETED SUCCESSFULLY IN {elapsed}s!")
    print("=" * 65)


if __name__ == "__main__":
    main()
