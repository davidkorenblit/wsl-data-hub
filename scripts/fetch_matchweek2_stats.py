#!/usr/bin/env python3
"""
Fetch detailed match stats for WSL Round 2 from FotMob:
- Arsenal vs Crystal Palace (5981639)
- Man United vs Chelsea (5981635)
- Liverpool vs Tottenham (5981638)
- West Ham vs London City Lionesses (5981634)
"""
import sys
import json
import requests

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

MATCHES = {
    "Arsenal vs Crystal Palace": 5981639,
    "Man United vs Chelsea": 5981635,
    "Liverpool vs Tottenham": 5981638,
    "West Ham vs LCL": 5981634
}

def fetch_match(match_id):
    url = f"https://www.fotmob.com/api/data/matchDetails?matchId={match_id}"
    res = requests.get(url, headers=HEADERS, timeout=15)
    if res.status_code == 200:
        return res.json()
    print(f"Failed to fetch {match_id}: status {res.status_code}")
    return None

def analyze_arsenal_palace(data):
    print("\n" + "="*50)
    print("🔴 ARSENAL 0 - 0 CRYSTAL PALACE")
    print("="*50)
    content = data.get("content", {})
    stats = content.get("stats", {})
    # Look for Periods/All stats
    periods = stats.get("Periods", {})
    all_stats = periods.get("All", {}).get("stats", [])
    
    for grp in all_stats:
        title = grp.get("title")
        print(f"\n--- {title} ---")
        for item in grp.get("stats", []):
            print(f"{item.get('title')}: {item.get('stats')}")
            
    # Lineup / Player ratings & Goalkeeper
    lineup = content.get("lineup", {})
    for team_key in ["homeTeam", "awayTeam"]:
        team = lineup.get(team_key, {})
        team_name = team.get("name")
        print(f"\nSquad/Rating for {team_name}:")
        players = team.get("players", [])
        for line in players:
            for p in line:
                rating = p.get("rating", {}).get("num", "-")
                name = p.get("name")
                pos = p.get("role")
                stats_p = p.get("stats", {})
                print(f"  • {name} ({pos}) - Rating: {rating}")

def analyze_chelsea_united(data):
    print("\n" + "="*50)
    print("🔵 MANCHESTER UNITED 0 - 5 CHELSEA")
    print("="*50)
    content = data.get("content", {})
    stats = content.get("stats", {})
    all_stats = stats.get("Periods", {}).get("All", {}).get("stats", [])
    for grp in all_stats:
        title = grp.get("title")
        print(f"\n--- {title} ---")
        for item in grp.get("stats", []):
            print(f"{item.get('title')}: {item.get('stats')}")
            
    # Goals / Scorers
    header = data.get("header", {})
    events = content.get("matchFacts", {}).get("events", {}).get("events", [])
    print("\nGoals & Events:")
    for ev in events:
        if ev.get("type") == "Goal":
            print(f"  ⚽ {ev.get('time')}' {ev.get('player', {}).get('name')} (Assist: {ev.get('assistStr', 'None')})")

def analyze_liverpool_spurs(data):
    print("\n" + "="*50)
    print("🔴 LIVERPOOL 1 - 1 TOTTENHAM")
    print("="*50)
    content = data.get("content", {})
    stats = content.get("stats", {})
    all_stats = stats.get("Periods", {}).get("All", {}).get("stats", [])
    for grp in all_stats:
        title = grp.get("title")
        print(f"\n--- {title} ---")
        for item in grp.get("stats", []):
            print(f"{item.get('title')}: {item.get('stats')}")

def analyze_lcl_westham(data):
    print("\n" + "="*50)
    print("🦁 WEST HAM 2 - 1 LONDON CITY LIONESSES")
    print("="*50)
    content = data.get("content", {})
    stats = content.get("stats", {})
    all_stats = stats.get("Periods", {}).get("All", {}).get("stats", [])
    for grp in all_stats:
        title = grp.get("title")
        print(f"\n--- {title} ---")
        for item in grp.get("stats", []):
            print(f"{item.get('title')}: {item.get('stats')}")
            
    # LCL players stats
    lineup = content.get("lineup", {})
    away = lineup.get("awayTeam", {})
    print(f"\nLCL Lineup & Stats:")
    for line in away.get("players", []):
        for p in line:
            name = p.get("name")
            role = p.get("role")
            rating = p.get("rating", {}).get("num", "-")
            print(f"  • {name} ({role}) - Rating: {rating}")

def main():
    print("Fetching match details from FotMob...")
    for name, mid in MATCHES.items():
        d = fetch_match(mid)
        if not d:
            continue
        if "Arsenal" in name:
            analyze_arsenal_palace(d)
        elif "Chelsea" in name:
            analyze_chelsea_united(d)
        elif "Liverpool" in name:
            analyze_liverpool_spurs(d)
        elif "West Ham" in name:
            analyze_lcl_westham(d)

if __name__ == "__main__":
    main()
