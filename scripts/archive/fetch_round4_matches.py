import json
import time
import requests
from pathlib import Path

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

def fetch_with_retry(url, retries=5, delay=2):
    for i in range(retries):
        try:
            res = requests.get(url, headers=HEADERS, timeout=15)
            if res.status_code == 200:
                return res.json()
            print(f"Status {res.status_code} for {url}, retrying...")
        except Exception as e:
            print(f"Attempt {i+1} failed: {e}")
        time.sleep(delay)
    return None

def get_match_data(mid, filename):
    p = Path(filename)
    if p.exists():
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    print(f"Fetching match {mid}...")
    data = fetch_with_retry(f"https://www.fotmob.com/api/data/matchDetails?matchId={mid}")
    if data:
        with open(p, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    return data

# Match IDs
che_ars = get_match_data(5981654, "scratch_che_ars.json")
tot_avl = get_match_data(5981653, "scratch_tot_avl.json")
lcl_bha = get_match_data(5981649, "scratch_lcl_bha.json")
mun_whu = get_match_data(5981650, "scratch_mun_whu.json")
bir_cry = get_match_data(5981651, "scratch_bir_cry.json")

print("\n--- STATUS OF DOWNLOADS ---")
print("Chelsea vs Arsenal:", bool(che_ars))
print("Spurs vs Villa:", bool(tot_avl))
print("LCL vs Brighton:", bool(lcl_bha))
print("Man Utd vs West Ham:", bool(mun_whu))
print("Birmingham vs Palace:", bool(bir_cry))
