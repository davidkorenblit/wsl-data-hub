#!/usr/bin/env python3
"""
Extract precise metrics for WSL Round 2:
1. Arsenal vs Palace: Russo, Mariona, Stanway, Chloe Kelly stats + Palace GK (Peyraud-Magnin) & CBs
2. Liverpool vs Spurs: Key match stats and Liverpool standout performers
3. West Ham vs LCL: LCL chances/xG + Midfield defensive actions (tackles, interceptions, recoveries)
4. Man United vs Chelsea: United defensive collapse metrics + Chelsea attacking efficiency
"""
import sys
import json
import requests

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_player_stat_dict(p_data):
    flat = {}
    flat["name"] = p_data.get("name")
    flat["team"] = p_data.get("teamName")
    flat["isGoalkeeper"] = p_data.get("isGoalkeeper")
    flat["shotmap"] = p_data.get("shotmap", [])
    for grp in p_data.get("stats", []):
        for stat_name, v in grp.get("stats", {}).items():
            val = v.get("stat", {}).get("value")
            flat[stat_name] = val
    return flat

def run():
    print("="*60)
    print("1. ARSENAL vs CRYSTAL PALACE (5981639)")
    print("="*60)
    res = requests.get('https://www.fotmob.com/api/data/matchDetails?matchId=5981639', headers=HEADERS).json()
    p_stats = res.get('content', {}).get('playerStats', {})
    
    palace_gk = None
    palace_def = []
    arsenal_att = []
    
    for pid, p in p_stats.items():
        st = get_player_stat_dict(p)
        if st.get("team") == "Arsenal Women":
            if any(name in st.get("name", "") for name in ["Russo", "Mariona", "Stanway", "Kelly", "Baum", "Foord", "Cooney-Cross"]):
                arsenal_att.append(st)
        else:
            if st.get("isGoalkeeper"):
                palace_gk = st
            elif any(name in st.get("name", "") for name in ["Everett", "Bartrip", "Goldie", "Napier"]):
                palace_def.append(st)
                
    print("\n--- Arsenal Key Creators / Attackers ---")
    for a in sorted(arsenal_att, key=lambda x: str(x.get("FotMob rating", "0")), reverse=True):
        print(f"• {a.get('name')}: Rating {a.get('FotMob rating')} | Shots: {a.get('Total shots', 0)} (On target: {a.get('Shots on target', 0)}) | xG: {a.get('Expected goals (xG)', 0)} | Chances created: {a.get('Chances created', 0)}")
        
    print("\n--- Palace Goalkeeper & Defence ---")
    if palace_gk:
        print(f"🧤 GK: {palace_gk.get('name')}: Rating {palace_gk.get('FotMob rating')} | Saves: {palace_gk.get('Saves')} | Saves inside box: {palace_gk.get('Saves inside box')} | Goals prevented: {palace_gk.get('Goals prevented')}")
    for d in palace_def:
        print(f"🛡️ {d.get('name')}: Rating {d.get('FotMob rating')} | Clearances: {d.get('Clearances', 0)} | Blocks: {d.get('Blocks', 0)} | Tackles won: {d.get('Tackles won', 0)}")

    print("\n" + "="*60)
    print("2. LIVERPOOL vs TOTTENHAM (5981638)")
    print("="*60)
    res_liv = requests.get('https://www.fotmob.com/api/data/matchDetails?matchId=5981638', headers=HEADERS).json()
    p_stats_liv = res_liv.get('content', {}).get('playerStats', {})
    liv_players = []
    spurs_players = []
    for pid, p in p_stats_liv.items():
        st = get_player_stat_dict(p)
        if "Liverpool" in st.get("team", ""):
            liv_players.append(st)
        elif "Tottenham" in st.get("team", ""):
            spurs_players.append(st)
            
    print("\n--- Liverpool Top Performers ---")
    for p in sorted(liv_players, key=lambda x: float(x.get("FotMob rating") or 0), reverse=True)[:5]:
        print(f"• {p.get('name')}: Rating {p.get('FotMob rating')} | Shots: {p.get('Total shots', 0)} | Chances created: {p.get('Chances created', 0)} | Tackles won: {p.get('Tackles won', 0)} | Duels won: {p.get('Duels won', 0)}")
        
    print("\n" + "="*60)
    print("3. WEST HAM vs LONDON CITY LIONESSES (5981634)")
    print("="*60)
    res_lcl = requests.get('https://www.fotmob.com/api/data/matchDetails?matchId=5981634', headers=HEADERS).json()
    p_stats_lcl = res_lcl.get('content', {}).get('playerStats', {})
    lcl_players = []
    for pid, p in p_stats_lcl.items():
        st = get_player_stat_dict(p)
        if "London City" in st.get("team", ""):
            lcl_players.append(st)
            
    print("\n--- LCL Attacking & Creative Stats ---")
    for p in sorted(lcl_players, key=lambda x: float(x.get("Chances created") or 0) + float(x.get("Total shots") or 0), reverse=True)[:6]:
        print(f"• {p.get('name')}: Rating {p.get('FotMob rating')} | Shots: {p.get('Total shots', 0)} (OT: {p.get('Shots on target', 0)}) | xG: {p.get('Expected goals (xG)', 0)} | Chances created: {p.get('Chances created', 0)}")

    print("\n--- LCL Midfield / Defensive Actions ---")
    for p in sorted(lcl_players, key=lambda x: float(x.get("Tackles won") or 0) + float(x.get("Interceptions") or 0), reverse=True):
        tackles = p.get("Tackles won", 0)
        interceptions = p.get("Interceptions", 0)
        recoveries = p.get("Recoveries", 0)
        duels = p.get("Duels won", 0)
        mins = p.get("Minutes played", 0)
        if float(mins or 0) > 30:
            print(f"• {p.get('name')} ({mins} min): Tackles won: {tackles} | Interceptions: {interceptions} | Recoveries: {recoveries} | Duels won: {duels} | Rating: {p.get('FotMob rating')}")

    print("\n" + "="*60)
    print("4. MANCHESTER UNITED vs CHELSEA (5981635)")
    print("="*60)
    res_che = requests.get('https://www.fotmob.com/api/data/matchDetails?matchId=5981635', headers=HEADERS).json()
    p_stats_che = res_che.get('content', {}).get('playerStats', {})
    che_att = []
    utd_def = []
    for pid, p in p_stats_che.items():
        st = get_player_stat_dict(p)
        if "Chelsea" in st.get("team", ""):
            che_att.append(st)
        elif "Manchester United" in st.get("team", ""):
            utd_def.append(st)

    print("\n--- Chelsea Key Attackers ---")
    for p in sorted(che_att, key=lambda x: float(x.get("FotMob rating") or 0), reverse=True)[:6]:
        print(f"• {p.get('name')}: Rating {p.get('FotMob rating')} | Goals: {p.get('Goals', 0)} | Assists: {p.get('Assists', 0)} | Shots: {p.get('Total shots', 0)} | xG: {p.get('Expected goals (xG)', 0)}")

    print("\n--- Man United Defenders / GK Collapse ---")
    for p in sorted(utd_def, key=lambda x: float(x.get("FotMob rating") or 0))[:6]:
        print(f"• {p.get('name')}: Rating {p.get('FotMob rating')} | Clearances: {p.get('Clearances', 0)} | Tackles won: {p.get('Tackles won', 0)} | Duels won: {p.get('Duels won', 0)}")

if __name__ == "__main__":
    run()
