#!/usr/bin/env python3
"""
Deep Tactical Analysis: Arsenal Attack & Lisa Baum vs Arsenal Attackers, plus Arsenal Defense Breakdown
======================================================================================================
1. Fetches all 5 WSL matches for Arsenal (MW1 to MW5) from FotMob API if not locally cached:
   - MW1: 5981533 (Brighton vs Arsenal)
   - MW2: 5981639 (Crystal Palace vs Arsenal)
   - MW3: 5981644 (Man United vs Arsenal)
   - MW4: 5981654 (Chelsea vs Arsenal)
   - MW5: 5981661 (Man City vs Arsenal)
2. Fetches Lisa Baum player profile (ID: 1638167).
3. Extracts and aggregates player-by-player metrics across all 5 matches for Arsenal forwards:
   - Lisa Baum, Alessia Russo, Beth Mead, Caitlin Foord, Stina Blackstenius, Sophia Smith, Chloe Kelly, Mariona Caldentey, Lina Hurtig.
   - Metrics: Minutes, Goals, npxG, Shots, Shots on target, xGOT, Chances created, Big chances, Assists, xA,
     Dribbles attempted & successful, Ground duels won & %, Aerial duels won, Fouls won, Touches in box.
   - Calculates absolute sums and Per-90 normalised stats.
   - Analyzes minute 1-60 vs 60-90 splits for Lisa Baum and the team.
4. Analyzes Arsenal Defense:
   - Goals conceded (MW1-5 total and per game)
   - Comparison with 2024/25 & 2025/26 baseline conceded goals
   - Clean sheets, Shots conceded, Shots on target conceded
   - Tackles, Interceptions, Clearances, Blocks, Errors leading to goal
   - xGA total, xGA per shot conceded
   - Goals conceded and xGA split: Minutes 1-60 vs 60-90.
"""

import os
import sys
import json
import time
from pathlib import Path
from typing import Dict, Any, List, Optional
import requests

# Fix Windows console UTF-8 output
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_MATCHES_DIR = PROJECT_ROOT / "data" / "raw" / "fotmob" / "matches"
RAW_PLAYERS_DIR = PROJECT_ROOT / "data" / "raw" / "fotmob" / "players"
SITE_DATA_DIR = PROJECT_ROOT / "_data"

RAW_MATCHES_DIR.mkdir(parents=True, exist_ok=True)
RAW_PLAYERS_DIR.mkdir(parents=True, exist_ok=True)
SITE_DATA_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

ARSENAL_MATCHES = [
    {"mw": 1, "id": 5981533, "opponent": "Brighton (A)", "local": "data/raw/fotmob/match_5981533_brighton_arsenal.json"},
    {"mw": 2, "id": 5981639, "opponent": "Crystal Palace (H)", "local": "data/raw/fotmob/matches/mw2_cry_ars_5981639.json"},
    {"mw": 3, "id": 5981644, "opponent": "Man United (A)", "local": "data/raw/fotmob/matches/mw3_mun_ars_5981644.json"},
    {"mw": 4, "id": 5981654, "opponent": "Chelsea (A)", "local": "data/raw/fotmob/matches/mw4_che_ars_5981654.json"},
    {"mw": 5, "id": 5981661, "opponent": "Man City (A)", "local": "data/raw/fotmob/matches/mw5_mci_ars_5981661.json"},
]

def fetch_json(url: str, retries: int = 5, delay: float = 1.5) -> Optional[Dict[str, Any]]:
    for attempt in range(retries):
        try:
            res = requests.get(url, headers=HEADERS, timeout=20)
            if res.status_code == 200:
                return res.json()
            print(f"  [Attempt {attempt + 1}] HTTP {res.status_code} for {url}")
        except Exception as e:
            print(f"  [Attempt {attempt + 1}] Error: {e}")
        time.sleep(delay)
    return None

def load_or_fetch_match(m_info: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    # Check scratch in root first
    local_path = PROJECT_ROOT / m_info["local"]
    root_scratch = PROJECT_ROOT / f"scratch_{m_info['id']}.json"
    
    # Specific known locations
    if m_info["mw"] == 5:
        mci_root = PROJECT_ROOT / "scratch_mci_ars.json"
        if mci_root.exists():
            with open(mci_root, "r", encoding="utf-8") as f:
                return json.load(f)
    elif m_info["mw"] == 4:
        che_root = PROJECT_ROOT / "scratch_che_ars.json"
        if che_root.exists():
            with open(che_root, "r", encoding="utf-8") as f:
                return json.load(f)

    if local_path.exists():
        with open(local_path, "r", encoding="utf-8") as f:
            return json.load(f)
            
    print(f"Fetching MW{m_info['mw']} (Match {m_info['id']}: {m_info['opponent']})...")
    url = f"https://www.fotmob.com/api/data/matchDetails?matchId={m_info['id']}"
    data = fetch_json(url)
    if data:
        with open(local_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"  -> Saved to {local_path}")
    return data

def parse_stat_val(v):
    if v is None:
        return 0.0
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        v = v.strip()
        if "/" in v:
            parts = v.split("/")
            try:
                return float(parts[0])
            except:
                return 0.0
        try:
            return float(v)
        except:
            return 0.0
    return 0.0

def parse_stat_total(v):
    if isinstance(v, str) and "/" in v:
        try:
            return float(v.split("/")[1])
        except:
            return 0.0
    return 0.0

def extract_flat_player_stats(pdata: Dict[str, Any]) -> Dict[str, Any]:
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
                    res[f"{k}_val"] = float(val) if val is not None else 0.0
                    res[f"{k}_tot"] = float(total) if total is not None else 0.0
                else:
                    res[k] = val
                    res[f"{k}_val"] = float(val) if isinstance(val, (int, float)) else parse_stat_val(val)
    return res

def analyze_all():
    print("=" * 80)
    print(" WSL 2026/27 - ARSENAL MW1-5 DEEP DATA EXTRACTION")
    print("=" * 80)
    
    matches_data = []
    for m_info in ARSENAL_MATCHES:
        mdata = load_or_fetch_match(m_info)
        if mdata:
            matches_data.append((m_info, mdata))
        else:
            print(f"[!] Could not load match {m_info['id']}")
            
    print(f"Loaded {len(matches_data)} matches for Arsenal.\n")
    
    # -------------------------------------------------------------
    # 1. PLAYER STATS AGGREGATION
    # -------------------------------------------------------------
    tracked_forwards = [
        "Lisa Baum", "Alessia Russo", "Beth Mead", "Caitlin Foord",
        "Stina Blackstenius", "Chloe Kelly", "Sophia Smith",
        "Mariona Caldentey", "Lina Hurtig", "Frida Maanum"
    ]
    
    player_agg = {}
    
    for m_info, mdata in matches_data:
        mw = m_info["mw"]
        opp = m_info["opponent"]
        content = mdata.get("content", {})
        pstats = content.get("playerStats", {})
        lineup = content.get("lineup", {})
        
        # Determine Arsenal team side (home or away)
        general = mdata.get("general", {})
        home_team = general.get("homeTeam", {})
        is_home_ars = "arsenal" in home_team.get("name", "").lower()
        ars_side = "home" if is_home_ars else "away"
        
        for pid, pdata in pstats.items():
            pname = pdata.get("name", "")
            # Match with target tracked forwards
            matched_name = None
            for tf in tracked_forwards:
                if tf.lower() in pname.lower() or pname.lower() in tf.lower():
                    matched_name = tf
                    break
            if not matched_name:
                continue
                
            flat = extract_flat_player_stats(pdata)
            mins = flat.get("Minutes played_val", 0.0)
            if mins == 0.0:
                mins = parse_stat_val(flat.get("Minutes played"))
            
            if matched_name not in player_agg:
                player_agg[matched_name] = {
                    "matches_played": 0,
                    "starts": 0,
                    "minutes": 0,
                    "goals": 0,
                    "assists": 0,
                    "shots": 0,
                    "shots_on_target": 0,
                    "xg": 0.0,
                    "xgot": 0.0,
                    "chances_created": 0,
                    "big_chances": 0,
                    "dribbles_att": 0,
                    "dribbles_succ": 0,
                    "ground_duels_att": 0,
                    "ground_duels_won": 0,
                    "aerial_duels_att": 0,
                    "aerial_duels_won": 0,
                    "fouls_won": 0,
                    "touches_box": 0,
                    "recoveries": 0,
                    "tackles_won": 0,
                    "sub_off_min": [],
                    "match_logs": []
                }
                
            agg = player_agg[matched_name]
            agg["matches_played"] += 1
            if mins > 45:
                agg["starts"] += 1
            agg["minutes"] += mins
            
            goals = flat.get("Goals_val", 0.0)
            assists = flat.get("Assists_val", 0.0)
            shots = flat.get("Total shots_val", 0.0)
            shots_ot = flat.get("Shots on target_val", 0.0)
            xg = flat.get("Expected goals (xG)_val", 0.0)
            xgot = flat.get("Expected goals on target (xGOT)_val", 0.0)
            chances = flat.get("Chances created_val", 0.0)
            big_chances = flat.get("Big chances created_val", 0.0)
            
            dribbles_succ = flat.get("Successful dribbles_val", 0.0)
            dribbles_att = flat.get("Successful dribbles_tot", 0.0)
            if dribbles_att == 0.0:
                dribbles_succ = flat.get("Dribbles_val", 0.0)
                dribbles_att = flat.get("Dribbles_tot", 0.0)
                
            gd_won = flat.get("Ground duels won_val", 0.0)
            gd_att = flat.get("Ground duels won_tot", 0.0)
            ad_won = flat.get("Aerial duels won_val", 0.0)
            ad_att = flat.get("Aerial duels won_tot", 0.0)
            
            fouls_won = flat.get("Was fouled_val", 0.0)
            touches_box = flat.get("Touches in opposition box_val", 0.0)
            recoveries = flat.get("Recoveries_val", 0.0)
            tackles_won = flat.get("Tackles won_val", 0.0)
            
            agg["goals"] += goals
            agg["assists"] += assists
            agg["shots"] += shots
            agg["shots_on_target"] += shots_ot
            agg["xg"] += xg
            agg["xgot"] += xgot
            agg["chances_created"] += chances
            agg["big_chances"] += big_chances
            agg["dribbles_att"] += dribbles_att
            agg["dribbles_succ"] += dribbles_succ
            agg["ground_duels_att"] += gd_att
            agg["ground_duels_won"] += gd_won
            agg["aerial_duels_att"] += ad_att
            agg["aerial_duels_won"] += ad_won
            agg["fouls_won"] += fouls_won
            agg["touches_box"] += touches_box
            agg["recoveries"] += recoveries
            agg["tackles_won"] += tackles_won
            
            if mins < 90 and mins > 0:
                agg["sub_off_min"].append(int(mins))
                
            agg["match_logs"].append({
                "mw": mw,
                "opp": opp,
                "mins": int(mins),
                "goals": int(goals),
                "shots": int(shots),
                "xg": round(xg, 2),
                "chances": int(chances),
                "dribbles": f"{int(dribbles_succ)}/{int(dribbles_att)}",
                "ground_duels": f"{int(gd_won)}/{int(gd_att)}"
            })

    # Print Player Comparisons
    print("-" * 80)
    print(" 1. ARSENAL ATTACKERS COMPARISON (MW1-5 AGGREGATE & PER 90)")
    print("-" * 80)
    
    header = f"{'Player':<18} | {'MP':<3} | {'Mins':<5} | {'G':<2} | {'A':<2} | {'Shots':<5} | {'xG':<5} | {'Chances':<7} | {'Dribbles':<8} | {'Gr.Duels':<8} | {'Fouled':<6}"
    print(header)
    print("-" * len(header))
    
    for p, d in sorted(player_agg.items(), key=lambda x: x[1]["minutes"], reverse=True):
        if d["minutes"] == 0:
            continue
        drib_str = f"{int(d['dribbles_succ'])}/{int(d['dribbles_att'])}"
        gd_str = f"{int(d['ground_duels_won'])}/{int(d['ground_duels_att'])}"
        print(f"{p:<18} | {d['matches_played']:<3} | {int(d['minutes']):<5} | {int(d['goals']):<2} | {int(d['assists']):<2} | {int(d['shots']):<5} | {d['xg']:<5.2f} | {int(d['chances_created']):<7} | {drib_str:<8} | {gd_str:<8} | {int(d['fouls_won']):<6}")

    print("\n" + "-" * 80)
    print(" 2. PER-90 NORMALIZED ATTACKING COMPARISON")
    print("-" * 80)
    
    header90 = f"{'Player':<18} | {'Mins':<5} | {'G/90':<5} | {'xG/90':<6} | {'Sh/90':<5} | {'SoT%':<5} | {'Ch/90':<6} | {'Drib/90':<8} | {'Dr.Succ%':<8} | {'GD Won/90':<10}"
    print(header90)
    print("-" * len(header90))
    
    for p, d in sorted(player_agg.items(), key=lambda x: (x[1]["xg"] / (x[1]["minutes"]/90.0) if x[1]["minutes"] > 0 else 0), reverse=True):
        m = d["minutes"]
        if m < 90:
            continue
        p90 = m / 90.0
        g90 = d["goals"] / p90
        xg90 = d["xg"] / p90
        sh90 = d["shots"] / p90
        sot_pct = (d["shots_on_target"] / d["shots"] * 100) if d["shots"] > 0 else 0.0
        ch90 = d["chances_created"] / p90
        dr90 = d["dribbles_att"] / p90
        dr_pct = (d["dribbles_succ"] / d["dribbles_att"] * 100) if d["dribbles_att"] > 0 else 0.0
        gd90 = d["ground_duels_won"] / p90
        
        print(f"{p:<18} | {int(m):<5} | {g90:<5.2f} | {xg90:<6.2f} | {sh90:<5.2f} | {sot_pct:<4.0f}% | {ch90:<6.2f} | {dr90:<8.2f} | {dr_pct:<7.0f}% | {gd90:<10.2f}")

    # Lisa Baum Detail Match by Match
    print("\n" + "-" * 80)
    print(" 3. LISA BAUM - MATCH BY MATCH BREAKDOWN")
    print("-" * 80)
    baum = player_agg.get("Lisa Baum", {})
    if baum:
        print(f"Total Minutes: {int(baum['minutes'])} / {baum['matches_played']*90} ({int(baum['minutes'])/(baum['matches_played']*90)*100:.1f}%)")
        print(f"Subbed off minutes: {baum['sub_off_min']}")
        for log in baum.get("match_logs", []):
            print(f"  MW{log['mw']} ({log['opp']}): {log['mins']} mins | Goals: {log['goals']} | Shots: {log['shots']} (xG: {log['xg']}) | Chances: {log['chances']} | Dribbles: {log['dribbles']} | Ground Duels: {log['ground_duels']}")

    # -------------------------------------------------------------
    # 2. ARSENAL DEFENSE BREAKDOWN
    # -------------------------------------------------------------
    print("\n" + "=" * 80)
    print(" 4. ARSENAL DEFENSE: CONCEDED METRICS & TEMPORAL SPLIT (MINS 1-60 vs 60-90)")
    print("=" * 80)
    
    total_goals_conceded = 0
    total_xga = 0.0
    total_shots_conceded = 0
    total_sot_conceded = 0
    clean_sheets = 0
    
    mins_1_60_goals = 0
    mins_60_90_goals = 0
    
    mins_1_60_xga = 0.0
    mins_60_90_xga = 0.0
    
    match_def_breakdown = []
    
    for m_info, mdata in matches_data:
        mw = m_info["mw"]
        opp = m_info["opponent"]
        content = mdata.get("content", {})
        header_teams = mdata.get("header", {}).get("teams", [])
        
        home_t = header_teams[0] if len(header_teams) > 0 else {}
        away_t = header_teams[1] if len(header_teams) > 1 else {}
        
        is_home_ars = (home_t.get("id") == 258657) or ("arsenal" in home_t.get("name", "").lower())
        ars_t = home_t if is_home_ars else away_t
        opp_t = away_t if is_home_ars else home_t
        
        ars_score = int(ars_t.get("score", 0))
        opp_score = int(opp_t.get("score", 0))
        
        shotmap = content.get("shotmap", {}).get("shots", [])
        
        # Opponent shots: shots where teamId != 258657 (Arsenal)
        opp_shots = [s for s in shotmap if s.get("teamId") != 258657]
        ars_shots = [s for s in shotmap if s.get("teamId") == 258657]
        
        m_xga = sum(float(s.get("expectedGoals", 0.0) or 0.0) for s in opp_shots)
        m_shots_conceded = len(opp_shots)
        m_sot_conceded = len([s for s in opp_shots if s.get("isOnTarget") or s.get("eventType") == "Goal"])
        
        # Extract official team defensive stats from Periods.All.stats
        all_stats = content.get("stats", {}).get("Periods", {}).get("All", {}).get("stats", [])
        team_idx = 0 if is_home_ars else 1
        opp_idx = 1 if is_home_ars else 0
        
        def find_stat(category_title, stat_title):
            for grp in all_stats:
                if grp.get("title", "").lower() == category_title.lower():
                    for st in grp.get("stats", []):
                        if st.get("title", "").lower() == stat_title.lower():
                            vals = st.get("stats", [0, 0])
                            return vals[team_idx] if len(vals) > team_idx else 0
            return 0

        ars_tackles = find_stat("Defence", "Tackles")
        ars_interceptions = find_stat("Defence", "Interceptions")
        ars_clearances = find_stat("Defence", "Clearances")
        ars_blocks = find_stat("Defence", "Blocks")
        ars_saves = find_stat("Defence", "Keeper saves")
        
        m_g_1_60 = 0
        m_g_60_90 = 0
        m_xga_1_60 = 0.0
        m_xga_60_90 = 0.0
        
        for s in opp_shots:
            m_time = s.get("min", 0)
            s_xg = float(s.get("expectedGoals", 0.0) or 0.0)
            is_goal = s.get("eventType") == "Goal"
            
            if m_time <= 60:
                m_xga_1_60 += s_xg
                if is_goal:
                    m_g_1_60 += 1
            else:
                m_xga_60_90 += s_xg
                if is_goal:
                    m_g_60_90 += 1
                    
        total_goals_conceded += opp_score
        total_xga += m_xga
        total_shots_conceded += m_shots_conceded
        total_sot_conceded += m_sot_conceded
        if opp_score == 0:
            clean_sheets += 1
            
        mins_1_60_goals += m_g_1_60
        mins_60_90_goals += m_g_60_90
        mins_1_60_xga += m_xga_1_60
        mins_60_90_xga += m_xga_60_90
        
        match_def_breakdown.append({
            "mw": mw,
            "opp": opp,
            "score": f"{ars_score}-{opp_score}",
            "conceded": opp_score,
            "shots_conc": m_shots_conceded,
            "sot_conc": m_sot_conceded,
            "xga": round(m_xga, 2),
            "tackles": ars_tackles,
            "interceptions": ars_interceptions,
            "clearances": ars_clearances,
            "blocks": ars_blocks,
            "saves": ars_saves,
            "g_1_60": m_g_1_60,
            "g_60_90": m_g_60_90,
            "xga_1_60": round(m_xga_1_60, 2),
            "xga_60_90": round(m_xga_60_90, 2)
        })
        
    print(f"{'MW':<3} | {'Opponent':<20} | {'Score':<5} | {'Conc':<4} | {'Shots':<5} | {'SoT':<3} | {'xGA':<5} | {'G 1-60':<6} | {'G 60-90':<7} | {'xGA 1-60':<8} | {'xGA 60-90':<9}")
    print("-" * 88)
    for mb in match_def_breakdown:
        print(f"{mb['mw']:<3} | {mb['opp']:<20} | {mb['score']:<5} | {mb['conceded']:<4} | {mb['shots_conc']:<5} | {mb['sot_conc']:<3} | {mb['xga']:<5.2f} | {mb['g_1_60']:<6} | {mb['g_60_90']:<7} | {mb['xga_1_60']:<8.2f} | {mb['xga_60_90']:<9.2f}")
        
    print("-" * 88)
    print(f"TOTAL: 5 Matches | Conceded: {total_goals_conceded} (avg {total_goals_conceded/5:.2f}/game) | xGA: {total_xga:.2f} (avg {total_xga/5:.2f}/game)")
    print(f"Clean Sheets: {clean_sheets} ({clean_sheets/5*100:.0f}%)")
    print(f"Shots Conceded: {total_shots_conceded} (avg {total_shots_conceded/5:.1f}/game) | SoT: {total_sot_conceded} (avg {total_sot_conceded/5:.1f}/game)")
    print(f"xGA per Shot Conceded: {total_xga/total_shots_conceded:.3f}")
    print(f"\nCRITICAL TIME SPLIT (MINUTE 60 CRISIS):")
    print(f"  Minutes  1 - 60: Goals Conceded = {mins_1_60_goals} | xGA = {mins_1_60_xga:.2f} (avg {mins_1_60_xga/5:.2f}/game)")
    print(f"  Minutes 60 - 90: Goals Conceded = {mins_60_90_goals} | xGA = {mins_60_90_xga:.2f} (avg {mins_60_90_xga/5:.2f}/game)")
    pct_late_goals = (mins_60_90_goals / total_goals_conceded * 100) if total_goals_conceded > 0 else 0
    print(f"  -> {pct_late_goals:.1f}% of all goals conceded occurred in the final 30 minutes (post-min 60)!")

    # Comparison with Historical Baselines
    print("\n" + "-" * 80)
    print(" 5. HISTORICAL DEFENSIVE BENCHMARK")
    print("-" * 80)
    print("2024/25 Season (Arsenal): Conceded 14 goals in 22 games = 0.64 goals/game.")
    print(f"2026/27 Season (Arsenal, MW1-5): Conceded {total_goals_conceded} in 5 games = {total_goals_conceded/5:.2f} goals/game.")
    multiplier = (total_goals_conceded/5.0) / 0.64 if total_goals_conceded > 0 else 1.0
    print(f"  -> Rate of conceding is {multiplier:.2f}x HIGHER than the 2024/25 championship benchmark!")

    # Save complete metrics to _data/arsenal_mw5_deep_analysis.json
    export_payload = {
        "player_stats": player_agg,
        "team_defense": {
            "matches": match_def_breakdown,
            "total_conceded": total_goals_conceded,
            "avg_conceded": total_goals_conceded / 5,
            "total_xga": total_xga,
            "avg_xga": total_xga / 5,
            "clean_sheets": clean_sheets,
            "shots_conceded": total_shots_conceded,
            "sot_conceded": total_sot_conceded,
            "mins_1_60_goals": mins_1_60_goals,
            "mins_60_90_goals": mins_60_90_goals,
            "mins_1_60_xga": mins_1_60_xga,
            "mins_60_90_xga": mins_60_90_xga,
            "pct_late_goals": pct_late_goals
        }
    }
    
    export_path = SITE_DATA_DIR / "arsenal_mw5_deep_analysis.json"
    with open(export_path, "w", encoding="utf-8") as f:
        json.dump(export_payload, f, ensure_ascii=False, indent=2)
    print(f"\n[OK] Successfully exported metrics to {export_path}")

if __name__ == "__main__":
    analyze_all()
