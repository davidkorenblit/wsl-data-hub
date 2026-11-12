#!/usr/bin/env python3
import sys
import json
import requests

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HEADERS = {"User-Agent": "Mozilla/5.0"}

def inspect_arsenal():
    res = requests.get('https://www.fotmob.com/api/data/matchDetails?matchId=5981639', headers=HEADERS).json()
    lineup = res.get('content', {}).get('lineup', {})
    
    for team_key in ['homeTeam', 'awayTeam']:
        t = lineup.get(team_key, {})
        print(f"\n=== {t.get('name')} ===")
        # Check players structure
        players = t.get('players', [])
        # players is a list of rows/lines
        for row in players:
            for p in row:
                name = p.get('name', {}).get('fullName') or p.get('name')
                rating = p.get('rating', {}).get('num', '-')
                role = p.get('role')
                stats = p.get('stats', [])
                shot_stats = {}
                for s in stats:
                    for item in s.get('stats', {}).values():
                        if isinstance(item, dict) and 'stat' in item:
                            shot_stats[item.get('title')] = item.get('stat', {}).get('value')
                print(f"  {name} ({role}) - Rating: {rating}")
                # Print key attack stats if any
                shot_info = []
                for s_cat in stats:
                    for k, val in s_cat.get('stats', {}).items():
                        title = val.get('title')
                        v = val.get('stat', {}).get('value')
                        if title in ['Total shots', 'Shots on target', 'Expected goals (xG)', 'Chances created', 'Saves', 'Goals prevented']:
                            shot_info.append(f"{title}: {v}")
                if shot_info:
                    print(f"      {', '.join(shot_info)}")

def inspect_lcl_westham():
    res = requests.get('https://www.fotmob.com/api/data/matchDetails?matchId=5981634', headers=HEADERS).json()
    lineup = res.get('content', {}).get('lineup', {})
    t = lineup.get('awayTeam', {})
    print(f"\n=== LCL Players (vs West Ham) ===")
    for row in t.get('players', []):
        for p in row:
            name = p.get('name', {}).get('fullName') or p.get('name')
            role = p.get('role')
            rating = p.get('rating', {}).get('num', '-')
            def_info = []
            for s_cat in p.get('stats', []):
                for k, val in s_cat.get('stats', {}).items():
                    title = val.get('title')
                    v = val.get('stat', {}).get('value')
                    if title in ['Tackles won', 'Interceptions', 'Recoveries', 'Duels won', 'Ground duels won', 'Chances created', 'Expected goals (xG)']:
                        def_info.append(f"{title}: {v}")
            print(f"  {name} ({role}) - Rating: {rating}")
            if def_info:
                print(f"      {', '.join(def_info)}")

if __name__ == "__main__":
    inspect_arsenal()
    inspect_lcl_westham()
