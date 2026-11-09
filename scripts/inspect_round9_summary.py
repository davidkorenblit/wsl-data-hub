import json
from pathlib import Path
import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

matches = [
    ("che_eve", "Chelsea vs Everton", "1 - 1"),
    ("mci_whu", "Manchester City vs West Ham United", "5 - 0"),
    ("avl_mun", "Aston Villa vs Manchester United", "0 - 1"),
    ("liv_ars", "Liverpool vs Arsenal", "1 - 2"),
    ("cry_cha", "Crystal Palace vs Charlton", "3 - 2"),
    ("tot_bha", "Tottenham Hotspur vs Brighton", "2 - 1"),
    ("lcl_bir", "London City Lionesses vs Birmingham City", "4 - 1")
]

print("=" * 70)
print(" ⚽ WSL MATCHWEEK 9 SUMMARY")
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

