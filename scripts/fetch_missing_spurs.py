import requests
import json
import time
from pathlib import Path

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

missing_matches = [
    ("mw1_tot_whu", 5981534),
    ("mw2_liv_tot", 5981638),
    ("mw3_cry_tot", 5981646),
    ("mw4_tot_avl", 5981653),
]

out_dir = Path("data/raw/fotmob/matches")
out_dir.mkdir(parents=True, exist_ok=True)

for name, mid in missing_matches:
    url = f"https://www.fotmob.com/api/data/matchDetails?matchId={mid}"
    print(f"Fetching {name} ({mid})...")
    try:
        r = requests.get(url, headers=headers, timeout=15)
        if r.status_code == 200:
            with open(out_dir / f"{name}_{mid}.json", "w", encoding="utf-8") as f:
                json.dump(r.json(), f, ensure_ascii=False, indent=2)
            print(f"  ✓ Saved {name}_{mid}.json")
        else:
            print(f"  ✗ Status {r.status_code}")
    except Exception as e:
        print(f"  ✗ Error {e}")
    time.sleep(1)

print("Done fetching missing Spurs matches.")

