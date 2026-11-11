import json
import glob
from pathlib import Path

# =====================================================================
# 1. ARSENAL CONCEDED GOALS (MW1 - MW9)
# =====================================================================
print("=" * 70)
print("1. ARSENAL CONCEDED GOALS ANALYSIS (MW1 - MW9)")
print("=" * 70)

arsenal_matches = glob.glob("data/raw/fotmob/matches/*ars*.json")
ars_goals_conceded = []

for f in sorted(arsenal_matches):
    with open(f, "r", encoding="utf-8") as fp:
        d = json.load(fp)
    
    gen = d.get("general", {})
    home_team = gen.get("homeTeam", {}).get("name", "")
    away_team = gen.get("awayTeam", {}).get("name", "")
    ars_is_home = "Arsenal" in home_team
    opp_team = away_team if ars_is_home else home_team
    opp_id = gen.get("awayTeam", {}).get("id") if ars_is_home else gen.get("homeTeam", {}).get("id")
    
    events = d.get("content", {}).get("matchFacts", {}).get("events", {}).get("events", [])
    shotmap = d.get("content", {}).get("shotmap", {}).get("shots", [])
    
    for e in events:
        if e.get("type") == "Goal" and not e.get("isOwnGoal", False):
            # check if scored by opponent
            # if Arsenal is home, opp is away
            is_opp = False
            scorer_id = e.get("player", {}).get("id")
            # find in shotmap
            shot_info = {}
            for s in shotmap:
                if s.get("eventType") == "Goal" and s.get("time") == e.get("time"):
                    # check team
                    if (ars_is_home and s.get("teamId") != 258657) or (not ars_is_home and s.get("teamId") != 258657):
                        is_opp = True
                        shot_info = s
                        break
            
            # fallback if shotmap match
            if not shot_info:
                # check team in event if possible
                pass
            
            if is_opp:
                ars_goals_conceded.append({
                    "match": f"{home_team} vs {away_team}",
                    "file": Path(f).name,
                    "minute": e.get("time"),
                    "scorer": e.get("player", {}).get("name"),
                    "assist": e.get("assist", {}).get("name"),
                    "situation": shot_info.get("situation", "OpenPlay"),
                    "shotType": shot_info.get("shotType", ""),
                    "isFastBreak": shot_info.get("isFastBreak", False),
                    "x": shot_info.get("x"),
                    "y": shot_info.get("y"),
                    "xg": shot_info.get("expectedGoals")
                })

for g in ars_goals_conceded:
    print(f"Match: {g['match']} | Min: {g['minute']}' | Scorer: {g['scorer']} | Assist: {g['assist']} | Situation: {g['situation']} | FastBreak: {g['isFastBreak']} | xG: {g['xg']}")

# If some matches aren't named with ars, let's search all matches for Arsenal conceded
print(f"Total conceded found in cached matches: {len(ars_goals_conceded)}")

