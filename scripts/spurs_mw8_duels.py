import json
from pathlib import Path

# 1. Check all Spurs players in Birmingham vs Spurs (MW8)
with open("scratch_bir_tot.json", "r", encoding="utf-8") as f:
    d = json.load(f)

ps = d['content'].get('playerStats', {})
id_to_name = {}
lineup = d['content']['lineup']['awayTeam'] # Spurs is awayTeam
starters = lineup.get('starters', [])
subs = lineup.get('subs', [])
for p in starters + subs:
    id_to_name[str(p.get('id'))] = (p.get('name'), p in starters, p.get('positionStringShort'))

print("=== SPURS vs BIRMINGHAM (MW8): DISPOSSESSED & DUELS LOST ===")
print(f"{'Player':<24} {'Pos':<5} {'Role':<8} {'Dispossessed':<14} {'Duels Lost':<12} {'Duels Won':<12} {'Total Duels':<12} {'Win %':<8}")
print("-" * 100)

for p in starters + subs:
    pid = str(p.get('id'))
    stats = ps.get(pid, {})
    pname = p.get('name')
    is_starter = "Starter" if p in starters else "Sub"
    pos = p.get('positionStringShort') or ""
    
    # Extract dispossessed & duels
    dispossessed = 0
    duels_lost = 0
    duels_won = 0
    
    for grp in stats.get('stats', []):
        st = grp.get('stats', {})
        if "Dispossessed" in st:
            v = st["Dispossessed"]
            dispossessed = v.get("stat", {}).get("value") if isinstance(v, dict) else v
        if "Duels lost" in st:
            v = st["Duels lost"]
            duels_lost = v.get("stat", {}).get("value") if isinstance(v, dict) else v
        if "Duels won" in st:
            v = st["Duels won"]
            duels_won = v.get("stat", {}).get("value") if isinstance(v, dict) else v
            
    dispossessed = dispossessed or 0
    duels_lost = duels_lost or 0
    duels_won = duels_won or 0
    total_duels = duels_won + duels_lost
    win_pct = f"{round(duels_won / total_duels * 100)}%" if total_duels > 0 else "-"
    
    print(f"{pname:<24} {pos:<5} {is_starter:<8} {dispossessed:<14} {duels_lost:<12} {duels_won:<12} {total_duels:<12} {win_pct:<8}")

