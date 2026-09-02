"""
Fetch Tottenham Hotspur Women Squad & Transfers from FotMob API
Configured for:
- Past/Baseline Season: 2025/2026
- New Season: 2026/2027
"""

import json
import requests
from pathlib import Path

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.fotmob.com/"
}

TOTTENHAM_ID = 628117

def fetch_tottenham_details():
    url = f"https://www.fotmob.com/api/data/teams?id={TOTTENHAM_ID}"
    res = requests.get(url, headers=HEADERS, timeout=15)
    res.raise_for_status()
    return res.json()

def parse_squad(data):
    squad_list = []
    raw_squad = data.get("squad", {}).get("squad", [])
    
    for section in raw_squad:
        role_title = section.get("title")
        if role_title == "coach":
            continue
        for m in section.get("members", []):
            role_info = m.get("role", {})
            pos_label = role_info.get("fallback") or role_title
            
            # map position short
            pos_short = "MF"
            if "keeper" in pos_label.lower():
                pos_short = "GK"
            elif "defender" in pos_label.lower() or "back" in pos_label.lower():
                pos_short = "DF"
            elif "forward" in pos_label.lower() or "striker" in pos_label.lower() or "winger" in pos_label.lower():
                pos_short = "FW"
            elif "midfielder" in pos_label.lower():
                pos_short = "MF"
                
            squad_list.append({
                "id": m.get("id"),
                "player": m.get("name"),
                "pos": pos_short,
                "role_detailed": pos_label,
                "age": str(m.get("age", "")),
                "nation": f"{m.get('ccode', '').lower()} {m.get('cname', '')}",
                "cname": m.get("cname", "")
            })
    return squad_list

def parse_transfers(data):
    transfers_raw = data.get("transfers", {})
    transfers_data = transfers_raw.get("data", {}) if isinstance(transfers_raw, dict) else {}
    
    transfers_in = []
    transfers_out = []
    
    for item in transfers_data.get("in", []):
        transfers_in.append({
            "player": item.get("name"),
            "pos": item.get("position", {}).get("label") if isinstance(item.get("position"), dict) else item.get("position"),
            "from": item.get("fromClub"),
            "fee": item.get("fee"),
            "transfer_type": item.get("transferType"),
            "date": item.get("transferDate")
        })
        
    for item in transfers_data.get("out", []):
        transfers_out.append({
            "player": item.get("name"),
            "pos": item.get("position", {}).get("label") if isinstance(item.get("position"), dict) else item.get("position"),
            "to": item.get("toClub"),
            "fee": item.get("fee"),
            "transfer_type": item.get("transferType"),
            "date": item.get("transferDate")
        })
        
    return {
        "team": "Tottenham Hotspur Women",
        "season_completed": "2025/26",
        "season_new": "2026/27",
        "transfers_in": transfers_in,
        "transfers_out": transfers_out
    }

def main():
    print("Fetching Tottenham Hotspur Women data from FotMob...")
    data = fetch_tottenham_details()
    
    squad_26_27 = parse_squad(data)
    transfers_data = parse_transfers(data)
    
    print(f"Parsed {len(squad_26_27)} current squad members for 2026/2027.")
    print(f"Parsed {len(transfers_data['transfers_in'])} transfers IN and {len(transfers_data['transfers_out'])} transfers OUT.")
    
    # Save squad
    squad_out_path = Path("_data/squads/tottenham_2026_27.json")
    with open(squad_out_path, "w", encoding="utf-8") as f:
        json.dump(squad_26_27, f, ensure_ascii=False, indent=2)
    print(f"Saved squad -> {squad_out_path}")
    
    # Save transfers
    transfers_out_path = Path("_data/transfers/tottenham.json")
    with open(transfers_out_path, "w", encoding="utf-8") as f:
        json.dump(transfers_data, f, ensure_ascii=False, indent=2)
    print(f"Saved transfers -> {transfers_out_path}")

if __name__ == "__main__":
    main()
