"""
Inspect all matches and goals conceded by Chelsea in 2025/2026 from FotMob
"""
import requests
import json

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

# Fetch Chelsea fixtures
url = "https://www.fotmob.com/api/data/teams?id=258661"
res = requests.get(url, headers=HEADERS, timeout=15)
data = res.json()

fixtures = data.get("fixtures", {}).get("allFixtures", {}).get("fixtures", [])
print(f"Total fixtures found: {len(fixtures)}")

matches_conceded = []
for m in fixtures:
    status = m.get("status", {})
    score = status.get("scoreStr", "")
    # Check if match has finished and Chelsea conceded
    if status.get("finished"):
        home = m.get("home", {})
        away = m.get("away", {})
        is_home = (home.get("id") == 258661)
        chelsea_score = home.get("score") if is_home else away.get("score")
        opp_score = away.get("score") if is_home else home.get("score")
        opp_name = away.get("name") if is_home else home.get("name")
        
        if opp_score is not None and opp_score > 0:
            matches_conceded.append({
                "id": m.get("id"),
                "date": m.get("status", {}).get("utcTime"),
                "tournament": m.get("tournament", {}).get("name"),
                "opponent": opp_name,
                "score": score,
                "chelsea_conceded": opp_score
            })

print(f"\nMatches where Chelsea conceded ({len(matches_conceded)} matches):")
for mc in matches_conceded:
    print(f"{mc['date'][:10]} | {mc['tournament']} | vs {mc['opponent']} | Result: {mc['score']} (conceded {mc['chelsea_conceded']}) | Match ID: {mc['id']}")

with open("_data/chelsea_conceded_matches.json", "w", encoding="utf-8") as f:
    json.dump(matches_conceded, f, ensure_ascii=False, indent=2)
