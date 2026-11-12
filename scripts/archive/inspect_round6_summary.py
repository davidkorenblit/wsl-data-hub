import json
from pathlib import Path
import sys

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

matches = [
    ("ars_bir", "Arsenal vs Birmingham City", "1 - 1"),
    ("che_tot", "Chelsea vs Tottenham Hotspur", "6 - 2"),
    ("cry_whu", "Crystal Palace vs West Ham United", "0 - 1"),
    ("avl_liv", "Aston Villa vs Liverpool", "2 - 1"),
    ("cha_mun", "Charlton vs Manchester United", "1 - 3"),
    ("lcl_eve", "London City Lionesses vs Everton", "2 - 1"),
    ("mci_bha", "Manchester City vs Brighton", "3 - 2")
]

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
    
    print("=" * 70)
    print(f"⚽ {title} ({final_score})")
    print("=" * 70)
    print(f"  xG: {xg[0]} vs {xg[1]} | Shots (On Target): {shots[0]} ({sot[0]}) vs {shots[1]} ({sot[1]})")
    print(f"  Possession: {poss[0]}% vs {poss[1]}% | Big Chances: {big_chances[0]} vs {big_chances[1]}")
    if goals:
        print(f"  Goals: {', '.join(goals)}")
    print()
