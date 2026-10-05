#!/usr/bin/env python3
"""
Fetch and Cache FotMob Match Details for WSL Matchweek 5
=========================================================
Downloads detailed match facts, stats, player ratings, and shotmaps
for all completed matches in Round 5.
"""

import json
import time
import requests
from pathlib import Path

# Windows console UTF-8 support
import sys
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SCRIPTS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPTS_DIR.parent
MATCHES_CACHE_DIR = PROJECT_ROOT / "data" / "raw" / "fotmob" / "matches"
MATCHES_CACHE_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

# Round 5 matches mapping: slug -> matchId
ROUND_5_MATCHES = {
    "mun_liv": {"id": 5981656, "label": "Manchester United vs Liverpool (1-0)"},
    "avl_cry": {"id": 5981657, "label": "Aston Villa vs Crystal Palace (1-1)"},
    "bha_cha": {"id": 5981658, "label": "Brighton vs Charlton (5-1)"},
    "eve_bir": {"id": 5981659, "label": "Everton vs Birmingham City (2-1)"},
    "tot_lcl": {"id": 5981655, "label": "Tottenham Hotspur vs London City Lionesses (1-6)"},
    "whu_che": {"id": 5981660, "label": "West Ham United vs Chelsea (0-3)"},
    "mci_ars": {"id": 5981661, "label": "Manchester City vs Arsenal (4-2)"}
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
    print(" 📥 Downloading WSL Matchweek 5 Deep Match Details from FotMob")
    print("=" * 65)
    
    success_count = 0
    for key, info in ROUND_5_MATCHES.items():
        mid = info["id"]
        label = info["label"]
        print(f"[*] Fetching: {label} (ID: {mid})...")
        data = fetch_match_details(mid)
        if data:
            # Save to raw matches cache
            dest_raw = MATCHES_CACHE_DIR / f"mw5_{key}_{mid}.json"
            with open(dest_raw, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            # Save to root scratch file for easy script inspection
            scratch_path = PROJECT_ROOT / f"scratch_{key}.json"
            with open(scratch_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                
            print(f"   ✓ Saved {dest_raw.name} and scratch_{key}.json")
            success_count += 1
        else:
            print(f"   ✗ Failed to download {label}")
        time.sleep(0.5)

    print("\n" + "=" * 65)
    print(f" ✨ Done! Successfully downloaded {success_count}/{len(ROUND_5_MATCHES)} matches.")
    print("=" * 65)

if __name__ == "__main__":
    main()
