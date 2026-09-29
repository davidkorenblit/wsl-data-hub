"""
Deep FotMob Extraction:
1. Brighton 2026/27 Matches 1-4 granular stats
2. Brighton 2025/26 Season Totals (Vidosic)
3. Real Sociedad 2025/26 Season Totals (Ruiz)
"""

import sys
import io
import json
import requests
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

def get_json(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            return r.json()
    except Exception as e:
        print(f"Error {url}: {e}")
    return None

def analyze_match(mid, round_no):
    data = get_json(f"https://www.fotmob.com/api/data/matchDetails?matchId={mid}")
    if not data:
        return None
    content = data.get("content", {})
    stats = content.get("stats", {})
    periods = stats.get("Periods", {}).get("All", {})
    stats_items = periods.get("stats", [])
    
    extracted = {}
    for group in stats_items:
        for item in group.get("stats", []):
            extracted[item.get("title")] = item.get("stats")

    lineup = content.get("lineup", {})
    home_t = lineup.get("homeTeam", {})
    away_t = lineup.get("awayTeam", {})
    
    header = data.get("header", {})
    teams = header.get("teams", [])
    home_name = teams[0].get("name") if len(teams) > 0 else "Home"
    away_name = teams[1].get("name") if len(teams) > 1 else "Away"
    score = header.get("status", {}).get("scoreStr", "")

    return {
        "round": round_no,
        "match": f"{home_name} {score} {away_name}",
        "home_formation": home_t.get("formation"),
        "away_formation": away_t.get("formation"),
        "stats": extracted
    }

def main():
    match_ids = [
        (1, 5981533),
        (2, 5981636),
        (3, 5981645),
        (4, 5981649)
    ]
    
    results = []
    print("=== PULLING BRIGHTON 2026/27 ROUNDS 1-4 STATS FROM FOTMOB ===")
    for r, mid in match_ids:
        res = analyze_match(mid, r)
        if res:
            results.append(res)
            print(f"\n--- Round {r}: {res['match']} ---")
            print(f"Home Formation: {res['home_formation']} | Away Formation: {res['away_formation']}")
            s = res['stats']
            for k in [
                'Expected goals (xG)', 'Total shots', 'Shots on target', 'Big chances',
                'Big chances missed', 'Ball possession', 'Accurate passes', 'Pass accuracy',
                'Touches in opposition box', 'Corners', 'Offsides', 'Tackles won', 'Interceptions',
                'Clearances', 'Fouls committed'
            ]:
                if k in s:
                    print(f"  {k}: {s[k]}")

    # Save to JSON
    with open("scratch_brighton_mw1_4_fotmob.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    # Now let's inspect season stats for Brighton and Real Sociedad
    print("\n=== PULLING TEAM STATS FROM FOTMOB API ===")
    bha_team = get_json("https://www.fotmob.com/api/data/teams?id=231505")
    rso_team = get_json("https://www.fotmob.com/api/data/teams?id=858300")
    
    # Check stats tabs
    print("BHA stats tab keys:", bha_team.get("stats", {}).keys() if bha_team else "None")
    print("RSO stats tab keys:", rso_team.get("stats", {}).keys() if rso_team else "None")

if __name__ == "__main__":
    main()
