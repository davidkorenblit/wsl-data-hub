#!/usr/bin/env python3
"""
WSL Data Hub - Matchweek Sync Master Script
===========================================
Synchronizes live/post-matchweek data from FotMob for the WSL (Women's Super League):
1. Downloads full raw league overview (standings, fixtures, results).
2. Updates `_data/league_table.json` and `assets/data/league_table.json`.
3. Updates `_data/wsl_matches.json` with all season fixtures.
4. Generates `_data/wsl_recent_results.json` containing recently completed matches.
5. Prints a clean, formatted terminal summary for immediate review.

Usage:
    python scripts/sync_matchweek.py
    python scripts/sync_matchweek.py --season 2026/2027
    python scripts/sync_matchweek.py --dry-run
"""

import sys
import time
import argparse
from pathlib import Path

# Ensure scripts directory is in path for imports
SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from fotmob_api_client import FotMobAPIClient, TEAM_ID_TO_SLUG
from paths import (
    SITE_DATA_DIR,
    ASSETS_DATA_DIR,
    FOTMOB_LEAGUES_DIR,
    ensure_all_directories
)


def print_banner(title: str, char: str = "="):
    line = char * 64
    print(f"\n{line}\n  {title}\n{line}")


def sync_matchweek(season: str = None, dry_run: bool = False):
    start_time = time.time()
    ensure_all_directories()

    print_banner("⚽ WSL Matchweek Sync Engine · WSL Data Hub", "=")
    print(f"[*] Connecting to FotMob API for WSL (League ID: 9227)...")
    if season:
        print(f"[*] Target Season: {season}")

    client = FotMobAPIClient()
    raw_data = client.fetch_league_raw(league_id=9227, season=season)

    if not raw_data:
        print("\n[!] ERROR: Failed to retrieve league data from FotMob.")
        print("    Please check network connection or verify FotMob API availability.")
        sys.exit(1)

    # 1. Parse Table
    table = client.parse_league_table(raw_data)
    if not table:
        print("[!] Warning: Could not extract league table standings.")

    # 2. Parse Matches
    all_matches = client.parse_league_matches(raw_data)
    finished_matches = [m for m in all_matches if m.get("finished")]

    # Group completed matches by round to find the latest completed round
    latest_round = None
    latest_round_matches = []
    if finished_matches:
        rounds_with_finished = sorted(
            list({m.get("round") for m in finished_matches if m.get("round") is not None}),
            reverse=True
        )
        if rounds_with_finished:
            latest_round = rounds_with_finished[0]
            latest_round_matches = [m for m in finished_matches if m.get("round") == latest_round]

    duration = round(time.time() - start_time, 2)

    # Display Results
    if latest_round_matches:
        print_banner(f"📌 תוצאות המחזור האחרון (מחזור {latest_round})", "-")
        for m in latest_round_matches:
            date_str = m.get("date", "")[:10] if m.get("date") else ""
            score = m.get("score", "vs")
            print(f"   • {m.get('home'):<24} {score:^7} {m.get('away'):<24} ({date_str})")
    elif finished_matches:
        print_banner(f"📌 משחקים אחרונים שהסתיימו ({len(finished_matches)} סה\"כ)", "-")
        for m in finished_matches[-6:]:
            date_str = m.get("date", "")[:10] if m.get("date") else ""
            print(f"   • {m.get('home'):<24} {m.get('score', 'vs'):^7} {m.get('away'):<24} ({date_str})")
    else:
        print("\n[*] עדיין לא הסתיימו משחקים רשמיים בעונה זו (טרום עונה / תחילת משחקים).")

    # Display Top Standings
    if table:
        print_banner("🏆 תמונת צמרת הטבלה (Top 6)", "-")
        print(f"   {'#':<3} {'מועדון':<24} {'משחקים':<8} {'הפרש':<7} {'נקודות':<6}")
        print(f"   {'-'*3} {'-'*24} {'-'*8} {'-'*7} {'-'*6}")
        for row in table[:6]:
            gd_str = f"+{row['gd']}" if row['gd'] > 0 else str(row['gd'])
            print(f"   {row['rk']:<3} {row['squad']:<24} {row['mp']:<8} {gd_str:<7} {row['pts']:<6}")

    # File Writing
    if dry_run:
        print("\n[!] DRY RUN MODE: No files were modified.")
    else:
        # Save Raw JSON
        raw_path = FOTMOB_LEAGUES_DIR / "league_9227_wsl_overview.json"
        client.save_json(raw_data, raw_path)

        # Save Standings
        if table:
            client.save_json(table, SITE_DATA_DIR / "league_table.json")
            client.save_json(table, ASSETS_DATA_DIR / "league_table.json")

        # Save Matches & Recent Results
        if all_matches:
            client.save_json(all_matches, SITE_DATA_DIR / "wsl_matches.json")
            recent_output = latest_round_matches if latest_round_matches else finished_matches
            client.save_json(recent_output, SITE_DATA_DIR / "wsl_recent_results.json")

        print_banner("💾 קבצים שעודכנו בהצלחה באתר", "-")
        print(f"   ✓ {SITE_DATA_DIR / 'league_table.json'}")
        print(f"   ✓ {ASSETS_DATA_DIR / 'league_table.json'}")
        print(f"   ✓ {SITE_DATA_DIR / 'wsl_matches.json'} ({len(all_matches)} משחקים)")
        print(f"   ✓ {SITE_DATA_DIR / 'wsl_recent_results.json'} ({len(recent_output)} תוצאות)")
        print(f"   ✓ {raw_path}")

    print_banner(f"✨ הסינכרון הושלם בהצלחה תוך {duration} שניות!", "=")
    print("👉 כעת ניתן לבצע git commit & push כדי להעלות את הנתונים לאתר החי.\n")


def main():
    parser = argparse.ArgumentParser(
        description="WSL Matchweek Sync - Pull live match results and standings from FotMob"
    )
    parser.add_argument(
        "--season",
        type=str,
        default=None,
        help="Season string (e.g. 2026/2027). Defaults to current active season on FotMob."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run fetch and display summary without modifying local JSON files."
    )
    args = parser.parse_args()

    sync_matchweek(season=args.season, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
