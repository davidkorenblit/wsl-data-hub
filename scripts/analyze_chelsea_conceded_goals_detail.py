"""
Analyze the exact goals conceded by Chelsea in key matches from FotMob matchDetails
"""
import requests
import json

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

MATCHES_TO_ANALYZE = [
    {"id": 4893195, "title": "WSL: Man City vs Chelsea (5-1, conceded 5)", "opp": "Manchester City"},
    {"id": 5103030, "title": "UWCL: Arsenal vs Chelsea (3-1, conceded 3)", "opp": "Arsenal"},
    {"id": 4893185, "title": "WSL: Arsenal vs Chelsea (2-0, conceded 2)", "opp": "Arsenal"},
    {"id": 5296879, "title": "FA Cup: Man City vs Chelsea (3-2, conceded 3)", "opp": "Manchester City"}
]

def analyze_match(m_info):
    mid = m_info["id"]
    url = f"https://www.fotmob.com/api/data/matchDetails?matchId={mid}"
    res = requests.get(url, headers=HEADERS, timeout=15)
    data = res.json()
    
    content = data.get("content", {})
    shotmap = content.get("shotmap", {}).get("shots", [])
    
    print(f"\n=======================================================")
    print(f"MATCH: {m_info['title']} (ID: {mid})")
    print(f"=======================================================")
    
    # Filter shots by opponent against Chelsea
    opp_shots = [s for s in shotmap if s.get("teamId") != 258661]
    opp_goals = [s for s in opp_shots if s.get("eventType") == "Goal"]
    
    print(f"Total opponent shots: {len(opp_shots)} | Opponent Goals: {len(opp_goals)}")
    
    for i, g in enumerate(opp_goals, 1):
        p_name = g.get("playerName")
        min_p = g.get("min")
        sit = g.get("situation")
        s_type = g.get("shotType")
        in_box = g.get("isFromInsideBox")
        xg = round(g.get("expectedGoals", 0), 2)
        xgot = round(g.get("expectedGoalsOnTarget", 0), 2)
        x_coord = round(g.get("x", 0), 1)
        y_coord = round(g.get("y", 0), 1)
        
        print(f"\n  GOAL #{i}: {p_name} ({min_p}')")
        print(f"    - Situation: {sit}")
        print(f"    - Shot Type: {s_type} (Inside Box: {in_box})")
        print(f"    - Coordinates: (x={x_coord}, y={y_coord}) - Pitch range: x: 0-105, y: 0-68")
        print(f"    - xG: {xg} | xGOT: {xgot}")

    # Check high xG saves by Hampton in this match
    hampton_saves = [s for s in opp_shots if s.get("eventType") in ["AttemptSaved", "SavedOffLine"]]
    print(f"\nHampton Saves in match: {len(hampton_saves)}")
    for sv in hampton_saves:
        xg = round(sv.get("expectedGoals", 0), 2)
        if xg >= 0.20:
            print(f"  * BIG SAVE: against {sv.get('playerName')} ({sv.get('min')}') | Sit: {sv.get('situation')} | xG: {xg}")

for m in MATCHES_TO_ANALYZE:
    try:
        analyze_match(m)
    except Exception as e:
        print(f"Error analyzing {m['title']}: {e}")
