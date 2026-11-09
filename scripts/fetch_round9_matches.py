#!/usr/bin/env python3
"""
Fetch and Cache FotMob Match Details for WSL Matchweek 9
=========================================================
Downloads detailed match facts, stats, player ratings, and shotmaps
for all completed matches in Round 9, caches them locally, and triggers
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

ROUND_9_MATCHES = {
    "che_eve": {"id": 5981686, "label": "Chelsea vs Everton (1-1)"},
    "mci_whu": {"id": 5981687, "label": "Manchester City vs West Ham United (5-0)"},
    "avl_mun": {"id": 5981685, "label": "Aston Villa vs Manchester United (0-1)"},
    "liv_ars": {"id": 5981683, "label": "Liverpool vs Arsenal (1-2)"},
    "cry_cha": {"id": 5981688, "label": "Crystal Palace vs Charlton (3-2)"},
    "tot_bha": {"id": 5981689, "label": "Tottenham Hotspur vs Brighton (2-1)"},
    "lcl_bir": {"id": 5981684, "label": "London City Lionesses vs Birmingham City (4-1)"}
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
    print(" 📥 Downloading WSL Matchweek 9 Deep Match Details from FotMob")
    print("=" * 65)
    
    success_count = 0
    for key, info in ROUND_9_MATCHES.items():
        mid = info["id"]
        label = info["label"]
        print(f"[*] Fetching: {label} (ID: {mid})...")
        data = fetch_match_details(mid)
        if data:
            dest_raw = MATCHES_CACHE_DIR / f"mw9_{key}_{mid}.json"
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
    print(f" ✨ Done! Successfully downloaded {success_count}/{len(ROUND_9_MATCHES)} matches.")
    print("=" * 65)

    # Now run enrichment
    print("\n[*] Enriching recent results with deep stats...")
    enrich_matchweek()
    print("✓ Enrichment complete!")

if __name__ == "__main__":
    main()

