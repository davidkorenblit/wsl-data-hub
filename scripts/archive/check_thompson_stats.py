import json
from pathlib import Path

# Look at Chelsea matches
matches_dir = Path("data/raw/fotmob/matches")
thompson_stats = []

for p in sorted(matches_dir.glob("mw*_che_*.json")) + sorted(matches_dir.glob("mw*_*_che_*.json")):
    try:
        d = json.load(open(p, "r", encoding="utf-8"))
        mid = d.get("general", {}).get("matchId")
        home = d.get("general", {}).get("homeTeam", {}).get("name")
        away = d.get("general", {}).get("awayTeam", {}).get("name")
        score = f"{d.get('header', {}).get('teams', [{}])[0].get('score')} - {d.get('header', {}).get('teams', [{}])[1].get('score')}"
        che_side = "homeTeam" if "Chelsea" in home else "awayTeam"
        lineup = d.get("content", {}).get("lineup", {}).get(che_side, {})
        for pl in lineup.get("starters", []) + lineup.get("subs", []):
            if "Thompson" in pl.get("name", ""):
                # check stats
                st = {}
                for grp in pl.get("stats", []):
                    for k, v in grp.get("stats", {}).items():
                        val = v.get("stat", {}).get("value") if isinstance(v, dict) else v
                        st[k] = val
                shots = [s for s in d.get("content", {}).get("shotmap", {}).get("shots", []) if "Thompson" in str(s.get("playerName"))]
                xg_sum = sum(s.get("expectedGoals", 0) for s in shots)
                assists = [e for e in d.get("content", {}).get("matchFacts", {}).get("events", {}).get("events", []) if "Thompson" in str(e.get("assistStr"))]
                goals = [e for e in d.get("content", {}).get("matchFacts", {}).get("events", {}).get("events", []) if e.get("type") == "Goal" and "Thompson" in str(e.get("player", {}).get("name"))]
                thompson_stats.append({
                    "match": f"{home} vs {away} ({score})",
                    "file": p.name,
                    "starter": pl in lineup.get("starters", []),
                    "minutes": st.get("Minutes played") or st.get("minutes_played"),
                    "goals": len(goals),
                    "assists": len(assists),
                    "shots": len(shots),
                    "xg": round(xg_sum, 3),
                    "chances_created": st.get("Chances created") or st.get("chances_created"),
                    "dribbles": st.get("Successful dribbles") or st.get("successful_dribbles"),
                    "rating": pl.get("rating", {}).get("num")
                })
    except Exception as ex:
        pass

print(f"Found {len(thompson_stats)} matches with Thompson:")
for t in thompson_stats:
    print(t)

