import json
from pathlib import Path
import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

matches = [
    ("tot_ars", "Tottenham Hotspur vs Arsenal", "1 - 2"),
    ("bha_whu", "Brighton vs West Ham United", "3 - 0"),
    ("cry_che", "Crystal Palace vs Chelsea", "1 - 3"),
    ("bir_cha", "Birmingham City vs Charlton", "1 - 0"),
    ("eve_avl", "Everton vs Aston Villa", "2 - 3"),
    ("liv_lcl", "Liverpool vs London City Lionesses", "2 - 2"),
    ("mun_mci", "Manchester United vs Manchester City", "1 - 1")
]

print("=" * 70)
print(" ⚽ WSL MATCHWEEK 7 SUMMARY")
print("=" * 70)

for key, title, final_score in matches:
    p = Path(f"scratch_{key}.json")
    if not p.exists():
        continue
    with open(p, "r", encoding="utf-8") as f:
        d = json.load(f)
    content = d.get("content", {})
    facts = content.get("matchFacts", {})
    events = facts.get("events", {}).get("events", [])
    goals = []
    for e in events:
        if e.get("type") == "Goal":
            scorer = e.get("player", {}).get("name", "Unknown")
            minute = e.get("time", "?")
            assist = e.get("assist", {}).get("name")
            extra = f" (assist: {assist})" if assist else ""
            goals.append(f"{scorer} {minute}'{extra}")
    
    stats = {}
    for grp in content.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
        for s in grp.get("stats", []):
            stats[s.get("title") or s.get("key")] = s.get("stats")
            
    xg = stats.get("Expected goals (xG)", ["-", "-"])
    shots = stats.get("Total shots", ["-", "-"])
    sot = stats.get("Shots on target", ["-", "-"])
    poss = stats.get("Ball possession", ["-", "-"])
    big_chances = stats.get("Big chances", ["-", "-"])
    
    print(f"\n⚽ {title} ({final_score})")
    print(f"  xG: {xg[0]} vs {xg[1]} | Shots (On Target): {shots[0]} ({sot[0]}) vs {shots[1]} ({sot[1]})")
    print(f"  Possession: {poss[0]}% vs {poss[1]}% | Big Chances: {big_chances[0]} vs {big_chances[1]}")
    if goals:
        print(f"  Goals: {', '.join(goals)}")

print("\n" + "=" * 70)
