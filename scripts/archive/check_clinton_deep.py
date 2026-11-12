import json

with open("scratch_lcl_mci.json", "r", encoding="utf-8") as f:
    d = json.load(f)

away = d['content']['lineup']['awayTeam']
print("Away Team (City) Formation:", away.get('formation'))

print("\n--- CITY STARTERS (with formation positions if available) ---")
for p in away.get('starters', []):
    print(f"Name: {p.get('name')}, Pos: {p.get('positionStringShort')}, Jersey: {p.get('jersey')}")

# Check lineup grid / rows if available
print("\n--- CITY LINEUP GRID ROWS ---")
for idx, row in enumerate(away.get('lineup', [])):
    pnames = [f"{p.get('name')} ({p.get('positionStringShort')})" for p in row]
    print(f"Row {idx+1}: {', '.join(pnames)}")

# Check Clinton full stats and ratings
ps = d['content'].get('playerStats', {})
clinton_id = "1182840"
clinton_stats = ps.get(clinton_id, {})
print("\n--- GRACE CLINTON FULL STATS ---")
for grp in clinton_stats.get('stats', []):
    print(f"\n[{grp.get('title')}]")
    for k, v in grp.get('stats', {}).items():
        val = v.get('stat', {}).get('value') if isinstance(v, dict) else v
        print(f"  {k}: {val}")

# Also check other midfielders: Yui Hasegawa, Laura Blindkilde, Aoba Fujino, etc.
print("\n--- ALL CITY PLAYERS RATINGS & POSITIONS ---")
for p in away.get('starters', []) + away.get('subs', []):
    pid = str(p.get('id'))
    p_st = ps.get(pid, {})
    rating = None
    mins = None
    for grp in p_st.get('stats', []):
        for k, v in grp.get('stats', {}).items():
            if k == "FotMob rating":
                rating = v.get('stat', {}).get('value') if isinstance(v, dict) else v
            if k == "Minutes played":
                mins = v.get('stat', {}).get('value') if isinstance(v, dict) else v
    print(f"  {p.get('name'):<24} (Mins: {str(mins):<4}, Rating: {str(rating):<6})")

