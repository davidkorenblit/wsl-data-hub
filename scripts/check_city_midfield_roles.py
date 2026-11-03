import json

with open("scratch_lcl_mci.json", "r", encoding="utf-8") as f:
    d = json.load(f)

ps = d['content'].get('playerStats', {})
id_to_name = {
    "1131573": "Laura Blindkilde",
    "829874": "Yui Hasegawa",
    "1442299": "Aoba Fujino",
    "1182840": "Grace Clinton",
    "1055684": "Mary Fowler",
    "888145": "Lauren Hemp"
}

for pid, name in id_to_name.items():
    st = ps.get(pid, {})
    print(f"\n=== {name} ===")
    for grp in st.get('stats', []):
        for k, v in grp.get('stats', {}).items():
            val = v.get('stat', {}).get('value') if isinstance(v, dict) else v
            if any(term in k.lower() for term in ['rating', 'minutes', 'touches', 'pass', 'tackle', 'chance', 'cross', 'shot', 'duel', 'dispossessed', 'third']):
                print(f"  {k}: {val}")

