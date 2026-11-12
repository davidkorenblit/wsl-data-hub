import json
import glob

che_files = glob.glob("data/raw/fotmob/matches/*che*.json")
chelsea_creators = {}

for f in che_files:
    with open(f, "r", encoding="utf-8") as fp:
        d = json.load(fp)
    pstats = d.get("content", {}).get("playerStats", {})
    for pid, pdata in pstats.items():
        if "Chelsea" in pdata.get("teamName", ""):
            name = pdata.get("name")
            if name not in chelsea_creators:
                chelsea_creators[name] = {
                    "matches": 0,
                    "minutes": 0,
                    "chances_created": 0,
                    "assists": 0,
                    "expected_assists": 0.0,
                    "touches": 0,
                    "shots": 0
                }
            
            sd = {}
            for sec in pdata.get("stats", []):
                for sname, sinfo in sec.get("stats", {}).items():
                    sd[sinfo.get("key", sname)] = sinfo.get("stat", {}).get("value", 0)
            
            mins = sd.get("minutes_played", 0)
            if mins > 0:
                chelsea_creators[name]["matches"] += 1
                chelsea_creators[name]["minutes"] += mins
                chelsea_creators[name]["chances_created"] += sd.get("chances_created", 0)
                chelsea_creators[name]["assists"] += sd.get("assists", 0)
                chelsea_creators[name]["expected_assists"] += sd.get("expected_assists", 0.0)
                chelsea_creators[name]["touches"] += sd.get("touches", 0)
                chelsea_creators[name]["shots"] += sd.get("total_shots", 0)

print(f"{'Player':<24} | {'Mins':<5} | {'ChancesCreated':<14} | {'Per90 CC':<8} | {'Assists':<7} | {'xA':<5}")
print("-" * 75)
for name, s in sorted(chelsea_creators.items(), key=lambda x: -x[1]["chances_created"]):
    if s["minutes"] >= 180:
        cc_per90 = (s["chances_created"] / s["minutes"]) * 90 if s["minutes"] > 0 else 0
        print(f"{name:<24} | {s['minutes']:<5} | {s['chances_created']:<14} | {cc_per90:<8.2f} | {s['assists']:<7} | {s['expected_assists']:<5.2f}")

