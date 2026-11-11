import json

with open("data/raw/fotmob/matches/mw9_tot_bha_5981689.json", "r", encoding="utf-8") as fp:
    d = json.load(fp)

pstats = d.get("content", {}).get("playerStats", {})
for pid, pdata in pstats.items():
    if "Pelova" in pdata.get("name", ""):
        print("Pelova stats object keys:", pdata.keys())
        shotmap = pdata.get("shotmap", [])
        print("Shotmap:", shotmap)
        # check if events or periods exist
        for sec in pdata.get("stats", []):
            print(sec.get("title"), ":", [f"{k}: {v.get('stat', {}).get('value')}" for k, v in sec.get("stats", {}).items() if 'touch' in k.lower() or 'pass' in k.lower()])

