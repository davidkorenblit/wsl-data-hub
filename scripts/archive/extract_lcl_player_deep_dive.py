import json
from pathlib import Path

MATCHES_DIR = Path("data/raw/fotmob/matches")

MATCH_FILES = [
    ("MW1", MATCHES_DIR / "mw1_lcl_mun_5981531.json"),
    ("MW2", MATCHES_DIR / "mw2_whu_lcl_5981634.json"),
    ("MW3", MATCHES_DIR / "mw3_cha_lcl_5981642.json"),
    ("MW4", MATCHES_DIR / "mw4_lcl_bha_5981649.json"),
    ("MW5", MATCHES_DIR / "mw5_tot_lcl_5981655.json"),
]

def get_player_stats(needle):
    records = []
    for rnd, fpath in MATCH_FILES:
        with open(fpath, "r", encoding="utf-8") as fp:
            d = json.load(fp)
        pstats = d.get("content", {}).get("playerStats", {})
        for pid, pdata in pstats.items():
            name = pdata.get("name", "")
            if needle.lower() in name.lower():
                stat_map = {"round": rnd, "name": name}
                for cat in pdata.get("stats", []):
                    for sk, sv in cat.get("stats", {}).items():
                        st = sv.get("stat", {})
                        stat_map[sk] = st.get("value", 0)
                        if "total" in st:
                            stat_map[f"{sk}_total"] = st.get("total", 0)
                records.append(stat_map)
                break
    return records

print("=" * 80)
print("DEEP DIVE: ALEXIA PUTELLAS")
print("=" * 80)
alexia = get_player_stats("Putellas")
for r in alexia:
    print(r.get("round"), "Min:", r.get("Minutes played"), "G:", r.get("Goals"), "A:", r.get("Assists"), "xG:", r.get("Expected goals (xG)"), "Shots:", r.get("Total shots"), "Chances:", r.get("Chances created"), "PassAcc:", f"{r.get('Accurate passes')}/{r.get('Accurate passes_total')}", "Rec:", r.get("Recoveries"), "Itc:", r.get("Interceptions"), "TacklesWon:", r.get("Tackles won"), "GDuelsWon:", f"{r.get('Ground duels won')}/{r.get('Ground duels won_total')}", "Rating:", r.get("FotMob rating"))

print("\n" + "=" * 80)
print("DEEP DIVE: DANIELLE VAN DE DONK")
print("=" * 80)
dvdd = get_player_stats("Donk")
for r in dvdd:
    print(r.get("round"), "Min:", r.get("Minutes played"), "G:", r.get("Goals"), "A:", r.get("Assists"), "xG:", r.get("Expected goals (xG)"), "Shots:", r.get("Total shots"), "Chances:", r.get("Chances created"), "PassAcc:", f"{r.get('Accurate passes')}/{r.get('Accurate passes_total')}", "Rec:", r.get("Recoveries"), "Itc:", r.get("Interceptions"), "TacklesWon:", r.get("Tackles won"), "GDuelsWon:", f"{r.get('Ground duels won')}/{r.get('Ground duels won_total')}", "Rating:", r.get("FotMob rating"))

print("\n" + "=" * 80)
print("DEEP DIVE: DEFENSIVE PILLARS (Mapi León & Saki Kumagai)")
print("=" * 80)
mapi = get_player_stats("León")
print("Mapi León:")
for r in mapi:
    print(r.get("round"), "Min:", r.get("Minutes played"), "Clearances:", r.get("Clearances"), "Itc:", r.get("Interceptions"), "Rec:", r.get("Recoveries"), "TacklesWon:", r.get("Tackles won"), "AerialWon:", f"{r.get('Aerial duels won')}/{r.get('Aerial duels won_total')}", "Rating:", r.get("FotMob rating"))

kumagai = get_player_stats("Kumagai")
print("\nSaki Kumagai:")
for r in kumagai:
    print(r.get("round"), "Min:", r.get("Minutes played"), "Clearances:", r.get("Clearances"), "Itc:", r.get("Interceptions"), "Rec:", r.get("Recoveries"), "TacklesWon:", r.get("Tackles won"), "AerialWon:", f"{r.get('Aerial duels won')}/{r.get('Aerial duels won_total')}", "Rating:", r.get("FotMob rating"))

# Export to _data/lcl_mw5_deep_analysis.json
export_data = {
    "team_matches": json.load(open("_data/lcl_matches_analyzed.json", "r", encoding="utf-8")),
    "alexia_putellas": alexia,
    "danielle_van_de_donk": dvdd,
    "mapi_leon": mapi,
    "saki_kumagai": kumagai
}
with open("_data/lcl_mw5_deep_analysis.json", "w", encoding="utf-8") as fp:
    json.dump(export_data, fp, indent=2, ensure_ascii=False)
print("\nSaved _data/lcl_mw5_deep_analysis.json successfully.")
