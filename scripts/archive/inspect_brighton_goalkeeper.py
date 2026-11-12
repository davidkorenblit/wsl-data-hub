"""
Inspect Brighton Goalkeeping Form in 2026/27 (Matches 1-4) vs 2025/26 Baseline
==============================================================================
"""

import sys
import io
import json
import requests

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

def main():
    print("=== 1. CHECKING GOALKEEPER IN MATCHES 1-4 ===")
    match_ids = [
        ("Round 1 vs Arsenal", 5981533),
        ("Round 2 vs Birmingham", 5981636),
        ("Round 3 vs Villa", 5981645),
        ("Round 4 vs LCL", 5981649)
    ]
    
    gk_ids = set()
    for name, mid in match_ids:
        data = get_json(f"https://www.fotmob.com/api/data/matchDetails?matchId={mid}")
        if not data:
            continue
        content = data.get("content", {})
        lineup = content.get("lineup", {})
        
        # Determine if Brighton was home or away
        header = data.get("header", {})
        teams = header.get("teams", [])
        is_bha_home = "Brighton" in teams[0].get("name", "") if len(teams) > 0 else False
        
        bha_lineup = lineup.get("homeTeam" if is_bha_home else "awayTeam", {})
        starters = bha_lineup.get("starters", [])
        
        # Goalkeeper is position 1 / GK
        gk = starters[0] if starters else {}
        gk_name = gk.get("name", {})
        if isinstance(gk_name, dict):
            gk_name = gk_name.get("fullName", gk_name.get("name"))
        gk_id = gk.get("id")
        gk_ids.add(gk_id)
        
        rating = gk.get("performance", {}).get("rating")
        
        # Opponent shots on target & goals
        stats = content.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", [])
        shots_on_target = None
        for grp in stats:
            for item in grp.get("stats", []):
                if item.get("title") == "Shots on target":
                    sot = item.get("stats", [])
                    shots_on_target = sot[1 if is_bha_home else 0] # opponent's SoT
        
        score = header.get("status", {}).get("scoreStr")
        print(f"\n{name} ({score}):")
        print(f"  Starter GK: {gk_name} (ID: {gk_id}) | FotMob Rating: {rating}")
        print(f"  Opponent Shots on Target: {shots_on_target}")

    print("\n=== 2. PULLING GOALKEEPER OVERALL STATS ===")
    for gkid in gk_ids:
        if not gkid:
            continue
        p_data = get_json(f"https://www.fotmob.com/api/data/playerData?id={gkid}")
        if not p_data:
            continue
        p_name = p_data.get("name")
        print(f"\nPlayer: {p_name} (ID: {gkid})")
        
        # Inspect season stats
        first_season = p_data.get("firstSeasonStats", {})
        stats_sec = first_season.get("statsSection", {})
        for grp in stats_sec.get("items", []):
            grp_title = grp.get("title")
            print(f"  Group: {grp_title}")
            for item in grp.get("items", []):
                print(f"    {item.get('title')}: {item.get('statValue')} (per90: {item.get('per90')}, percentile: {item.get('percentileRankPer90')})")

if __name__ == "__main__":
    main()
