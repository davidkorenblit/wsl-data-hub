import json
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

matches = {
    "che_ars": 5981654,
    "tot_avl": 5981653,
    "lcl_bha": 5981649,
    "mun_whu": 5981650,
    "bir_cry": 5981651,
    "liv_eve": 5981652,
    "cha_mci": 5981648
}

for name, mid in matches.items():
    url = f"https://www.fotmob.com/api/data/matchDetails?matchId={mid}"
    res = requests.get(url, headers=HEADERS, timeout=15)
    if res.status_code == 200:
        with open(f"scratch_{name}.json", "w", encoding="utf-8") as f:
            json.dump(res.json(), f, ensure_ascii=False, indent=2)
        print(f"Saved scratch_{name}.json")
    else:
        print(f"Failed {name} ({mid})")
