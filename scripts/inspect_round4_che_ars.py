import json
import requests
import sys

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

def get_match(match_id):
    url = f"https://www.fotmob.com/api/data/matchDetails?matchId={match_id}"
    res = requests.get(url, headers=HEADERS, timeout=15)
    if res.status_code == 200:
        return res.json()
    print(f"Failed to fetch {match_id}: status {res.status_code}")
    return None

def inspect_chelsea_arsenal(data):
    print("\n" + "="*50)
    print("CHELSEA VS ARSENAL (5981654)")
    print("="*50)
    header = data.get("header", {})
    print("Teams:", header.get("teams", []))
    
    # General match stats
    content = data.get("content", {})
    stats = content.get("stats", {})
    # Look at stats periods
    periods = stats.get("Periods", {})
    all_stats = periods.get("All", {}).get("stats", [])
    for group in all_stats:
        title = group.get("title")
        items = group.get("stats", [])
        print(f"\n--- {title} ---")
        for item in items:
            key = item.get("key") or item.get("title")
            stats_val = item.get("stats")
            print(f"  {key}: {stats_val}")
            
    # Lineups and player stats
    lineup = content.get("lineup", {})
    lineup_data = lineup.get("lineup", [])
    for team in lineup_data:
        team_name = team.get("teamName")
        print(f"\nTeam: {team_name}")
        for player in team.get("players", []):
            name = player.get("name", {}).get("fullName")
            pos = player.get("role") or player.get("position")
            rating = player.get("rating", {}).get("num")
            stats_p = player.get("stats", {})
            print(f"  {name} ({pos}) - Rating: {rating}")
            # print some stats if available
            if stats_p:
                for stat_grp in stats_p:
                    for s_item in stat_grp.get("stats", {}).values():
                        # key and value
                        pass

if __name__ == "__main__":
    data = get_match(5981654)
    if data:
        with open("scratch_che_ars.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Saved scratch_che_ars.json")
