import json
import glob
from pathlib import Path

ars_files = [
    ("MW1", "data/raw/fotmob/matches/mw1_bha_ars_5981533.json"),
    ("MW2", "data/raw/fotmob/matches/mw2_cry_ars_5981639.json"),
    ("MW3", "data/raw/fotmob/matches/mw3_mun_ars_5981644.json"),
    ("MW4", "data/raw/fotmob/matches/mw4_che_ars_5981654.json"),
    ("MW5", "data/raw/fotmob/matches/mw5_mci_ars_5981661.json"),
    ("MW6", "data/raw/fotmob/matches/mw6_ars_bir_5981663.json"),
    ("MW7", "data/raw/fotmob/matches/mw7_tot_ars_5981675.json"),
    ("MW8", "data/raw/fotmob/matches/mw8_ars_avl_5981677.json"),
    ("MW9", "data/raw/fotmob/matches/mw9_liv_ars_5981683.json"),
]

print("=== ALL GOALS CONCEDED BY ARSENAL IN 2026/27 (MW1 - MW9) ===")

conceded_goals = []

for mw, fpath in ars_files:
    if not Path(fpath).exists():
        continue
    with open(fpath, "r", encoding="utf-8") as fp:
        d = json.load(fp)
    gen = d.get("general", {})
    home_name = gen.get("homeTeam", {}).get("name", "")
    away_name = gen.get("awayTeam", {}).get("name", "")
    ars_is_home = "Arsenal" in home_name
    opp_name = away_name if ars_is_home else home_name
    opp_id = gen.get("awayTeam", {}).get("id") if ars_is_home else gen.get("homeTeam", {}).get("id")
    
    content = d.get("content", {})
    events = content.get("matchFacts", {}).get("events", {}).get("events", [])
    shotmap = content.get("shotmap", {}).get("shots", [])
    
    for e in events:
        if e.get("type") == "Goal":
            # check if opponent goal
            scorer_id = e.get("player", {}).get("id")
            # verify via shotmap or event team
            # Find in shotmap
            shot = None
            for s in shotmap:
                if s.get("eventType") == "Goal" and abs(s.get("time", 0) - e.get("time", 0)) <= 1:
                    if s.get("teamId") != 258657:
                        shot = s
                        break
            
            # If shot found or team is not Arsenal
            is_opp = False
            if shot:
                is_opp = True
            elif e.get("isOwnGoal", False):
                # if Arsenal scored an own goal, that's conceded
                # check which player
                pass
            else:
                # check team in playerStats
                pstats = content.get("playerStats", {})
                for pid, pdata in pstats.items():
                    if pdata.get("name") == e.get("player", {}).get("name"):
                        if "Arsenal" not in pdata.get("teamName", ""):
                            is_opp = True
            
            if is_opp:
                scorer_name = e.get("player", {}).get("name")
                minute = e.get("time")
                assist = e.get("assist", {}).get("name")
                sit = shot.get("situation", "OpenPlay") if shot else "Unknown"
                fast_break = shot.get("isFastBreak", False) if shot else False
                xg = shot.get("expectedGoals", 0.0) if shot else 0.0
                shot_type = shot.get("shotType", "") if shot else ""
                conceded_goals.append({
                    "mw": mw,
                    "opp": opp_name,
                    "minute": minute,
                    "scorer": scorer_name,
                    "assist": assist,
                    "situation": sit,
                    "fast_break": fast_break,
                    "xg": xg,
                    "shot_type": shot_type
                })

for g in conceded_goals:
    print(f"[{g['mw']}] vs {g['opp']:<16} | Min: {g['minute']:<2}' | Scorer: {g['scorer']:<18} | Assist: {str(g['assist']):<18} | Sit: {g['situation']:<10} | FastBreak: {str(g['fast_break']):<5} | xG: {g['xg']}")

print(f"\nTotal goals conceded by Arsenal: {len(conceded_goals)}")

