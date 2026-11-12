"""
Tottenham Hotspur Women - Defensive Unit Comprehensive Deep-Dive
==================================================================
Fetches all detailed metrics, percentiles, traits, and playing profiles
for every defender in the 2026/2027 squad from FotMob:
1. Alice Sombath (1214575)
2. Caitlin Dijkstra (1215012)
3. Clare Hunt (1453078)
4. Tōko Koga (1627765)
5. Amanda Nildén (1050882)
6. Ella Morris (1257462)
7. Hanna Wijk (1214582)
8. Julie Blakstad (1031793)
9. Luana Bühler (888364)
10. Josefine Rybrink (887268)

Saves output to: `_data/tottenham_defenders_comparison.json`
"""

import json
from pathlib import Path
from fotmob_api_client import FotMobAPIClient

client = FotMobAPIClient()

DEFENDERS = [
    {"id": 1214575, "name": "Alice Sombath", "name_he": "אליס סומבאת", "primary_role": "CB / RB / LB (רכש מליון)"},
    {"id": 1215012, "name": "Caitlin Dijkstra", "name_he": "קייטלין דייקסטרה", "primary_role": "CB (רכש מוולפסבורג)"},
    {"id": 1453078, "name": "Clare Hunt", "name_he": "קלייר האנט", "primary_role": "CB"},
    {"id": 1627765, "name": "Tōko Koga", "name_he": "טוקו קוגה", "primary_role": "CB / Anchor"},
    {"id": 1050882, "name": "Amanda Nildén", "name_he": "אמנדה נילדן", "primary_role": "LB / LWB"},
    {"id": 1257462, "name": "Ella Morris", "name_he": "אלה מוריס", "primary_role": "RB / RWB"},
    {"id": 1214582, "name": "Hanna Wijk", "name_he": "חנה וייק", "primary_role": "RB / RWB (האקן/שוודיה)"},
    {"id": 1031793, "name": "Julie Blakstad", "name_he": "ז'ולי בלקסטאד", "primary_role": "LWB / LB / Winger"},
    {"id": 888364, "name": "Luana Bühler", "name_he": "לואנה ביהלר", "primary_role": "CB"},
    {"id": 887268, "name": "Josefine Rybrink", "name_he": "יוזפין רייברינק", "primary_role": "CB / RB"}
]

def fetch_defenders_data():
    results = []
    
    for d in DEFENDERS:
        pname = d['name'].encode('ascii', 'ignore').decode('ascii')
        print(f"Fetching {pname} (ID: {d['id']})...")
        raw = client.fetch_player_raw(d["id"])
        if not raw:
            print(f" -> Failed to fetch {d['name']}")
            continue
            
        metrics = client.parse_player_metrics(raw)
        
        # Flatten stats
        def_stats = {}
        pass_stats = {}
        poss_stats = {}
        
        for sec in metrics.get("stats_sections", []):
            cat = sec.get("section", "").lower()
            for stat in sec.get("stats", []):
                key = stat.get("metric")
                data_point = {
                    "val": stat.get("stat_value"),
                    "per90": stat.get("per_90"),
                    "pct": stat.get("percentile_rank")
                }
                if "defend" in cat:
                    def_stats[key] = data_point
                elif "pass" in cat:
                    pass_stats[key] = data_point
                elif "possess" in cat:
                    poss_stats[key] = data_point

        profile = {
            "id": d["id"],
            "name": d["name"],
            "name_he": d["name_he"],
            "primary_role": d["primary_role"],
            "position_label": metrics.get("primary_position"),
            "traits": metrics.get("traits", []),
            "key_metrics": {
                # Defending
                "tackles_per90": def_stats.get("Tackles", {}).get("per90"),
                "tackles_pct": def_stats.get("Tackles", {}).get("pct"),
                "interceptions_per90": def_stats.get("Interceptions", {}).get("per90"),
                "interceptions_pct": def_stats.get("Interceptions", {}).get("pct"),
                "clearances_per90": def_stats.get("Clearances", {}).get("per90"),
                "clearances_pct": def_stats.get("Clearances", {}).get("pct"),
                "recoveries_per90": def_stats.get("Recoveries", {}).get("per90"),
                "recoveries_pct": def_stats.get("Recoveries", {}).get("pct"),
                "defensive_actions_per90": def_stats.get("Defensive actions", {}).get("per90"),
                "defensive_actions_pct": def_stats.get("Defensive actions", {}).get("pct"),
                "duels_won_pct": poss_stats.get("Duels won %", {}).get("per90"),
                "duels_won_percentile": poss_stats.get("Duels won %", {}).get("pct"),
                "aerials_won_pct": poss_stats.get("Aerials won %", {}).get("per90"),
                "aerials_won_percentile": poss_stats.get("Aerials won %", {}).get("pct"),
                # Passing & Progression
                "accurate_passes_per90": pass_stats.get("Accurate passes", {}).get("per90"),
                "pass_accuracy": pass_stats.get("Pass accuracy", {}).get("per90"),
                "pass_accuracy_pct": pass_stats.get("Pass accuracy", {}).get("pct"),
                "accurate_long_balls_per90": pass_stats.get("Accurate long balls", {}).get("per90"),
                "accurate_long_balls_pct": pass_stats.get("Accurate long balls", {}).get("pct"),
                "long_ball_accuracy": pass_stats.get("Long ball accuracy", {}).get("per90"),
                "long_ball_accuracy_pct": pass_stats.get("Long ball accuracy", {}).get("pct"),
                # Attacking support
                "chances_created_per90": pass_stats.get("Chances created", {}).get("per90"),
                "chances_created_pct": pass_stats.get("Chances created", {}).get("pct"),
                "successful_crosses_per90": pass_stats.get("Successful crosses", {}).get("per90"),
                "successful_crosses_pct": pass_stats.get("Successful crosses", {}).get("pct"),
                "touches_per90": poss_stats.get("Touches", {}).get("per90"),
                "touches_pct": poss_stats.get("Touches", {}).get("pct")
            }
        }
        results.append(profile)
        print(f" -> OK: {pname} processed.")

    out_file = Path("_data/tottenham_defenders_comparison.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved all defenders comparison data -> {out_file}")

if __name__ == "__main__":
    fetch_defenders_data()
