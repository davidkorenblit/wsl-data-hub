"""
Extract FotMob Official Data for Brighton (Vidosic & Ruiz) and Real Sociedad (Ruiz)
==================================================================================
"""

import sys
import io
import json
import requests
from pathlib import Path

# Force UTF-8 on Windows stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

def fetch_json(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            return r.json()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return None

def main():
    print("--- 1. Fetching Team Data ---")
    bha = fetch_json("https://www.fotmob.com/api/data/teams?id=231505")
    rso = fetch_json("https://www.fotmob.com/api/data/teams?id=858300")

    print("\n--- Brighton Coach History (Recent) ---")
    coaches = bha.get("overview", {}).get("coachHistory", [])
    for c in coaches[-5:]:
        print(f"  {c.get('name')} | from: {c.get('startDate')} | to: {c.get('endDate')}")

    print("\n--- Real Sociedad Coach History (Recent) ---")
    rso_coaches = rso.get("overview", {}).get("coachHistory", [])
    for c in rso_coaches[-5:]:
        print(f"  {c.get('name')} | from: {c.get('startDate')} | to: {c.get('endDate')}")

    # Inspect Brighton current season stats in overview / stats
    bha_overview = bha.get("overview", {})
    print("\n--- Brighton Current Season Overview ---")
    print("Season:", bha_overview.get("season"))
    print("Selected Season:", bha_overview.get("selectedSeason"))
    last_lineup = bha_overview.get("lastLineupStats", {})
    print("Last Lineup Stats:", json.dumps(last_lineup, indent=2))

    # Pull match details for Brighton's MW1-MW4
    print("\n--- 2. Fetching Brighton 2026/27 Matches Details ---")
    # Match IDs from wsl_matches:
    # Round 1: Arsenal vs Brighton (5981628) or similar, let's find all Brighton matches in wsl_matches
    wsl_matches_path = Path("_data/wsl_matches.json")
    if wsl_matches_path.exists():
        with open(wsl_matches_path, "r", encoding="utf-8") as f:
            all_matches = json.load(f)
        bha_matches = [m for m in all_matches if (m.get("home_id") == 231505 or m.get("away_id") == 231505) and m.get("finished")]
        print(f"Found {len(bha_matches)} finished Brighton matches in 2026/27:")
        for m in bha_matches:
            mid = m.get("id")
            m_data = fetch_json(f"https://www.fotmob.com/api/data/matchDetails?matchId={mid}")
            if not m_data:
                continue
            content = m_data.get("content", {})
            stats = content.get("stats", {})
            periods = stats.get("Periods", {}).get("All", {})
            stats_items = periods.get("stats", [])
            
            # Extract key stats
            extracted = {}
            for group in stats_items:
                for item in group.get("stats", []):
                    title = item.get("title")
                    val = item.get("stats")
                    extracted[title] = val

            lineup = content.get("lineup", {})
            home_t = lineup.get("homeTeam", {})
            away_t = lineup.get("awayTeam", {})
            is_bha_home = m.get("home_id") == 231505
            bha_t = home_t if is_bha_home else away_t
            
            print(f"\n>> Round {m.get('round')}: {m.get('home')} {m.get('score')} {m.get('away')}")
            print(f"   Formation: {bha_t.get('formation')}")
            print(f"   xG: {extracted.get('Expected goals (xG)')}")
            print(f"   Big chances: {extracted.get('Big chances')}")
            print(f"   Big chances missed: {extracted.get('Big chances missed')}")
            print(f"   Total shots: {extracted.get('Total shots')}")
            print(f"   Shots on target: {extracted.get('Shots on target')}")
            print(f"   Possession: {extracted.get('Ball possession')}")
            print(f"   Accurate passes: {extracted.get('Accurate passes')}")
            print(f"   Pass accuracy: {extracted.get('Pass accuracy')}")
            print(f"   Tackles won: {extracted.get('Tackles won')}")
            print(f"   Interceptions: {extracted.get('Interceptions')}")

if __name__ == "__main__":
    main()
