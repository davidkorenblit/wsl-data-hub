import json
import glob
from pathlib import Path

# Task 1: Bunny Shaw & City vs West Ham
print("=" * 60)
print("TASK 1: BUNNY SHAW & CITY VS WEST HAM")
print("=" * 60)

# Check all City matches in data/raw/fotmob/matches
city_files = glob.glob("data/raw/fotmob/matches/*mci*.json")
shaw_goals = 0
shaw_matches = 0
for f in sorted(city_files):
    with open(f, "r", encoding="utf-8") as fp:
        d = json.load(fp)
    pstats = d.get("content", {}).get("playerStats", {})
    for pid, pdata in pstats.items():
        if "Shaw" in pdata.get("name", ""):
            shaw_matches += 1
            # get goals from stats
            for sec in pdata.get("stats", []):
                for sname, sinfo in sec.get("stats", {}).items():
                    if sinfo.get("key") == "goals":
                        shaw_goals += sinfo.get("stat", {}).get("value", 0)

print(f"Bunny Shaw in cached matches: {shaw_goals} goals in {shaw_matches} appearances")

# Inspect City vs West Ham
with open("data/raw/fotmob/matches/mw9_mci_whu_5981687.json", "r", encoding="utf-8") as fp:
    mci_whu = json.load(fp)

content = mci_whu.get("content", {})
pstats = content.get("playerStats", {})
for pid, pdata in pstats.items():
    name = pdata.get("name", "")
    if any(k in name for k in ["Fujino", "Hasegawa", "Fowler", "Asseyi", "Gago", "Shaw"]):
        stat_dict = {}
        for sec in pdata.get("stats", []):
            for sname, sinfo in sec.get("stats", {}).items():
                stat_dict[sinfo.get("key", sname)] = sinfo.get("stat", {}).get("value", 0)
        print(f"Player: {name:<20} | Min: {stat_dict.get('minutes_played', 0)} | Touches: {stat_dict.get('touches', 0)} | BoxT: {stat_dict.get('touches_opp_box', 0)} | Tack+Rec: {stat_dict.get('tackles', 0)}+{stat_dict.get('recoveries', 0)} | DuelsWon: {stat_dict.get('duels_won', 0)} | Shots: {stat_dict.get('total_shots', 0)} | Goals: {stat_dict.get('goals', 0)}")

# West Ham vs Liverpool (MW8) where West Ham won 4-1
whu_liv_file = "data/raw/fotmob/matches/mw8_whu_liv_5981682.json"
if Path(whu_liv_file).exists():
    with open(whu_liv_file, "r", encoding="utf-8") as fp:
        whu_liv = json.load(fp)
    print("\n--- West Ham in MW8 (4-1 win over Liverpool) ---")
    for sec in whu_liv.get("content", {}).get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
        for s in sec.get("stats", []):
            if s.get("title") in ["Expected goals (xG)", "Total shots", "Touches in opposition box", "Big chances"]:
                print(f"{s.get('title')}: {s.get('stats')}")

