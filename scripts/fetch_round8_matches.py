#!/usr/bin/env python3
"""
Fetch and Cache FotMob Match Details for WSL Matchweek 8
=========================================================
Downloads detailed match facts, stats, player ratings, and shotmaps
for all completed matches in Round 8, caches them locally, and triggers
enrichment for Jekyll front-end presentation.
"""

import json
import time
import requests
from pathlib import Path
import sys

# Windows console UTF-8 support
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SCRIPTS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPTS_DIR.parent
MATCHES_CACHE_DIR = PROJECT_ROOT / "data" / "raw" / "fotmob" / "matches"
MATCHES_CACHE_DIR.mkdir(parents=True, exist_ok=True)

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from enrich_recent_results import enrich_matchweek

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

ROUND_8_MATCHES = {
    "eve_mun": {"id": 5981676, "label": "Everton vs Manchester United (0-0)"},
    "ars_avl": {"id": 5981677, "label": "Arsenal vs Aston Villa (1-1)"},
    "lcl_mci": {"id": 5981681, "label": "London City Lionesses vs Manchester City (1-2)"},
    "bir_tot": {"id": 5981678, "label": "Birmingham City vs Tottenham Hotspur (1-4)"},
    "bha_cry": {"id": 5981679, "label": "Brighton vs Crystal Palace (2-1)"},
    "whu_liv": {"id": 5981682, "label": "West Ham United vs Liverpool (4-1)"},
    "cha_che": {"id": 5981680, "label": "Charlton vs Chelsea (0-6)"}
}

def fetch_match_details(match_id: int, retries: int = 3, delay: float = 1.5):
    url = f"https://www.fotmob.com/api/data/matchDetails?matchId={match_id}"
    for attempt in range(1, retries + 1):
        try:
            res = requests.get(url, headers=HEADERS, timeout=15)
            if res.status_code == 200:
                return res.json()
            print(f"   [!] Status {res.status_code} for match {match_id} (attempt {attempt}/{retries})")
        except Exception as e:
            print(f"   [!] Error fetching match {match_id}: {e} (attempt {attempt}/{retries})")
        time.sleep(delay)
    return None

def main():
    print("=" * 65)
    print(" 📥 Downloading WSL Matchweek 8 Deep Match Details from FotMob")
    print("=" * 65)
    
    success_count = 0
    for key, info in ROUND_8_MATCHES.items():
        mid = info["id"]
        label = info["label"]
        print(f"[*] Fetching: {label} (ID: {mid})...")
        data = fetch_match_details(mid)
        if data:
            dest_raw = MATCHES_CACHE_DIR / f"mw8_{key}_{mid}.json"
            with open(dest_raw, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            scratch_path = PROJECT_ROOT / f"scratch_{key}.json"
            with open(scratch_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                
            print(f"   ✓ Saved {dest_raw.name} and scratch_{key}.json")
            success_count += 1
        else:
            print(f"   ✗ Failed to download {label}")
        time.sleep(0.5)

    print("\n" + "=" * 65)
    print(f" ✨ Done! Successfully downloaded {success_count}/{len(ROUND_8_MATCHES)} matches.")
    print("=" * 65)

    # Now run enrichment
    print("\n[*] Enriching recent results with deep stats...")
    enrich_matchweek()
    print("✓ Enrichment complete!")

if __name__ == "__main__":
    main()
