import json
import time
from pathlib import Path
import requests

RAW_MATCHES_DIR = Path("data/raw/fotmob/matches")
RAW_MATCHES_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

# The 5 WSL matches for LCL
LCL_MATCHES = {
    5981531: "mw1_lcl_mun_5981531.json",
    5981634: "mw2_whu_lcl_5981634.json",
    5981642: "mw3_cha_lcl_5981642.json",
    5981649: "mw4_lcl_bha_5981649.json",
    5981655: "mw5_tot_lcl_5981655.json"
}

for mid, fname in LCL_MATCHES.items():
    dest = RAW_MATCHES_DIR / fname
    if dest.exists() and dest.stat().st_size > 1000:
        print(f"Match {mid} ({fname}) already cached.")
        continue
    url = f"https://www.fotmob.com/api/data/matchDetails?matchId={mid}"
    print(f"Fetching {url} -> {fname}...")
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        if r.status_code == 200:
            with open(dest, "w", encoding="utf-8") as f:
                f.write(r.text)
            print(f"Successfully saved {fname} ({len(r.text)} bytes)")
        else:
            print(f"Error {r.status_code} for {mid}")
    except Exception as e:
        print(f"Exception for {mid}: {e}")
    time.sleep(1.2)

print("Done fetching LCL matches.")
