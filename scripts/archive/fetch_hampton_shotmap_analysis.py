import requests
import json

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

url = "https://www.fotmob.com/api/data/playerData?id=1081975"
res = requests.get(url, headers=HEADERS, timeout=15)
data = res.json()

with open("_data/hampton_fotmob_raw.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("=== Hannah Hampton FotMob Analysis ===")
traits = data.get("traits", {}).get("items", [])
print("Traits:")
for t in traits:
    print(f"  {t.get('title')}: {round(t.get('value', 0)*100)}%")

stats_sections = data.get("firstSeasonStats", {}).get("statsSection", {}).get("items", [])
for sec in stats_sections:
    print(f"\n--- {sec.get('title')} ---")
    for item in sec.get("items", []):
        print(f"  {item.get('title')}: {item.get('statValue')} (per90: {item.get('per90')}, pct: {item.get('percentileRankPer90')}%)")

shotmap = data.get("firstSeasonStats", {}).get("shotmap", [])
print(f"\nShotmap entries: {len(shotmap)}")

situations = {}
event_types = {}
goals_breakdown = []
high_xg_saves = []

for s in shotmap:
    sit = s.get("situation", "Unknown")
    situations[sit] = situations.get(sit, 0) + 1
    
    evt = s.get("eventType", "Unknown")
    event_types[evt] = event_types.get(evt, 0) + 1
    
    xg = s.get("expectedGoals", 0)
    xgot = s.get("expectedGoalsOnTarget", 0)
    
    if evt == "Goal":
        goals_breakdown.append({
            "min": s.get("min"),
            "situation": sit,
            "shotType": s.get("shotType"),
            "isFromInsideBox": s.get("isFromInsideBox"),
            "xg": xg,
            "xgot": xgot,
            "matchId": s.get("matchId")
        })
    elif evt in ["AttemptSaved", "SavedOffLine"] and (xg > 0.25 or xgot > 0.4):
        high_xg_saves.append({
            "min": s.get("min"),
            "situation": sit,
            "shotType": s.get("shotType"),
            "isFromInsideBox": s.get("isFromInsideBox"),
            "xg": xg,
            "xgot": xgot,
            "matchId": s.get("matchId")
        })

print("\nSituations breakdown across all shots faced:")
for sit, count in situations.items():
    print(f"  {sit}: {count}")

print(f"\nGoals conceded in shotmap ({len(goals_breakdown)}):")
for g in goals_breakdown:
    print(f"  Min {g['min']} | Sit: {g['situation']} | InsideBox: {g['isFromInsideBox']} | Type: {g['shotType']} | xG: {round(g['xg'], 2)} | xGOT: {round(g['xgot'], 2)}")

print(f"\nBig saves / High xG shots saved by Hampton ({len(high_xg_saves)}):")
for sv in high_xg_saves:
    print(f"  Min {sv['min']} | Sit: {sv['situation']} | InsideBox: {sv['isFromInsideBox']} | Type: {sv['shotType']} | xG: {round(sv['xg'], 2)} | xGOT: {round(sv['xgot'], 2)}")
