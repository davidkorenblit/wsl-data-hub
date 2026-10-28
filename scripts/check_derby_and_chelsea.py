import json
from pathlib import Path
import sys

PROJECT_ROOT = Path("c:/Users/david/wsl_data_for_posts/wsl-data-hub")

# 1. Clinton chance in mun_mci
with open(PROJECT_ROOT / "scratch_mun_mci.json", "r", encoding="utf-8") as f:
    mun_mci = json.load(f)

print("=== MANCHESTER DERBY SHOTS (Around min 75-95) ===")
for s in mun_mci.get("content", {}).get("shotmap", {}).get("shots", []):
    min_shot = s.get("min")
    pname = s.get("playerName", "")
    xg = s.get("expectedGoals")
    xgot = s.get("expectedGoalsOnTarget")
    stype = s.get("shotType")
    ev = s.get("eventType")
    if min_shot and min_shot >= 75:
        print(f"Min {min_shot}' | {pname} | Event: {ev} | xG: {xg} | xGOT: {xgot} | Type: {stype}")

# Also check all Clinton shots in match
print("\n--- All Grace Clinton shots & chances ---")
for s in mun_mci.get("content", {}).get("shotmap", {}).get("shots", []):
    if "clinton" in s.get("playerName", "").lower():
        print(f"Clinton: Min {s.get('min')}' | Event: {s.get('eventType')} | xG: {s.get('expectedGoals')} | xGOT: {s.get('expectedGoalsOnTarget')}")

# 2. Chelsea young fullback debut & Malard shots in cry_che
with open(PROJECT_ROOT / "scratch_cry_che.json", "r", encoding="utf-8") as f:
    cry_che = json.load(f)

print("\n=== CHELSEA SHOTS & MALARD MISSES ===")
for s in cry_che.get("content", {}).get("shotmap", {}).get("shots", []):
    if "malard" in s.get("playerName", "").lower():
        xg_val = s.get("expectedGoals")
        xg_str = f"{xg_val:.3f}" if xg_val is not None else "-"
        print(f"Malard: Min {s.get('min')}' | Event: {s.get('eventType')} | xG: {xg_str} | xGOT: {s.get('expectedGoalsOnTarget')}")

# Check Chelsea substitutions and starters for young debutant
print("\n=== CHELSEA LINEUP & SUBS ===")
events = cry_che.get("content", {}).get("matchFacts", {}).get("events", {}).get("events", [])
for e in events:
    if e.get("type") == "Substitution":
        swap = e.get("swap", [{}])
        player_in = swap[0].get("name") if swap else ""
        print(f"Sub Min {e.get('time')}: {e.get('player', {}).get('name')} -> {player_in}")

pstats = cry_che.get("content", {}).get("playerStats", {})
print("\nChelsea players in stats:")
for pid, p in pstats.items():
    if "chelsea" in p.get("teamName", "").lower():
        print(f"  {p.get('name')} (Minutes: {p.get('stats', [{}])[0].get('stats', {}).get('Minutes played', {}).get('stat', {}).get('value')})")

