"""
WSL Data Hub - Complete FBref Data Extraction & Pipeline Script
Uses ScraperFC to fetch 5 core WSL stat categories (standard, shooting, passing, defense, keeper)
for 2025-2026, cleans column names, and saves both full league raw data and LCL squad subsets.
"""

import os
import time
import pandas as pd
import ScraperFC as sfc

# Absolute path resolution ensuring data is saved inside wsl-data-hub/data/
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
LCL_DATA_DIR = os.path.join(BASE_DIR, "data", "teams", "london_city_lionesses")

os.makedirs(RAW_DATA_DIR, exist_ok=True)
os.makedirs(LCL_DATA_DIR, exist_ok=True)

def flatten_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Flattens MultiIndex headers into clean snake_case column names.
    """
    if isinstance(df.columns, pd.MultiIndex):
        new_cols = []
        for col in df.columns:
            top = str(col[0]).strip().lower().replace(" ", "_")
            bottom = str(col[1]).strip().lower().replace(" ", "_")
            if "unnamed" in top or top == bottom:
                new_cols.append(bottom)
            else:
                new_cols.append(f"{top}_{bottom}")
        df.columns = new_cols
    else:
        df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]
    return df

def filter_lcl_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filters DataFrame rows for London City Lionesses.
    Checks common squad/team column names.
    """
    for col in df.columns:
        if "squad" in col.lower() or "team" in col.lower():
            mask = df[col].astype(str).str.contains("Lionesses", case=False, na=False)
            filtered = df[mask]
            if not filtered.empty:
                return filtered
    return df

def main():
    print("=== WSL Data Hub Pipeline Starting ===")
    print(f"Target Raw Dir: {RAW_DATA_DIR}")
    print(f"Target LCL Dir: {LCL_DATA_DIR}\n")

    fb = sfc.FBref()
    # Comprehensive list of all 11 official FBref categories
    stat_types = [
        "standard",
        "goalkeeping",
        "advanced goalkeeping",
        "shooting",
        "passing",
        "pass types",
        "goal and shot creation",
        "defensive",
        "possession",
        "playing time",
        "misc"
    ]
    
    OVERWRITE = False  # Set to True if you want to force re-downloading existing tables
    total_files_saved = 0

    for st in stat_types:
        st_clean = st.replace(" ", "_")
        check_file = os.path.join(RAW_DATA_DIR, f"wsl_{st_clean}_squad.csv")
        if os.path.exists(check_file) and not OVERWRITE:
            print(f"⏩ Skipping stat_type '{st}' - files already exist locally.")
            continue

        print(f"\n---> Fetching stat_type: '{st}' for WSL 2025-2026...")
        try:
            res_dict = fb.scrape_stats("2025-2026", "England WSL", st)
            
            if not isinstance(res_dict, dict):
                res_dict = {"table": res_dict}

            for key, df in res_dict.items():
                if not isinstance(df, pd.DataFrame):
                    continue

                clean_df = flatten_columns(df.copy())
                key_clean = str(key).lower().replace(" ", "_")
                
                # 1. Save Full League Raw CSV
                raw_filename = f"wsl_{st_clean}_{key_clean}.csv"
                raw_filepath = os.path.join(RAW_DATA_DIR, raw_filename)
                clean_df.to_csv(raw_filepath, index=False, encoding="utf-8-sig")
                print(f" Saved Raw League File: {raw_filename} (Shape: {clean_df.shape})")
                total_files_saved += 1

                # 2. Filter and Save LCL Specific Subset
                lcl_df = filter_lcl_data(clean_df)
                if not lcl_df.empty:
                    lcl_filename = f"lcl_{st_clean}_{key_clean}.csv"
                    lcl_filepath = os.path.join(LCL_DATA_DIR, lcl_filename)
                    lcl_df.to_csv(lcl_filepath, index=False, encoding="utf-8-sig")
                    print(f"   Saved LCL Subset File: {lcl_filename} (Shape: {lcl_df.shape})")
                    total_files_saved += 1

        except Exception as e:
            print(f"❌ Error fetching stat_type '{st}': {e}")

        # Sleep briefly between stat types to be respectful to FBref
        time.sleep(1)

    print(f"\n=== WSL Data Hub Pipeline Complete! Total Files Created: {total_files_saved} ===")

if __name__ == "__main__":
    main()
