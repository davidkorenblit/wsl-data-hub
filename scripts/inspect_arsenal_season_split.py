"""
Detailed Match Timeline Analysis for Arsenal Women (WSL 2024/25)
Calculates:
1. First 5 matches vs Matches 6-22
2. First 8 matches vs Matches 9-22
3. Full chronological match log
"""

import json
from pathlib import Path

# Load FotMob overview data
overview_file = Path("data/raw/fotmob/leagues/league_9227_wsl_overview.json")
with open(overview_file, "r", encoding="utf-8") as f:
    league_data = json.load(f)

# Extract all matches
all_matches = league_data.get("matches", {}).get("allMatches", [])

arsenal_matches = []
for m in all_matches:
    home = m.get("home", {})
    away = m.get("away", {})
    status = m.get("status", {})
    
    h_name = home.get("name", "")
    a_name = away.get("name", "")
    
    if h_name == "Arsenal" or a_name == "Arsenal":
        # Extract score
        score_str = status.get("scoreStr", "")
        # Parse goals
        if "-" in score_str:
            parts = score_str.split("-")
            try:
                h_goals = int(parts[0].strip())
                a_goals = int(parts[1].strip())
            except:
                continue
        else:
            continue
            
        is_home = (h_name == "Arsenal")
        opp_name = a_name if is_home else h_name
        gf = h_goals if is_home else a_goals
        ga = a_goals if is_home else h_goals
        
        # Result and Points
        if gf > ga:
            res = "W"
            pts = 3
        elif gf == ga:
            res = "D"
            pts = 1
        else:
            res = "L"
            pts = 0
            
        match_round = m.get("round", "")
        date_utc = status.get("utcTime", "")
        
        arsenal_matches.append({
            "round": match_round,
            "date": date_utc,
            "is_home": is_home,
            "venue": "Home" if is_home else "Away",
            "opponent": opp_name,
            "score": f"{gf}-{ga}",
            "gf": gf,
            "ga": ga,
            "gd": gf - ga,
            "result": res,
            "pts": pts
        })

# Sort by date
arsenal_matches.sort(key=lambda x: x["date"])

print(f"Total Arsenal WSL matches parsed: {len(arsenal_matches)}")

# Print chronological log
print("\n=== CHRONOLOGICAL MATCH LOG ===")
for i, m in enumerate(arsenal_matches, 1):
    print(f"M{i:02d} | Date: {m['date'][:10]} | vs {m['opponent']:<18} ({m['venue']:<4}) | Score: {m['score']} ({m['result']}) | Pts: {m['pts']}")

def calc_split(matches, name):
    n = len(matches)
    if n == 0:
        return {}
    tot_pts = sum(m['pts'] for m in matches)
    tot_gf = sum(m['gf'] for m in matches)
    tot_ga = sum(m['ga'] for m in matches)
    tot_gd = tot_gf - tot_ga
    wins = sum(1 for m in matches if m['result'] == 'W')
    draws = sum(1 for m in matches if m['result'] == 'D')
    losses = sum(1 for m in matches if m['result'] == 'L')
    
    return {
        "split": name,
        "matches": n,
        "record": f"{wins}W-{draws}D-{losses}L",
        "pts": tot_pts,
        "ppg": round(tot_pts / n, 2),
        "gf": tot_gf,
        "gf_per_game": round(tot_gf / n, 2),
        "ga": tot_ga,
        "ga_per_game": round(tot_ga / n, 2),
        "gd": tot_gd,
        "gd_per_game": round(tot_gd / n, 2)
    }

first_5 = calc_split(arsenal_matches[:5], "First 5 Matches (Opening Stretch)")
rest_17 = calc_split(arsenal_matches[5:], "Matches 6-22 (Rest of Season)")

first_8 = calc_split(arsenal_matches[:8], "First 8 Matches (Initial Third)")
rest_14 = calc_split(arsenal_matches[8:], "Matches 9-22 (Final Two Thirds)")

total_season = calc_split(arsenal_matches, "Full Season (22 Matches)")

# Save structured summary to _data
summary = {
    "team": "Arsenal",
    "season": "2024/25",
    "splits": {
        "first_5": first_5,
        "rest_17": rest_17,
        "first_8": first_8,
        "rest_14": rest_14,
        "full_season": total_season
    },
    "match_log": arsenal_matches
}

out_path = Path("_data/arsenal_season_timeline.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)

print("\n=== SPLIT ANALYSIS COMPARISON ===")
print("First 5 vs Rest 17:")
print(f"  First 5: {first_5['record']} | {first_5['pts']} pts ({first_5['ppg']} PPG) | GF: {first_5['gf']} ({first_5['gf_per_game']}/g) | GA: {first_5['ga']} ({first_5['ga_per_game']}/g)")
print(f"  Rest 17: {rest_17['record']} | {rest_17['pts']} pts ({rest_17['ppg']} PPG) | GF: {rest_17['gf']} ({rest_17['gf_per_game']}/g) | GA: {rest_17['ga']} ({rest_17['ga_per_game']}/g)")

print("\nFirst 8 vs Rest 14:")
print(f"  First 8: {first_8['record']} | {first_8['pts']} pts ({first_8['ppg']} PPG) | GF: {first_8['gf']} ({first_8['gf_per_game']}/g) | GA: {first_8['ga']} ({first_8['ga_per_game']}/g)")
print(f"  Rest 14: {rest_14['record']} | {rest_14['pts']} pts ({rest_14['ppg']} PPG) | GF: {rest_14['gf']} ({rest_14['gf_per_game']}/g) | GA: {rest_14['ga']} ({rest_14['ga_per_game']}/g)")
