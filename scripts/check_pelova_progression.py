import json
import glob

tot_matches = glob.glob("data/raw/fotmob/matches/*tot*.json")
pelova_stats = []

for f in sorted(tot_matches):
    with open(f, "r", encoding="utf-8") as fp:
        d = json.load(fp)
    gen = d.get("general", {})
    match_name = f"{gen.get('homeTeam', {}).get('name')} vs {gen.get('awayTeam', {}).get('name')}"
    pstats = d.get("content", {}).get("playerStats", {})
    
    for pid, pdata in pstats.items():
        if "Pelova" in pdata.get("name", ""):
            sd = {}
            for sec in pdata.get("stats", []):
                for sname, sinfo in sec.get("stats", {}).items():
                    sd[sinfo.get("key", sname)] = sinfo.get("stat", {}).get("value", 0)
            
            pelova_stats.append({
                "match": match_name,
                "file": f,
                "mins": sd.get("minutes_played", 0),
                "touches": sd.get("touches", 0),
                "passes": sd.get("accurate_passes", 0),
                "total_passes": sd.get("total_passes", 0),
                "chances": sd.get("chances_created", 0),
                "dispossessed": sd.get("dispossessed", 0),
                "recoveries": sd.get("recoveries", 0),
                "rating": sd.get("rating_title", 0)
            })

print(f"{'Match':<38} | {'Min':<4} | {'Touches':<7} | {'Touches/90':<10} | {'Passes':<8} | {'Chances':<7} | {'Rating':<6}")
print("-" * 90)
for p in pelova_stats:
    t90 = (p['touches'] / p['mins']) * 90 if p['mins'] > 0 else 0
    print(f"{p['match']:<38} | {p['mins']:<4} | {p['touches']:<7} | {t90:<10.1f} | {p['passes']:<8} | {p['chances']:<7} | {p['rating']:<6}")

