"""
WSL Data Hub - London City Lionesses Transfer Movement Calculator
=================================================================
Compares 2025/26 squad with current 2026/27 squad from Wikipedia.
Exports structured JSON to `_data/lcl_transfers_2025.json`.
"""

import json
import unicodedata
import pandas as pd
from pathlib import Path

from paths import LCL_PLAYERS_DIR, SITE_DATA_DIR, HUB_ROOT

SITE_DATA_DIR.mkdir(parents=True, exist_ok=True)


def normalize_name(name: str) -> str:
    """Normalize names to handle accents (León -> Leon) and variations."""
    if not isinstance(name, str):
        return ""
    nfkd = unicodedata.normalize('NFKD', name)
    clean = "".join([c for c in nfkd if not unicodedata.combining(c)]).lower().strip()
    return clean


def compute_transfers():
    # 1. Load Current 2026/27 Squad (from Wikipedia)
    csv_path = LCL_PLAYERS_DIR / "lcl_squad_current_2627.csv"
    df_new = pd.read_csv(csv_path)

    # 2. Load 2025/26 Squad (from FBref standard player stats)
    old_squad_json = SITE_DATA_DIR / "squads" / "london-city-lionesses.json"
    with open(old_squad_json, "r", encoding="utf-8") as f:
        old_squad_data = json.load(f)
    df_old = pd.DataFrame(old_squad_data)

    df_new["norm_name"] = df_new["player"].apply(normalize_name)
    df_old["norm_name"] = df_old["player"].apply(normalize_name)

    # Known name mappings across seasons
    alias_map = {
        "malou marcetto": "malou rylov",
        "malou marcetto rylov": "malou rylov",
        "elena linari": "elena linari",
    }

    old_names = set(df_old["norm_name"].tolist())
    
    # Identify Arrivals (Transfers In)
    transfers_in = []
    for _, row in df_new.iterrows():
        n = row["norm_name"]
        mapped_n = alias_map.get(n, n)
        if mapped_n not in old_names:
            transfers_in.append({
                "no": int(row["no"]),
                "player": str(row["player"]),
                "pos": str(row["pos"]),
                "nation": str(row["nation"]),
                "status": "New Signing"
            })

    # Identify Departures (Transfers Out)
    new_names = set(df_new["norm_name"].tolist())
    for k, v in alias_map.items():
        if k in new_names:
            new_names.add(v)

    transfers_out = []
    for _, row in df_old.iterrows():
        n = row["norm_name"]
        if n not in new_names:
            transfers_out.append({
                "player": str(row["player"]),
                "pos": str(row["pos"]),
                "min": int(row.get("min", 0)) if pd.notnull(row.get("min")) else 0,
                "status": "Departed"
            })

    # Retained players
    retained = []
    for _, row in df_new.iterrows():
        n = row["norm_name"]
        mapped_n = alias_map.get(n, n)
        if mapped_n in old_names:
            retained.append({
                "no": int(row["no"]),
                "player": str(row["player"]),
                "pos": str(row["pos"]),
                "nation": str(row["nation"]),
                "status": "Retained"
            })

    output_data = {
        "team_name": "London City Lionesses",
        "season": "2026/27",
        "summary": {
            "total_new_signings": len(transfers_in),
            "total_departures": len(transfers_out),
            "total_retained": len(retained)
        },
        "transfers_in": transfers_in,
        "transfers_out": transfers_out,
        "retained": retained
    }

    out_json = SITE_DATA_DIR / "lcl_transfers_2025.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"[OK] Generated transfer movements: {len(transfers_in)} In, {len(transfers_out)} Out, {len(retained)} Retained.")
    print(f"[OK] Saved to: {out_json}")
    return output_data


if __name__ == "__main__":
    compute_transfers()
