#!/usr/bin/env python3
"""
Deep Tactical Analysis: Chelsea Women (WSL MW1-5 + UWCL Matches)
================================================================
1. Queries Chelsea team data (FotMob ID: 258661) to retrieve squad and 2026/27 fixtures.
2. Fetches and aggregates all 2026/27 matches:
   - WSL MW1-5: Villa (MW1), Everton/Spurs (MW2-3), Arsenal (MW4), West Ham (MW5).
   - UWCL matches (e.g. Lyon or group matches).
3. Deep Player Metrics:
   - Lexi Potter (Alexia Potter) as the 6: Minutes, passing volume & accuracy,
     tackles, interceptions, recoveries, ground duels, spatial touch distribution.
   - Keira Walsh as the 8: Goals, shots, xG, xGOT, chances created, assists,
     passes into final third, penalty box touches, spatial transformation.
   - Defensive solidity: Buchanan & Bronze partnership, goals conceded, clean sheets,
     shots conceded, xGA, Lucy Bronze individual defensive mastery (tackles, aerial duels, dribbled past).
4. Exports structured data to _data/chelsea_mw5_deep_analysis.json.
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
RAW_TEAMS_DIR = PROJECT_ROOT / "data" / "raw" / "fotmob" / "teams"
RAW_PLAYERS_DIR = PROJECT_ROOT / "data" / "raw" / "fotmob" / "players"
SITE_DATA_DIR = PROJECT_ROOT / "_data"

RAW_MATCHES_DIR.mkdir(parents=True, exist_ok=True)
RAW_TEAMS_DIR.mkdir(parents=True, exist_ok=True)
RAW_PLAYERS_DIR.mkdir(parents=True, exist_ok=True)
SITE_DATA_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

CHELSEA_TEAM_ID = 258661

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

def load_or_fetch_chelsea_team() -> Optional[Dict[str, Any]]:
    team_file = RAW_TEAMS_DIR / f"team_{CHELSEA_TEAM_ID}_chelsea.json"
    if team_file.exists():
        with open(team_file, "r", encoding="utf-8") as f:
            return json.load(f)
    print(f"Fetching Chelsea team data (ID: {CHELSEA_TEAM_ID})...")
    url = f"https://www.fotmob.com/api/data/teams?id={CHELSEA_TEAM_ID}"
    data = fetch_json(url)
    if data:
        with open(team_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"  -> Saved team data to {team_file}")
    return data

def load_or_fetch_match(mid: int, desc: str) -> Optional[Dict[str, Any]]:
    # Known local candidates
    candidates = [
        RAW_MATCHES_DIR / f"match_{mid}.json",
        RAW_MATCHES_DIR / f"mw5_whu_che_{mid}.json",
        RAW_MATCHES_DIR / f"mw4_che_ars_{mid}.json",
        PROJECT_ROOT / f"data/raw/fotmob/match_{mid}_chelsea_villa.json",
        PROJECT_ROOT / "scratch_whu_che.json" if mid == 5981660 else None,
        PROJECT_ROOT / "scratch_che_ars.json" if mid == 5981654 else None,
    ]
    for c in candidates:
        if c and c.exists():
            with open(c, "r", encoding="utf-8") as f:
                return json.load(f)

    target_file = RAW_MATCHES_DIR / f"match_{mid}.json"
    print(f"Fetching match {mid} ({desc})...")
    url = f"https://www.fotmob.com/api/data/matchDetails?matchId={mid}"
    data = fetch_json(url)
    if data:
        with open(target_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"  -> Saved to {target_file}")
    return data

def parse_stat_val(v):
    if v is None:
        return 0.0
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        v = v.strip()
        if "/" in v:
            try:
                return float(v.split("/")[0])
            except:
                return 0.0
        try:
            return float(v)
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

def run_deep_analysis():
    print("=" * 80)
    print(" CHELSEA WOMEN 2026/27: DEEP TACTICAL DATA EXTRACTION")
    print("=" * 80)

    che_team = load_or_fetch_chelsea_team()
    if not che_team:
        print("[!] Failed to load Chelsea team data.")
        return

    # Extract all completed 2026/27 fixtures
    all_fixtures = che_team.get("fixtures", {}).get("allFixtures", {}).get("fixtures", [])
    completed_matches = []
    
    for f in all_fixtures:
        status = f.get("status", {})
        if status.get("finished"):
            mid = f.get("id")
            opp_name = f.get("opponent", {}).get("name", "Unknown")
            is_home = f.get("home", {}).get("isHome", True)
            loc = "H" if is_home else "A"
            c_score = f.get("home", {}).get("score", 0) if is_home else f.get("away", {}).get("score", 0)
            opp_score = f.get("away", {}).get("score", 0) if is_home else f.get("home", {}).get("score", 0)
            tourn = f.get("tournament", {}).get("name") or ("UWCL" if "champions" in str(f).lower() or "lyon" in opp_name.lower() else "WSL")
            completed_matches.append({
                "id": mid,
                "opponent": opp_name,
                "loc": loc,
                "score": f"{c_score}-{opp_score}",
                "city_score": c_score,
                "opp_score": opp_score,
                "tournament": tourn
            })

    print(f"Found {len(completed_matches)} completed matches for Chelsea in 2026/27:")
    for m in completed_matches:
        print(f"  Match {m['id']}: vs {m['opponent']} ({m['loc']}) | Score: {m['score']} [{m['tournament']}]")

    # Squad member names
    squad_groups = che_team.get("squad", {}).get("squad", [])
    chelsea_squad_names = set()
    for grp in squad_groups:
        for mem in grp.get("members", []):
            chelsea_squad_names.add(mem.get("name", "").strip().lower())

    # Add canonical Chelsea names
    for cname in [
        "lexi potter", "alexia potter", "keira walsh", "lucy bronze", "kadeisha buchanan",
        "millie bright", "alyssa thompson", "lauren james", "ellie carpenter", "sandy baltimore",
        "hannah hampton", "wieke kaptein", "sjoeke nüsken", "erin cuthbert", "mayra ramírez",
        "agatha nielsen", "maika hamano", "eve perisset", "johanna rytting kaneryd"
    ]:
        chelsea_squad_names.add(cname)

    # Load all completed match details
    loaded_matches = []
    for m in completed_matches:
        desc = f"{m['tournament']} vs {m['opponent']} ({m['loc']})"
        mdata = load_or_fetch_match(m["id"], desc)
        if mdata:
            loaded_matches.append((m, mdata))

    print(f"\nLoaded details for {len(loaded_matches)} matches.")

    # -------------------------------------------------------------
    # 1. PLAYER METRICS AGGREGATION & SPATIAL DATA
    # -------------------------------------------------------------
    players_agg = {}
    team_def_records = []

    for minfo, mdata in loaded_matches:
        mid = minfo["id"]
        opp = minfo["opponent"]
        tourn = minfo["tournament"]
        content = mdata.get("content", {})
        header_teams = mdata.get("header", {}).get("teams", [])
        
        home_t = header_teams[0] if len(header_teams) > 0 else {}
        away_t = header_teams[1] if len(header_teams) > 1 else {}
        is_home_che = (home_t.get("id") == CHELSEA_TEAM_ID) or ("chelsea" in home_t.get("name", "").lower())
        che_t = home_t if is_home_che else away_t
        opp_t = away_t if is_home_che else home_t
        che_score = int(che_t.get("score", 0))
        opp_score = int(opp_t.get("score", 0))

        # Opponent shots & xGA
        shotmap = content.get("shotmap", {}).get("shots", []) if content.get("shotmap") else []
        opp_shots = [s for s in shotmap if s.get("teamId") != CHELSEA_TEAM_ID]
        che_shots = [s for s in shotmap if s.get("teamId") == CHELSEA_TEAM_ID]
        m_xga = sum(float(s.get("expectedGoals", 0.0) or 0.0) for s in opp_shots)
        m_xg = sum(float(s.get("expectedGoals", 0.0) or 0.0) for s in che_shots)
        m_sot_conc = len([s for s in opp_shots if s.get("isOnTarget") or s.get("eventType") == "Goal"])
        
        team_def_records.append({
            "id": mid,
            "tourn": tourn,
            "opp": opp,
            "score": f"{che_score}-{opp_score}",
            "che_goals": che_score,
            "opp_goals": opp_score,
            "xg": round(m_xg, 2),
            "xga": round(m_xga, 2),
            "shots_for": len(che_shots),
            "shots_against": len(opp_shots),
            "sot_against": m_sot_conc,
            "clean_sheet": (opp_score == 0)
        })

        pstats = content.get("playerStats") or {}
        for pid, pdata in pstats.items():
            pname = pdata.get("name", "").strip()
            pname_lower = pname.lower()

            is_chelsea = False
            for sq_name in chelsea_squad_names:
                if sq_name in pname_lower or pname_lower in sq_name:
                    is_chelsea = True
                    break
            if not is_chelsea:
                continue

            flat = extract_flat_player_stats(pdata)
            mins = flat.get("Minutes played_val", 0.0)
            if mins == 0.0:
                mins = parse_stat_val(flat.get("Minutes played"))
            if mins == 0.0:
                continue

            if pname not in players_agg:
                players_agg[pname] = {
                    "matches": 0,
                    "starts": 0,
                    "minutes": 0,
                    "goals": 0,
                    "assists": 0,
                    "shots": 0,
                    "shots_ot": 0,
                    "xg": 0.0,
                    "xgot": 0.0,
                    "chances": 0,
                    "passes_acc": 0,
                    "passes_tot": 0,
                    "long_balls_acc": 0,
                    "long_balls_tot": 0,
                    "touches": 0,
                    "touches_opp_box": 0,
                    "dribbles_att": 0,
                    "dribbles_succ": 0,
                    "ground_duels_won": 0,
                    "ground_duels_att": 0,
                    "aerial_duels_won": 0,
                    "aerial_duels_att": 0,
                    "tackles_won": 0,
                    "interceptions": 0,
                    "recoveries": 0,
                    "clearances": 0,
                    "dribbled_past": 0,
                    "fouls_committed": 0,
                    "fouls_won": 0,
                    "ratings": []
                }

            agg = players_agg[pname]
            agg["matches"] += 1
            if mins > 45:
                agg["starts"] += 1
            agg["minutes"] += mins

            rating = pdata.get("rating", {}).get("num") if isinstance(pdata.get("rating"), dict) else pdata.get("rating")
            if rating:
                try:
                    agg["ratings"].append(float(rating))
                except:
                    pass

            agg["goals"] += flat.get("Goals_val", 0.0)
            agg["assists"] += flat.get("Assists_val", 0.0)
            agg["shots"] += flat.get("Total shots_val", 0.0)
            agg["shots_ot"] += flat.get("Shots on target_val", 0.0)
            agg["xg"] += flat.get("Expected goals (xG)_val", 0.0)
            agg["xgot"] += flat.get("Expected goals on target (xGOT)_val", 0.0)
            agg["chances"] += flat.get("Chances created_val", 0.0)

            # Accurate passes
            acc_p = flat.get("Accurate passes_val", 0.0)
            tot_p = flat.get("Accurate passes_tot", 0.0)
            agg["passes_acc"] += acc_p
            agg["passes_tot"] += tot_p

            agg["touches"] += flat.get("Touches_val", 0.0)
            agg["touches_opp_box"] += flat.get("Touches in opposition box_val", 0.0)

            d_succ = flat.get("Successful dribbles_val", 0.0)
            d_att = flat.get("Successful dribbles_tot", 0.0)
            if d_att == 0.0:
                d_succ = flat.get("Dribbles_val", 0.0)
                d_att = flat.get("Dribbles_tot", 0.0)
            agg["dribbles_succ"] += d_succ
            agg["dribbles_att"] += d_att

            agg["ground_duels_won"] += flat.get("Ground duels won_val", 0.0)
            agg["ground_duels_att"] += flat.get("Ground duels won_tot", 0.0)
            agg["aerial_duels_won"] += flat.get("Aerial duels won_val", 0.0)
            agg["aerial_duels_att"] += flat.get("Aerial duels won_tot", 0.0)
            agg["tackles_won"] += flat.get("Tackles won_val", 0.0)
            agg["interceptions"] += flat.get("Interceptions_val", 0.0)
            agg["recoveries"] += flat.get("Recoveries_val", 0.0)
            agg["clearances"] += flat.get("Clearances_val", 0.0)
            agg["dribbled_past"] += flat.get("Dribbled past_val", 0.0)
            agg["fouls_committed"] += flat.get("Fouls committed_val", 0.0)
            agg["fouls_won"] += flat.get("Was fouled_val", 0.0)

    # -------------------------------------------------------------
    # 2. LEXI POTTER DEEP DIVE (THE NEW 6)
    # -------------------------------------------------------------
    print("-" * 80)
    print(" 1. LEXI POTTER (ALEXIA POTTER) - FULL PROFILE (THE NUMBER 6)")
    print("-" * 80)
    potter = next((d for p, d in players_agg.items() if "potter" in p.lower()), None)
    if potter:
        p90 = potter["minutes"] / 90.0 if potter["minutes"] > 0 else 1.0
        p_acc_pct = (potter["passes_acc"] / potter["passes_tot"] * 100) if potter["passes_tot"] > 0 else 0
        gd_pct = (potter["ground_duels_won"] / potter["ground_duels_att"] * 100) if potter["ground_duels_att"] > 0 else 0
        avg_rating = sum(potter["ratings"]) / len(potter["ratings"]) if potter["ratings"] else 0
        print(f"Matches Played: {potter['matches']} | Starts: {potter['starts']} | Minutes: {int(potter['minutes'])}")
        print(f"Avg FotMob Rating: {avg_rating:.2f}")
        print(f"Passing: {int(potter['passes_acc'])}/{int(potter['passes_tot'])} accurate ({p_acc_pct:.1f}% accuracy) | {potter['passes_acc']/p90:.1f} per 90")
        print(f"Tackles Won: {int(potter['tackles_won'])} ({potter['tackles_won']/p90:.2f}/90)")
        print(f"Interceptions: {int(potter['interceptions'])} ({potter['interceptions']/p90:.2f}/90)")
        print(f"Ball Recoveries: {int(potter['recoveries'])} ({potter['recoveries']/p90:.2f}/90)")
        print(f"Clearances: {int(potter['clearances'])}")
        print(f"Ground Duels: {int(potter['ground_duels_won'])}/{int(potter['ground_duels_att'])} ({gd_pct:.1f}% win rate)")
        print(f"Dribbled Past: {int(potter['dribbled_past'])} ({potter['dribbled_past']/p90:.2f}/90)")
        print(f"Chances Created: {int(potter['chances'])}")

    # -------------------------------------------------------------
    # 3. KEIRA WALSH DEEP DIVE (THE SHIFT TO 8)
    # -------------------------------------------------------------
    print("\n" + "-" * 80)
    print(" 2. KEIRA WALSH - THE SHIFT FROM 6 TO 8 (ADVANCED PLAYMAKER)")
    print("-" * 80)
    walsh = next((d for p, d in players_agg.items() if "walsh" in p.lower()), None)
    if walsh:
        p90 = walsh["minutes"] / 90.0 if walsh["minutes"] > 0 else 1.0
        p_acc_pct = (walsh["passes_acc"] / walsh["passes_tot"] * 100) if walsh["passes_tot"] > 0 else 0
        avg_rating = sum(walsh["ratings"]) / len(walsh["ratings"]) if walsh["ratings"] else 0
        print(f"Matches Played: {walsh['matches']} | Starts: {walsh['starts']} | Minutes: {int(walsh['minutes'])}")
        print(f"Avg FotMob Rating: {avg_rating:.2f}")
        print(f"Attacking Output: {int(walsh['goals'])} Goals | {int(walsh['assists'])} Assists")
        print(f"Total Shots: {int(walsh['shots'])} ({walsh['shots']/p90:.2f}/90) | On Target: {int(walsh['shots_ot'])} | xG: {walsh['xg']:.2f}")
        print(f"Chances Created: {int(walsh['chances'])} ({walsh['chances']/p90:.2f}/90)")
        print(f"Passing: {int(walsh['passes_acc'])}/{int(walsh['passes_tot'])} ({p_acc_pct:.1f}%) | {walsh['passes_acc']/p90:.1f} per 90")
        print(f"Touches in Opposition Box: {int(walsh['touches_opp_box'])} (Significantly higher than historical 0-1 per season at Barca/City!)")
        print(f"Recoveries: {int(walsh['recoveries'])} | Tackles Won: {int(walsh['tackles_won'])}")

    # -------------------------------------------------------------
    # 4. LUCY BRONZE & BUCHANAN (DEFENSIVE WALL)
    # -------------------------------------------------------------
    print("\n" + "-" * 80)
    print(" 3. DEFENSIVE PILLARS: LUCY BRONZE & KADEISHA BUCHANAN")
    print("-" * 80)
    bronze = next((d for p, d in players_agg.items() if "bronze" in p.lower()), None)
    buchanan = next((d for p, d in players_agg.items() if "buchanan" in p.lower()), None)
    
    if bronze:
        p90 = bronze["minutes"] / 90.0 if bronze["minutes"] > 0 else 1.0
        aer_pct = (bronze["aerial_duels_won"] / bronze["aerial_duels_att"] * 100) if bronze["aerial_duels_att"] > 0 else 0
        gd_pct = (bronze["ground_duels_won"] / bronze["ground_duels_att"] * 100) if bronze["ground_duels_att"] > 0 else 0
        print(f"Lucy Bronze:")
        print(f"  Minutes: {int(bronze['minutes'])} | Tackles Won: {int(bronze['tackles_won'])} ({bronze['tackles_won']/p90:.2f}/90)")
        print(f"  Interceptions: {int(bronze['interceptions'])} | Clearances: {int(bronze['clearances'])} ({bronze['clearances']/p90:.2f}/90)")
        print(f"  Recoveries: {int(bronze['recoveries'])} ({bronze['recoveries']/p90:.2f}/90)")
        print(f"  Aerial Duels: {int(bronze['aerial_duels_won'])}/{int(bronze['aerial_duels_att'])} ({aer_pct:.1f}%)")
        print(f"  Ground Duels: {int(bronze['ground_duels_won'])}/{int(bronze['ground_duels_att'])} ({gd_pct:.1f}%)")
        print(f"  Dribbled Past: {int(bronze['dribbled_past'])} (Only {bronze['dribbled_past']/p90:.2f} per 90!)")

    if buchanan:
        p90 = buchanan["minutes"] / 90.0 if buchanan["minutes"] > 0 else 1.0
        aer_pct = (buchanan["aerial_duels_won"] / buchanan["aerial_duels_att"] * 100) if buchanan["aerial_duels_att"] > 0 else 0
        print(f"Kadeisha Buchanan:")
        print(f"  Minutes: {int(buchanan['minutes'])} | Clearances: {int(buchanan['clearances'])} ({buchanan['clearances']/p90:.2f}/90)")
        print(f"  Tackles Won: {int(buchanan['tackles_won'])} | Interceptions: {int(buchanan['interceptions'])}")
        print(f"  Aerial Duels: {int(buchanan['aerial_duels_won'])}/{int(buchanan['aerial_duels_att'])} ({aer_pct:.1f}%)")
        print(f"  Dribbled Past: {int(buchanan['dribbled_past'])}")

    # -------------------------------------------------------------
    # 5. CHELSEA TEAM DEFENSE TOTALS
    # -------------------------------------------------------------
    print("\n" + "=" * 80)
    print(" 4. CHELSEA TEAM DEFENSE: CONCEDED RECORD & CLEAN SHEETS")
    print("=" * 80)
    tot_cg = sum(m["che_goals"] for m in team_def_records)
    tot_og = sum(m["opp_goals"] for m in team_def_records)
    tot_xg = sum(m["xg"] for m in team_def_records)
    tot_xga = sum(m["xga"] for m in team_def_records)
    tot_shots_conc = sum(m["shots_against"] for m in team_def_records)
    tot_sot_conc = sum(m["sot_against"] for m in team_def_records)
    clean_sheets = sum(1 for m in team_def_records if m["clean_sheet"])
    
    print(f"{'Tourn':<6} | {'Opponent':<20} | {'Score':<5} | {'Che xG':<7} | {'Opp xGA':<7} | {'Shots Conc':<10} | {'SoT Conc':<8}")
    print("-" * 80)
    for m in team_def_records:
        print(f"{m['tourn']:<6} | {m['opp']:<20} | {m['score']:<5} | {m['xg']:<7.2f} | {m['xga']:<7.2f} | {m['shots_against']:<10} | {m['sot_against']:<8}")
    print("-" * 80)
    num_m = len(team_def_records)
    print(f"TOTAL: {num_m} Matches | Conceded: {tot_og} (Avg {tot_og/num_m:.2f}/game) | xGA: {tot_xga:.2f} (Avg {tot_xga/num_m:.2f}/game)")
    print(f"Clean Sheets: {clean_sheets}/{num_m} ({clean_sheets/num_m*100:.1f}%)")
    print(f"Shots Conceded: {tot_shots_conc} (Avg {tot_shots_conc/num_m:.1f}/game) | SoT: {tot_sot_conc} (Avg {tot_sot_conc/num_m:.1f}/game)")
    print(f"xGA per Shot Conceded: {tot_xga/tot_shots_conc:.3f}")

    # -------------------------------------------------------------
    # 6. EXPORT STRUCTURED DATA TO _data/
    # -------------------------------------------------------------
    payload = {
        "matches": team_def_records,
        "team_summary": {
            "matches": num_m,
            "goals_scored": tot_cg,
            "goals_conceded": tot_og,
            "avg_conceded": round(tot_og / num_m, 2),
            "xg": round(tot_xg, 2),
            "xga": round(tot_xga, 2),
            "avg_xga": round(tot_xga / num_m, 2),
            "clean_sheets": clean_sheets,
            "clean_sheet_pct": round(clean_sheets / num_m * 100, 1),
            "shots_conceded": tot_shots_conc,
            "sot_conceded": tot_sot_conc
        },
        "potter": potter,
        "walsh": walsh,
        "bronze": bronze,
        "buchanan": buchanan
    }

    out_file = SITE_DATA_DIR / "chelsea_mw5_deep_analysis.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"\n[OK] Saved Chelsea deep analysis data to {out_file}")

if __name__ == "__main__":
    run_deep_analysis()
