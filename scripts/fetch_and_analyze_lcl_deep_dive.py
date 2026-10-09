#!/usr/bin/env python3
"""
Deep Tactical Analysis: London City Lionesses (WSL 2026/27 MW1-5)
=================================================================
1. Queries LCL team data (FotMob ID: 1075419) to retrieve squad and 2026/27 fixtures.
2. Fetches and aggregates all 2026/27 matches:
   - Matchweek 1: Manchester United
   - Matchweek 2: West Ham
   - Matchweek 3: Brighton
   - Matchweek 4: Tottenham / others
   - Matchweek 5: etc.
3. Deep Player Metrics:
   - Alexia Putellas ("El Reina"): Goals, assists, shots, xG, chances created,
     and out-of-possession work rate (recoveries, interceptions, ground duels, tackles).
   - Daniëlle van de Donk: Minutes, fitness, duels, chances, contributions.
4. Defensive Solidity & Tactical Shift:
   - Verification: Did LCL concede any goals since the West Ham match?
   - Clean sheets, goals conceded, xGA, shots conceded, possession evolution.
5. Exports structured data to _data/lcl_mw5_deep_analysis.json.
"""

import os
import sys
import json
import time
from pathlib import Path
from typing import Dict, Any, List, Optional
import requests

# Fix Windows console UTF-8 output
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_MATCHES_DIR = PROJECT_ROOT / "data" / "raw" / "fotmob" / "matches"
RAW_TEAMS_DIR = PROJECT_ROOT / "data" / "raw" / "fotmob" / "teams"
RAW_PLAYERS_DIR = PROJECT_ROOT / "data" / "raw" / "fotmob" / "players"
SITE_DATA_DIR = PROJECT_ROOT / "_data"

RAW_MATCHES_DIR.mkdir(parents=True, exist_ok=True)
RAW_TEAMS_DIR.mkdir(parents=True, exist_ok=True)
RAW_PLAYERS_DIR.mkdir(parents=True, exist_ok=True)
SITE_DATA_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

LCL_TEAM_ID = 1075419

def fetch_json(url: str, retries: int = 5, delay: float = 1.5) -> Optional[Dict[str, Any]]:
    for attempt in range(retries):
        try:
            res = requests.get(url, headers=HEADERS, timeout=20)
            if res.status_code == 200:
                return res.json()
            print(f"  [Attempt {attempt + 1}] HTTP {res.status_code} for {url}")
        except Exception as e:
            print(f"  [Attempt {attempt + 1}] Error: {e}")
        time.sleep(delay)
    return None

def load_or_fetch_lcl_team() -> Optional[Dict[str, Any]]:
    team_file = RAW_TEAMS_DIR / f"team_{LCL_TEAM_ID}_london_city_lionesses.json"
    data = None
    if team_file.exists():
        with open(team_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    
    # Try fetching fresh data
    url = f"https://www.fotmob.com/api/data/teams?id={LCL_TEAM_ID}"
    fresh_data = fetch_json(url)
    if fresh_data and "fixtures" in fresh_data:
        data = fresh_data
        with open(team_file, "w", encoding="utf-8") as f:
            json.dump(fresh_data, f, ensure_ascii=False, indent=2)
        print(f"[OK] Fetched fresh LCL team data.")
    else:
        print(f"[INFO] Using cached LCL team data.")
    return data

def get_completed_matches(team_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    fixtures_section = team_data.get("fixtures", {})
    all_fixtures = fixtures_section.get("allFixtures", {}).get("fixtures", [])
    if not all_fixtures:
        # Check other possible locations
        for k in ["previousFixtures", "fixtures", "results"]:
            if k in fixtures_section:
                print(f"Found key in fixtures: {k}")
    
    completed = []
    # If all_fixtures is empty, check overview fixtures
    overview_fixtures = team_data.get("overview", {}).get("fixtures", [])
    fixtures_to_check = all_fixtures if all_fixtures else overview_fixtures
    
    for fix in fixtures_to_check:
        status = fix.get("status", {})
        if status.get("finished"):
            completed.append(fix)
    
    print(f"Found {len(completed)} completed matches for LCL in team json:")
    for m in completed:
        home = m.get("home", {}).get("name")
        away = m.get("away", {}).get("name")
        home_s = m.get("home", {}).get("score")
        away_s = m.get("away", {}).get("score")
        tourn = m.get("tournament", {}).get("name")
        print(f"  - [{m.get('id')}] {home} {home_s} : {away_s} {away} ({tourn}) - {m.get('status', {}).get('utcTime')}")
    return completed

def fetch_match_details(match_id: int) -> Optional[Dict[str, Any]]:
    match_file = RAW_MATCHES_DIR / f"match_{match_id}.json"
    if match_file.exists():
        with open(match_file, "r", encoding="utf-8") as f:
            return json.load(f)
    
    url = f"https://www.fotmob.com/api/matchDetails?matchId={match_id}"
    data = fetch_json(url)
    if data:
        with open(match_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"  [OK] Saved match {match_id} details.")
    return data

def extract_match_team_stats(match_data: Dict[str, Any], match_meta: Dict[str, Any]) -> Dict[str, Any]:
    header = match_data.get("header", {})
    teams = header.get("teams", [])
    lcl_is_home = (teams[0].get("id") == LCL_TEAM_ID) if len(teams) > 0 else True
    
    content = match_data.get("content", {})
    stats_sec = content.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", [])
    
    # Fallback team score
    home_score = teams[0].get("score", 0) if len(teams) > 0 else 0
    away_score = teams[1].get("score", 0) if len(teams) > 1 else 0
    lcl_goals = home_score if lcl_is_home else away_score
    opp_goals = away_score if lcl_is_home else home_score
    
    opponent_name = teams[1].get("name") if lcl_is_home else teams[0].get("name")
    
    team_stats = {
        "id": match_meta.get("id"),
        "date": match_meta.get("status", {}).get("utcTime"),
        "tourn": match_meta.get("tournament", {}).get("name"),
        "opponent": opponent_name,
        "score": f"{lcl_goals}-{opp_goals}",
        "lcl_goals": lcl_goals,
        "opp_goals": opp_goals,
        "clean_sheet": (opp_goals == 0),
        "possession": 0.0,
        "xg": 0.0,
        "xga": 0.0,
        "shots_for": 0,
        "shots_against": 0,
        "sot_against": 0
    }
    
    for grp in stats_sec:
        for item in grp.get("items", []):
            title = item.get("title", "")
            vals = item.get("values", [0, 0])
            lcl_val = vals[0] if lcl_is_home else vals[1]
            opp_val = vals[1] if lcl_is_home else vals[0]
            
            if title == "Ball possession":
                try:
                    team_stats["possession"] = float(str(lcl_val).replace("%", ""))
                except:
                    pass
            elif title == "Expected goals (xG)":
                try:
                    team_stats["xg"] = float(lcl_val)
                    team_stats["xga"] = float(opp_val)
                except:
                    pass
            elif title == "Total shots":
                try:
                    team_stats["shots_for"] = int(lcl_val)
                    team_stats["shots_against"] = int(opp_val)
                except:
                    pass
            elif title == "Shots on target":
                try:
                    team_stats["sot_against"] = int(opp_val)
                except:
                    pass

    return team_stats

def extract_player_stats_from_match(match_data: Dict[str, Any], player_needle: str) -> Optional[Dict[str, Any]]:
    content = match_data.get("content", {})
    pstats = content.get("playerStats", {})
    
    for pid, pdata in pstats.items():
        name = pdata.get("name", "")
        if player_needle.lower() in name.lower():
            # Found player!
            res = {
                "name": name,
                "pid": pid,
                "minutes": 0,
                "goals": 0,
                "assists": 0,
                "shots": 0,
                "shots_on_target": 0,
                "xg": 0.0,
                "chances_created": 0,
                "passes_acc": 0,
                "passes_tot": 0,
                "touches": 0,
                "touches_opp_box": 0,
                "dribbles_succ": 0,
                "dribbles_att": 0,
                "ground_duels_won": 0,
                "ground_duels_att": 0,
                "aerial_duels_won": 0,
                "aerial_duels_att": 0,
                "tackles_won": 0,
                "interceptions": 0,
                "recoveries": 0,
                "clearances": 0,
                "dribbled_past": 0,
                "fouls_committed": 0,
                "fouls_won": 0,
                "rating": 0.0
            }
            
            for cat in pdata.get("stats", []):
                for k, v in cat.get("stats", {}).items():
                    st = v.get("stat", {})
                    val = st.get("value", 0)
                    tot = st.get("total", 0)
                    
                    if k == "Minutes played":
                        res["minutes"] = val
                    elif k == "Goals":
                        res["goals"] = val
                    elif k == "Assists":
                        res["assists"] = val
                    elif k == "Total shots":
                        res["shots"] = val
                    elif k == "Shots on target":
                        res["shots_on_target"] = val
                    elif k == "Expected goals (xG)":
                        res["xg"] = val
                    elif k == "Chances created":
                        res["chances_created"] = val
                    elif k == "Accurate passes":
                        res["passes_acc"] = val
                        res["passes_tot"] = tot
                    elif k == "Touches":
                        res["touches"] = val
                    elif k == "Touches in opposition box":
                        res["touches_opp_box"] = val
                    elif k == "Successful dribbles":
                        res["dribbles_succ"] = val
                        res["dribbles_att"] = tot
                    elif k == "Ground duels won":
                        res["ground_duels_won"] = val
                        res["ground_duels_att"] = tot
                    elif k == "Aerial duels won":
                        res["aerial_duels_won"] = val
                        res["aerial_duels_att"] = tot
                    elif k == "Tackles won":
                        res["tackles_won"] = val
                    elif k == "Interceptions":
                        res["interceptions"] = val
                    elif k == "Recoveries":
                        res["recoveries"] = val
                    elif k == "Clearances":
                        res["clearances"] = val
                    elif k == "Dribbled past":
                        res["dribbled_past"] = val
                    elif k == "Fouls committed":
                        res["fouls_committed"] = val
                    elif k == "Fouls won":
                        res["fouls_won"] = val
                    elif k == "FotMob rating":
                        res["rating"] = val

            return res
    return None

def main():
    print("=== Fetching & Analyzing London City Lionesses 2026/27 ===")
    team_data = load_or_fetch_lcl_team()
    if not team_data:
        print("[ERROR] Could not load LCL team data.")
        return
    
    matches = get_completed_matches(team_data)
    if not matches:
        print("[ERROR] No completed 2026 matches found for LCL.")
        return

    team_match_summaries = []
    alexia_by_match = []
    dvdd_by_match = []
    
    for m in matches:
        mid = m.get("id")
        m_details = fetch_match_details(mid)
        if not m_details:
            continue
        
        t_stat = extract_match_team_stats(m_details, m)
        team_match_summaries.append(t_stat)
        
        # Check Alexia Putellas
        alexia = extract_player_stats_from_match(m_details, "Putellas")
        if not alexia:
            alexia = extract_player_stats_from_match(m_details, "Alexia")
        if alexia:
            alexia["match_id"] = mid
            alexia["opponent"] = t_stat["opponent"]
            alexia["date"] = t_stat["date"]
            alexia_by_match.append(alexia)
            
        # Check Daniëlle van de Donk
        dvdd = extract_player_stats_from_match(m_details, "Donk")
        if not dvdd:
            dvdd = extract_player_stats_from_match(m_details, "Danielle")
        if dvdd:
            dvdd["match_id"] = mid
            dvdd["opponent"] = t_stat["opponent"]
            dvdd["date"] = t_stat["date"]
            dvdd_by_match.append(dvdd)

    # Sort chronological
    team_match_summaries.sort(key=lambda x: str(x.get("date")))
    alexia_by_match.sort(key=lambda x: str(x.get("date")))
    dvdd_by_match.sort(key=lambda x: str(x.get("date")))

    print("\n=== LCL Match Results & Clean Sheet Tracking ===")
    conceded_since_whu = 0
    whu_seen = False
    for tm in team_match_summaries:
        opp = tm["opponent"]
        score = tm["score"]
        tourn = tm["tourn"]
        print(f"  Match: vs {opp:20} | Score: {score:5} | CS: {tm['clean_sheet']} | Poss: {tm['possession']}% | xGA: {tm['xga']} | Shots Against: {tm['shots_against']}")
        if "west ham" in opp.lower():
            whu_seen = True
        elif whu_seen:
            conceded_since_whu += tm["opp_goals"]

    print(f"\nGoals conceded since West Ham match: {conceded_since_whu}")

    # Alexia Aggregation
    alexia_tot = {
        "matches": len(alexia_by_match),
        "minutes": sum(x["minutes"] for x in alexia_by_match),
        "goals": sum(x["goals"] for x in alexia_by_match),
        "assists": sum(x["assists"] for x in alexia_by_match),
        "shots": sum(x["shots"] for x in alexia_by_match),
        "shots_on_target": sum(x["shots_on_target"] for x in alexia_by_match),
        "xg": round(sum(x["xg"] for x in alexia_by_match), 2),
        "chances_created": sum(x["chances_created"] for x in alexia_by_match),
        "passes_acc": sum(x["passes_acc"] for x in alexia_by_match),
        "passes_tot": sum(x["passes_tot"] for x in alexia_by_match),
        "touches": sum(x["touches"] for x in alexia_by_match),
        "touches_opp_box": sum(x["touches_opp_box"] for x in alexia_by_match),
        "dribbles_succ": sum(x["dribbles_succ"] for x in alexia_by_match),
        "dribbles_att": sum(x["dribbles_att"] for x in alexia_by_match),
        "ground_duels_won": sum(x["ground_duels_won"] for x in alexia_by_match),
        "ground_duels_att": sum(x["ground_duels_att"] for x in alexia_by_match),
        "aerial_duels_won": sum(x["aerial_duels_won"] for x in alexia_by_match),
        "aerial_duels_att": sum(x["aerial_duels_att"] for x in alexia_by_match),
        "tackles_won": sum(x["tackles_won"] for x in alexia_by_match),
        "interceptions": sum(x["interceptions"] for x in alexia_by_match),
        "recoveries": sum(x["recoveries"] for x in alexia_by_match),
        "clearances": sum(x["clearances"] for x in alexia_by_match),
        "dribbled_past": sum(x["dribbled_past"] for x in alexia_by_match),
        "fouls_won": sum(x["fouls_won"] for x in alexia_by_match),
        "by_match": alexia_by_match
    }

    # Daniëlle van de Donk Aggregation
    dvdd_tot = {
        "matches": len(dvdd_by_match),
        "minutes": sum(x["minutes"] for x in dvdd_by_match),
        "goals": sum(x["goals"] for x in dvdd_by_match),
        "assists": sum(x["assists"] for x in dvdd_by_match),
        "shots": sum(x["shots"] for x in dvdd_by_match),
        "shots_on_target": sum(x["shots_on_target"] for x in dvdd_by_match),
        "xg": round(sum(x["xg"] for x in dvdd_by_match), 2),
        "chances_created": sum(x["chances_created"] for x in dvdd_by_match),
        "passes_acc": sum(x["passes_acc"] for x in dvdd_by_match),
        "passes_tot": sum(x["passes_tot"] for x in dvdd_by_match),
        "touches": sum(x["touches"] for x in dvdd_by_match),
        "touches_opp_box": sum(x["touches_opp_box"] for x in dvdd_by_match),
        "dribbles_succ": sum(x["dribbles_succ"] for x in dvdd_by_match),
        "dribbles_att": sum(x["dribbles_att"] for x in dvdd_by_match),
        "ground_duels_won": sum(x["ground_duels_won"] for x in dvdd_by_match),
        "ground_duels_att": sum(x["ground_duels_att"] for x in dvdd_by_match),
        "aerial_duels_won": sum(x["aerial_duels_won"] for x in dvdd_by_match),
        "aerial_duels_att": sum(x["aerial_duels_att"] for x in dvdd_by_match),
        "tackles_won": sum(x["tackles_won"] for x in dvdd_by_match),
        "interceptions": sum(x["interceptions"] for x in dvdd_by_match),
        "recoveries": sum(x["recoveries"] for x in dvdd_by_match),
        "clearances": sum(x["clearances"] for x in dvdd_by_match),
        "dribbled_past": sum(x["dribbled_past"] for x in dvdd_by_match),
        "fouls_won": sum(x["fouls_won"] for x in dvdd_by_match),
        "by_match": dvdd_by_match
    }

    output_data = {
        "matches": team_match_summaries,
        "conceded_since_whu": conceded_since_whu,
        "alexia_putellas": alexia_tot,
        "danielle_van_de_donk": dvdd_tot
    }

    out_file = SITE_DATA_DIR / "lcl_mw5_deep_analysis.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    print(f"\n[OK] Successfully saved detailed LCL analysis to {out_file}")

if __name__ == "__main__":
    main()
