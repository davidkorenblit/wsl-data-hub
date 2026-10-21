#!/usr/bin/env python3
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path("c:/Users/david/wsl_data_for_posts/wsl-data-hub")

def load_json(name):
    p = PROJECT_ROOT / name
    if not p.exists():
        p = PROJECT_ROOT / f"scratch_{name}.json"
    if p.exists():
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def get_player_stats_flat(pdata):
    res = {}
    for cat in pdata.get("stats", []):
        cat_stats = cat.get("stats", {})
        if isinstance(cat_stats, dict):
            for k, v in cat_stats.items():
                stat_obj = v.get("stat", {})
                val = stat_obj.get("value")
                total = stat_obj.get("total")
                if total is not None:
                    res[k] = f"{val}/{total}"
                else:
                    res[k] = val
    return res

output_lines = []

def log(msg=""):
    output_lines.append(str(msg))

def fmt_num(val):
    if val is None:
        return "-"
    if isinstance(val, (int, float)):
        return f"{val:.3f}"
    return str(val)

# ==========================================
# 1. CHELSEA VS TOTTENHAM (scratch_che_tot)
# ==========================================
log("=" * 70)
log("1. CHELSEA VS TOTTENHAM (scratch_che_tot.json)")
log("=" * 70)
che_tot = load_json("scratch_che_tot.json")
if che_tot:
    content = che_tot.get("content", {})
    # Team stats
    stats_dict = {}
    for grp in content.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
        for s in grp.get("stats", []):
            stats_dict[s.get("title") or s.get("key")] = s.get("stats")
    log(f"xG: {stats_dict.get('Expected goals (xG)')}")
    log(f"Shots: {stats_dict.get('Total shots')} | On target: {stats_dict.get('Shots on target')}")
    log(f"Big chances: {stats_dict.get('Big chances')}")
    log(f"Possession: {stats_dict.get('Ball possession')}%")

    # Goals from shotmap
    log("\n--- GOALS & XG ---")
    for s in content.get("shotmap", {}).get("shots", []):
        if s.get("eventType") == "Goal":
            log(f"Goal: {s.get('playerName')} {s.get('min')}' | xG: {fmt_num(s.get('expectedGoals'))} | xGOT: {fmt_num(s.get('expectedGoalsOnTarget'))} | type: {s.get('shotType')}")

    # Players
    log("\n--- KEY PLAYERS STATS ---")
    pstats = content.get("playerStats", {})
    targets = ["Hampton", "Carpenter", "James", "Hamano", "Nüsken", "Thompson", 
               "Holdt", "Vinberg", "Vangsgaard", "Bruun", "Blakstad", "Tilly", "Koga", "Ahtinen", "Summanen"]
    for pid, pdata in pstats.items():
        name = pdata.get("name", "")
        if any(t.lower() in name.lower() for t in targets):
            flat = get_player_stats_flat(pdata)
            rating = pdata.get("rating", {}).get("num") if isinstance(pdata.get("rating"), dict) else pdata.get("rating")
            log(f"\n* {name} (Rating: {rating}):")
            for k in ["Minutes played", "Goals", "Assists", "Expected goals (xG)", "Total shots", 
                      "Accurate passes", "Long balls", "Accurate long balls", "Passes into final third",
                      "Chances created", "Touches", "Touches in opposition box", "Dispossessed", 
                      "Possession lost", "Tackles won", "Interceptions", "Clearances", 
                      "Ground duels won", "Aerial duels won", "Saves", "Goals conceded"]:
                if k in flat:
                    log(f"    - {k}: {flat[k]}")

# ==========================================
# 2. ARSENAL VS BIRMINGHAM (scratch_ars_bir)
# ==========================================
log("\n" + "=" * 70)
log("2. ARSENAL VS BIRMINGHAM CITY (scratch_ars_bir.json)")
log("=" * 70)
ars_bir = load_json("scratch_ars_bir.json")
if ars_bir:
    content = ars_bir.get("content", {})
    stats_dict = {}
    for grp in content.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
        for s in grp.get("stats", []):
            stats_dict[s.get("title") or s.get("key")] = s.get("stats")
    log(f"Score: 1 - 1")
    log(f"xG: {stats_dict.get('Expected goals (xG)')}")
    log(f"Shots: {stats_dict.get('Total shots')} | On target: {stats_dict.get('Shots on target')}")
    log(f"Big chances: {stats_dict.get('Big chances')} | Big chances missed: {stats_dict.get('Big chances missed')}")
    log(f"Possession: {stats_dict.get('Ball possession')}%")
    log("\n--- GOALS & SHOTS ---")
    for s in content.get("shotmap", {}).get("shots", []):
        if s.get("eventType") == "Goal":
            log(f"Goal: {s.get('playerName')} {s.get('min')}' | xG: {fmt_num(s.get('expectedGoals'))} | xGOT: {fmt_num(s.get('expectedGoalsOnTarget'))}")
    
    log("\n--- ARSENAL KEY PLAYERS ---")
    pstats = ars_bir.get("content", {}).get("playerStats", {})
    for pid, pdata in pstats.items():
        name = pdata.get("name", "")
        if any(t.lower() in name.lower() for t in ["Russo", "Smith", "Baum", "Vallotto", "Mead"]):
            flat = get_player_stats_flat(pdata)
            rating = pdata.get("rating", {}).get("num") if isinstance(pdata.get("rating"), dict) else pdata.get("rating")
            log(f"\n* {name} (Rating: {rating}):")
            for k in ["Minutes played", "Goals", "Assists", "Expected goals (xG)", "Total shots", "Accurate passes", "Chances created", "Touches in opposition box", "Dispossessed", "Possession lost"]:
                if k in flat:
                    log(f"    - {k}: {flat[k]}")

# ==========================================
# 3. CHARLTON VS MAN UNITED (scratch_cha_mun)
# ==========================================
log("\n" + "=" * 70)
log("3. CHARLTON VS MANCHESTER UNITED (scratch_cha_mun.json)")
log("=" * 70)
cha_mun = load_json("scratch_cha_mun.json")
if cha_mun:
    content = cha_mun.get("content", {})
    stats_dict = {}
    for grp in content.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
        for s in grp.get("stats", []):
            stats_dict[s.get("title") or s.get("key")] = s.get("stats")
    log(f"Score: 1 - 3")
    log(f"xG: {stats_dict.get('Expected goals (xG)')}")
    log(f"Shots: {stats_dict.get('Total shots')} | On target: {stats_dict.get('Shots on target')}")
    log(f"Big chances: {stats_dict.get('Big chances')}")
    log(f"Possession: {stats_dict.get('Ball possession')}%")
    log("\n--- GOALS & MINUTES ---")
    for s in content.get("shotmap", {}).get("shots", []):
        if s.get("eventType") == "Goal":
            log(f"Goal: {s.get('playerName')} {s.get('min')}' | xG: {fmt_num(s.get('expectedGoals'))} | xGOT: {fmt_num(s.get('expectedGoalsOnTarget'))}")

    log("\n--- MAN UNITED PLAYERS ---")
    pstats = content.get("playerStats", {})
    for pid, pdata in pstats.items():
        name = pdata.get("name", "")
        if any(t.lower() in name.lower() for t in ["Toone", "Park", "Terland", "Riviere", "Tullis-Joyce", "Malard"]):
            flat = get_player_stats_flat(pdata)
            rating = pdata.get("rating", {}).get("num") if isinstance(pdata.get("rating"), dict) else pdata.get("rating")
            log(f"\n* {name} (Rating: {rating}):")
            for k in ["Minutes played", "Goals", "Assists", "Expected goals (xG)", "Total shots", "Accurate passes", "Chances created", "Successful dribbles", "Touches", "Dispossessed", "Possession lost"]:
                if k in flat:
                    log(f"    - {k}: {flat[k]}")

# ==========================================
# 4. ASTON VILLA VS LIVERPOOL (scratch_avl_liv)
# ==========================================
log("\n" + "=" * 70)
log("4. ASTON VILLA VS LIVERPOOL (scratch_avl_liv.json)")
log("=" * 70)
avl_liv = load_json("scratch_avl_liv.json")
if avl_liv:
    content = avl_liv.get("content", {})
    stats_dict = {}
    for grp in content.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
        for s in grp.get("stats", []):
            stats_dict[s.get("title") or s.get("key")] = s.get("stats")
    log(f"Score: 2 - 1")
    log(f"xG: {stats_dict.get('Expected goals (xG)')}")
    log(f"Shots: {stats_dict.get('Total shots')} | On target: {stats_dict.get('Shots on target')}")
    log(f"Big chances: {stats_dict.get('Big chances')} | Big chances missed: {stats_dict.get('Big chances missed')}")
    log(f"Possession: {stats_dict.get('Ball possession')}%")
    log("\n--- GOALS ---")
    for s in content.get("shotmap", {}).get("shots", []):
        if s.get("eventType") == "Goal":
            log(f"Goal: {s.get('playerName')} {s.get('min')}' | xG: {fmt_num(s.get('expectedGoals'))} | xGOT: {fmt_num(s.get('expectedGoalsOnTarget'))}")

    pstats = content.get("playerStats", {})
    for pid, pdata in pstats.items():
        name = pdata.get("name", "")
        if any(g in name.lower() for g in ["keating", "d'angelo", "micah", "laws"]):
            flat = get_player_stats_flat(pdata)
            rating = pdata.get("rating", {}).get("num") if isinstance(pdata.get("rating"), dict) else pdata.get("rating")
            log(f"\n* Goalkeeper {name} (Rating: {rating}):")
            for k in ["Minutes played", "Saves", "Goals conceded", "Accurate passes", "Long balls", "Accurate long balls"]:
                if k in flat:
                    log(f"    - {k}: {flat[k]}")

# ==========================================
# 5. MAN CITY VS BRIGHTON (scratch_mci_bha)
# ==========================================
log("\n" + "=" * 70)
log("5. MANCHESTER CITY VS BRIGHTON (scratch_mci_bha.json)")
log("=" * 70)
mci_bha = load_json("scratch_mci_bha.json")
if mci_bha:
    content = mci_bha.get("content", {})
    stats_dict = {}
    for grp in content.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
        for s in grp.get("stats", []):
            stats_dict[s.get("title") or s.get("key")] = s.get("stats")
    log(f"Score: 3 - 2")
    log(f"xG: {stats_dict.get('Expected goals (xG)')}")
    log(f"Shots: {stats_dict.get('Total shots')} | On target: {stats_dict.get('Shots on target')}")
    log(f"Big chances: {stats_dict.get('Big chances')}")
    log(f"Possession: {stats_dict.get('Ball possession')}%")
    log("\n--- GOALS ---")
    for s in content.get("shotmap", {}).get("shots", []):
        if s.get("eventType") == "Goal":
            log(f"Goal: {s.get('playerName')} {s.get('min')}' | xG: {fmt_num(s.get('expectedGoals'))} | xGOT: {fmt_num(s.get('expectedGoalsOnTarget'))}")

    log("\n--- MAN CITY / BRIGHTON PLAYERS ---")
    pstats = content.get("playerStats", {})
    for pid, pdata in pstats.items():
        name = pdata.get("name", "")
        if any(t.lower() in name.lower() for t in ["Hemp", "Clinton", "Shaw", "Nnadozie", "Knaak", "Miedema", "Mead"]):
            flat = get_player_stats_flat(pdata)
            rating = pdata.get("rating", {}).get("num") if isinstance(pdata.get("rating"), dict) else pdata.get("rating")
            log(f"\n* {name} (Rating: {rating}):")
            for k in ["Minutes played", "Goals", "Assists", "Expected goals (xG)", "Expected assists (xA)", "Total shots", 
                      "Accurate passes", "Chances created", "Touches", "Touches in opposition box", 
                      "Successful dribbles", "Tackles won", "Interceptions", "Dispossessed", "Possession lost", "Saves", "Goals conceded"]:
                if k in flat:
                    log(f"    - {k}: {flat[k]}")

# ==========================================
# 6. CRYSTAL PALACE VS WEST HAM (scratch_cry_whu)
# ==========================================
log("\n" + "=" * 70)
log("6. CRYSTAL PALACE VS WEST HAM (scratch_cry_whu.json)")
log("=" * 70)
cry_whu = load_json("scratch_cry_whu.json")
if cry_whu:
    content = cry_whu.get("content", {})
    log("\n--- WEST HAM PLAYERS ---")
    pstats = content.get("playerStats", {})
    for pid, pdata in pstats.items():
        name = pdata.get("name", "")
        if any(t.lower() in name.lower() for t in ["og", "asseyi", "skeels", "denton", "piubel", "gorry", "szemik"]):
            flat = get_player_stats_flat(pdata)
            rating = pdata.get("rating", {}).get("num") if isinstance(pdata.get("rating"), dict) else pdata.get("rating")
            log(f"\n* {name} (Rating: {rating}):")
            for k in ["Minutes played", "Goals", "Assists", "Total shots", "Accurate passes", "Chances created", "Touches", "Tackles won", "Interceptions", "Clearances", "Ground duels won", "Aerial duels won"]:
                if k in flat:
                    log(f"    - {k}: {flat[k]}")

report_path = PROJECT_ROOT / "scripts" / "round6_report.txt"
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print(f"Report written to {report_path}")
