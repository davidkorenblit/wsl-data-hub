#!/usr/bin/env python3
"""
Extract Matchweek 5 Post Metrics
================================
Extracts deep tactical metrics for:
1. Tottenham vs London City Lionesses (Goal 3 events, Alexia, Geyoro, VdD, Diani, Spurs press breakdown)
2. Man City vs Arsenal (Baum stats, Casparij goal xG, Russo goal, minute 1-60 vs 60-90 splits)
3. Brighton vs Charlton (xG vs Goals, Charlton conceded stats)
4. Man United vs Liverpool (Defensive metrics, clean sheet)
"""

import json
import sys
from pathlib import Path

# Fix Windows console UTF-8 output
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROJECT_ROOT = Path(__file__).resolve().parent.parent

def load_json(name):
    p = PROJECT_ROOT / name
    if not p.exists():
        p = PROJECT_ROOT / "data" / "raw" / "fotmob" / "matches" / f"{name}.json"
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

def analyze_tot_lcl():
    print("=" * 70)
    print(" 1. TOTTENHAM HOTSPUR vs LONDON CITY LIONESSES (1 - 6)")
    print("=" * 70)
    data = load_json("scratch_tot_lcl.json")
    if not data:
        print(" [!] scratch_tot_lcl.json not found")
        return

    content = data.get("content", {})
    facts = content.get("matchFacts", {})
    events = facts.get("events", {}).get("events", [])
    
    print("\n--- Event Timeline & Goals ---")
    for e in events:
        time_str = f"{e.get('time')}'"
        e_type = e.get("type")
        if e_type in ["Goal", "Card", "Substitution"]:
            player = e.get("player", {}).get("name", "")
            assist = e.get("assist", {}).get("name")
            extra = f" (Assist: {assist})" if assist else ""
            swap = e.get("swap", [{}])
            sub_in = swap[0].get("name", "") if (e_type == "Substitution" and swap) else ""
            desc = f"{player} -> {sub_in}" if sub_in else f"{player}{extra}"
            print(f"  [{time_str}] {e_type}: {desc}")

    # Inspect Shotmap for Goal 3 (approx min 33-35)
    shotmap = content.get("shotmap", {}).get("shots", [])
    print("\n--- Shotmap / Key Shots ---")
    for s in shotmap:
        min_shot = s.get("min")
        p_name = s.get("playerName")
        is_goal = s.get("eventType") == "Goal"
        xg = s.get("expectedGoals")
        shot_type = s.get("shotType")
        if is_goal or (min_shot and 30 <= min_shot <= 36):
            print(f"  Min {min_shot}' | {p_name} | Goal={is_goal} | xG={xg:.3f} | Type={shot_type}")

    # Player stats from playerStats
    pstats = content.get("playerStats", {})
    players_to_track = [
        "Putellas", "Geyoro", "Donk", "Diani", 
        "Wienroither", "Blakstad", "Tandberg", "Gaupset", 
        "Pelova", "Spence", "Nildén", "Kop", "Bühler", "Dijkstra", "Cascarino"
    ]
    
    print("\n--- Key Player Ratings & Stats ---")
    for pid, pdata in pstats.items():
        name = pdata.get("name", "")
        if any(target.lower() in name.lower() for target in players_to_track):
            flat = get_player_stats_flat(pdata)
            rating = pdata.get("rating", {}).get("num") if isinstance(pdata.get("rating"), dict) else pdata.get("rating")
            print(f"\n* {name} - FotMob Rating: {rating}")
            keys_to_show = [
                "Minutes played", "Goals", "Assists", "Total shots", "Expected goals (xG)",
                "Expected assists (xA)", "Accurate passes", "Chances created", "Touches",
                "Touches in opposition box", "Successful dribbles", "Tackles won", "Interceptions",
                "Recoveries", "Clearances", "Ground duels won", "Aerial duels won", "Possession lost", "Defensive actions"
            ]
            for k in keys_to_show:
                if k in flat and flat[k] is not None:
                    print(f"    - {k}: {flat[k]}")

def analyze_mci_ars():
    print("\n" + "=" * 70)
    print(" 2. MANCHESTER CITY vs ARSENAL (4 - 2)")
    print("=" * 70)
    data = load_json("scratch_mci_ars.json")
    if not data:
        print(" [!] scratch_mci_ars.json not found")
        return

    content = data.get("content", {})
    shotmap = content.get("shotmap", {}).get("shots", [])
    
    print("\n--- Goals & High-Value / Wonder Shots ---")
    for s in shotmap:
        min_shot = s.get("min")
        p_name = s.get("playerName")
        is_goal = s.get("eventType") == "Goal"
        xg = s.get("expectedGoals")
        xgot = s.get("expectedGoalsOnTarget")
        shot_type = s.get("shotType")
        if is_goal:
            print(f"  GOAL: Min {min_shot}' | {p_name} | xG={xg} | xGOT={xgot} | Type={shot_type}")

    # Inspect Casparij shot specifically
    for s in shotmap:
        if "casparij" in s.get("playerName", "").lower():
            print(f"  -> Casparij Shot: Min {s.get('min')}' | xG={s.get('expectedGoals')} | xGOT={s.get('expectedGoalsOnTarget')} | isGoal={s.get('eventType') == 'Goal'}")

    # Timeline of subs
    events = content.get("matchFacts", {}).get("events", {}).get("events", [])
    print("\n--- Substitutions Timeline ---")
    for e in events:
        if e.get("type") == "Substitution":
            time_str = f"{e.get('time')}'"
            team = "Home (MCI)" if e.get("isHome") else "Away (ARS)"
            swap = e.get("swap", [{}])[0]
            player_out = e.get("player", {}).get("name", "")
            player_in = swap.get("name", "")
            print(f"  [{time_str}] {team}: OFF {player_out} -> ON {player_in}")

    # Lineup / Player Stats (Baum, Russo, Stanway, Blackstenius, Hasegawa, Shaw, Hemp)
    pstats = content.get("playerStats", {})
    tracked = ["Baum", "Russo", "Stanway", "Hasegawa", "Hemp", "Shaw", "Casparij", "Fowler"]
    
    print("\n--- Player Stats (Baum, Russo, Stanway, etc.) ---")
    for pid, pdata in pstats.items():
        name = pdata.get("name", "")
        if any(t.lower() in name.lower() for t in tracked):
            flat = get_player_stats_flat(pdata)
            rating = pdata.get("rating", {}).get("num") if isinstance(pdata.get("rating"), dict) else pdata.get("rating")
            print(f"\n* {name} - Rating: {rating}")
            keys_to_show = [
                "Minutes played", "Goals", "Assists", "Total shots", "Expected goals (xG)",
                "Expected assists (xA)", "Accurate passes", "Chances created", "Touches",
                "Successful dribbles", "Tackles won", "Possession lost", "Recoveries", "Clearances"
            ]
            for k in keys_to_show:
                if k in flat and flat[k] is not None:
                    print(f"    - {k}: {flat[k]}")

def analyze_bha_cha():
    print("\n" + "=" * 70)
    print(" 3. BRIGHTON vs CHARLTON (5 - 1)")
    print("=" * 70)
    data = load_json("scratch_bha_cha.json")
    if not data:
        print(" [!] scratch_bha_cha.json not found")
        return

    content = data.get("content", {})
    stats = {}
    for grp in content.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
        for s in grp.get("stats", []):
            stats[s.get("title") or s.get("key")] = s.get("stats")

    print(f"  Final Score: Brighton 5 - 1 Charlton")
    print(f"  xG: Brighton {stats.get('Expected goals (xG)', ['-'])[0]} vs Charlton {stats.get('Expected goals (xG)', ['-', '-'])[1]}")
    print(f"  Shots: Brighton {stats.get('Total shots', ['-'])[0]} vs Charlton {stats.get('Total shots', ['-', '-'])[1]}")
    print(f"  Shots on target: Brighton {stats.get('Shots on target', ['-'])[0]} vs Charlton {stats.get('Shots on target', ['-', '-'])[1]}")
    print(f"  Big chances: Brighton {stats.get('Big chances', ['-'])[0]} vs Charlton {stats.get('Big chances', ['-', '-'])[1]}")

def analyze_mun_liv():
    print("\n" + "=" * 70)
    print(" 4. MANCHESTER UNITED vs LIVERPOOL (1 - 0)")
    print("=" * 70)
    data = load_json("scratch_mun_liv.json")
    if not data:
        return
    content = data.get("content", {})
    stats = {}
    for grp in content.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", []):
        for s in grp.get("stats", []):
            stats[s.get("title") or s.get("key")] = s.get("stats")
    print(f"  Final Score: Man Utd 1 - 0 Liverpool")
    print(f"  xG: Man Utd {stats.get('Expected goals (xG)', ['-'])[0]} vs Liverpool {stats.get('Expected goals (xG)', ['-', '-'])[1]}")
    print(f"  Shots: Man Utd {stats.get('Total shots', ['-'])[0]} vs Liverpool {stats.get('Total shots', ['-', '-'])[1]}")
    print(f"  Big chances: Man Utd {stats.get('Big chances', ['-'])[0]} vs Liverpool {stats.get('Big chances', ['-', '-'])[1]}")

if __name__ == "__main__":
    analyze_tot_lcl()
    analyze_mci_ars()
    analyze_bha_cha()
    analyze_mun_liv()
