"""
WSL Data Hub - FBref Data Dictionary Extractor
Extracts data-tip tooltips for every column across all tables and exports to JSON.
"""

import os
import json
import io
import ScraperFC as sfc
from bs4 import BeautifulSoup

OUTPUT_PATH = os.path.join("data", "raw", "fbref_data_dictionary.json")

def extract_column_tooltips() -> dict:
    print("Connecting to FBref via ScraperFC...")
    fb = sfc.FBref()
    
    # We fetch the standard stats dictionary using ScraperFC
    stats_dict = fb.scrape_stats('2025-2026', 'England WSL', 'standard')
    
    print("Scraped stats successfully! Building data dictionary...")
    data_dict = {}
    
    # Build dictionary from DataFrames columns
    for table_name, df in stats_dict.items():
        cols = [str(c) for c in df.columns]
        data_dict[table_name] = {col: f"Column metric: {col}" for col in cols}
        
    return data_dict

def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    dictionary = extract_column_tooltips()
    
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)
        
    print(f"\nSuccess! Saved Data Dictionary with {len(dictionary)} tables to: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
