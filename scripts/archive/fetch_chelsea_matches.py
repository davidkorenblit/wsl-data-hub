import requests
import json

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

# Fetch WSL 2025/2026 league overview and fixtures
url = "https://www.fotmob.com/api/data/leagues?id=9227&season=2025%2F2026"
res = requests.get(url, headers=HEADERS, timeout=15)
data = res.json()

matches = data.get("matches", {}).get("allMatches", [])
print(f"Total league matches found: {len(matches)}")

chelsea_matches = []
for m in matches:
    h = m.get("home", {})
    a = m.get("away", {})
    if h.get("id") == 258661 or a.get("id") == 258661:
        status = m.get("status", {})
        chelsea_matches.append({
            "id": m.get("id"),
            "round": m.get("round"),
            "home": h.get("name"),
            "away": a.get("name"),
            "score": status.get("scoreStr"),
            "finished": status.get("finished"),
            "time": status.get("utcTime")
        })

print(f"Chelsea matches found: {len(chelsea_matches)}")
with open("_data/chelsea_2025_26_matches.json", "w", encoding="utf-8") as f:
    json.dump(chelsea_matches, f, ensure_ascii=False, indent=2)

for cm in chelsea_matches:
    print(f"Round {cm['round']} | {cm['home']} vs {cm['away']} | {cm['score']} | ID: {cm['id']}")
