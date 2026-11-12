import json

def inspect_team_lineup(file_path, is_home=True):
    with open(file_path, "r", encoding="utf-8") as f:
        d = json.load(f)
    lineup = d.get("content", {}).get("lineup", {})
    t = lineup.get("homeTeam" if is_home else "awayTeam", {})
    print(f"\n--- {t.get('name')} Formation: {t.get('formation')} ---")
    for p in t.get("starters", []):
        name = p.get("name")
        if isinstance(name, dict):
            name = name.get("fullName", name.get("name"))
        print(f"  {name} | pos: {p.get('position')} | role: {p.get('role')} | id: {p.get('id')}")
    print("Subs:")
    for p in t.get("subs", []):
        name = p.get("name")
        if isinstance(name, dict):
            name = name.get("fullName", name.get("name"))
        print(f"  {name} | id: {p.get('id')}")

print("=== MANCHESTER UNITED ===")
inspect_team_lineup("scratch_mun_whu.json", is_home=True)

print("=== LCL LINEUP ===")
inspect_team_lineup("scratch_lcl_bha.json", is_home=True)
