"""
Compare Dario Vidosic (Brighton 2025/26) vs Arturo Ruiz (Real Sociedad 2025/26)
Using Official FotMob Season Topstats
"""

import sys
import io
import json
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

def get_stats(league_id, season_id, target_team_id):
    url = f"https://data.fotmob.com/stats/{league_id}/season/{season_id}/topstats.json"
    r = requests.get(url, headers=HEADERS, timeout=15)
    if r.status_code != 200:
        return {}
    data = r.json()
    team_metrics = {}
    for cat in data.get("TopLists", []):
        cat_name = cat.get("LocalizedTitleId") or cat.get("Title")
        # Check team stats
        for entry in cat.get("StatList", []):
            t_id = entry.get("TeamId") or entry.get("ParticipantId")
            if str(t_id) == str(target_team_id):
                team_metrics[cat_name] = {
                    "rank": entry.get("Rank"),
                    "value": entry.get("StatValue"),
                    "sub_value": entry.get("SubStatValue"),
                    "per90": entry.get("Per90StatValue")
                }
    return team_metrics

def main():
    print("=== EXTRACTING FOTMOB VERIFIED SEASON METRICS ===")
    
    # Brighton 2025/26 in WSL (Vidosic)
    # League 9227, Season 27506, Team 231505
    bha_25_26 = get_stats(9227, 27506, 231505)
    
    # Real Sociedad 2025/26 in Liga F (Ruiz)
    # League 9907, Season 27778, Team 858300
    rso_25_26 = get_stats(9907, 27778, 858300)
    
    print("\n--- BRIGHTON 2025/26 (Dario Vidosic) ---")
    for k, v in bha_25_26.items():
        print(f"  {k}: {v}")
        
    print("\n--- REAL SOCIEDAD 2025/26 (Arturo Ruiz) ---")
    for k, v in rso_25_26.items():
        print(f"  {k}: {v}")

    # Save to JSON
    with open("scratch_fotmob_vidosic_vs_ruiz.json", "w", encoding="utf-8") as f:
        json.dump({
            "brighton_vidosic_2025_26": bha_25_26,
            "real_sociedad_ruiz_2025_26": rso_25_26
        }, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
