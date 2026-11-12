import requests
import json

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

def check_match(mid, name):
    url = f"https://www.fotmob.com/api/data/matchDetails?matchId={mid}"
    res = requests.get(url, headers=HEADERS, timeout=15)
    data = res.json()
    shotmap = data.get("content", {}).get("shotmap", {}).get("shots", [])
    
    print(f"\n==========================================")
    print(f"{name} (ID: {mid})")
    print(f"==========================================")
    opp_shots = [s for s in shotmap if s.get("teamId") != 258661]
    opp_goals = [s for s in opp_shots if s.get("eventType") == "Goal"]
    print(f"Opponent shots: {len(opp_shots)}, Goals: {len(opp_goals)}")
    
    for g in opp_goals:
        print(f"  * GOAL: {g.get('playerName')} ({g.get('min')}') | Sit: {g.get('situation')} | Type: {g.get('shotType')} | xG: {round(g.get('expectedGoals', 0), 2)} | (x={round(g.get('x', 0), 1)}, y={round(g.get('y', 0), 1)})")
        
    for s in opp_shots:
        sit = s.get("situation")
        xg = round(s.get("expectedGoals", 0), 2)
        if sit == "FastBreak" or xg >= 0.3:
            print(f"  -> Threat ({sit}): {s.get('playerName')} ({s.get('min')}') | evt: {s.get('eventType')} | xG: {xg}")

check_match(4893223, "WSL: Chelsea vs Aston Villa (4-3)")
check_match(4893210, "WSL: Chelsea vs Brighton (2-1)")
