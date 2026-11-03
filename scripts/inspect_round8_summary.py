import json
from pathlib import Path
import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

matches = [
    ("eve_mun", "Everton vs Manchester United", "0 - 0"),
    ("ars_avl", "Arsenal vs Aston Villa", "1 - 1"),
    ("lcl_mci", "London City Lionesses vs Manchester City", "1 - 2"),
    ("bir_tot", "Birmingham City vs Tottenham Hotspur", "1 - 4"),
    ("bha_cry", "Brighton vs Crystal Palace", "2 - 1"),
    ("whu_liv", "West Ham United vs Liverpool", "4 - 1"),
    ("cha_che", "Charlton vs Chelsea", "0 - 6")
]

print("=" * 70)
print(" ⚽ WSL MATCHWEEK 8 SUMMARY")
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
