"""
WSL Data Hub - Central Path Configuration Module
================================================
Centralizes all directory and file paths used across data ingestion,
processing, calculation, and visualization scripts.
"""

from pathlib import Path

# Base Paths
SCRIPTS_DIR = Path(__file__).resolve().parent
HUB_ROOT = SCRIPTS_DIR.parent
WORKSPACE_ROOT = HUB_ROOT.parent

# Data Directories
DATA_DIR = HUB_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
LEAGUE_DIR = RAW_DIR / "league"
SQUADS_DIR = RAW_DIR / "squads"
OPPONENTS_DIR = RAW_DIR / "opponents"
PLAYERS_DIR = RAW_DIR / "players"
SOURCE_FBREF_DIR = RAW_DIR / "source_fbref"
TEAMS_DIR = DATA_DIR / "teams"
LCL_DIR = TEAMS_DIR / "london_city_lionesses"
LCL_SQUAD_DIR = LCL_DIR / "squad"
LCL_PLAYERS_DIR = LCL_DIR / "players"
LCL_OPPONENTS_DIR = LCL_DIR / "opponents"

# Processed & Jekyll Data Directories
SITE_DATA_DIR = HUB_ROOT / "_data"
SITE_SQUADS_DIR = SITE_DATA_DIR / "squads"
ASSETS_DATA_DIR = HUB_ROOT / "assets" / "data"

# Output & Assets Directories
ASSETS_IMAGES_DIR = HUB_ROOT / "assets" / "images"
EVALUATIONS_CHARTS_DIR = ASSETS_IMAGES_DIR / "evaluations"
PREVIEWS_DIR = ASSETS_IMAGES_DIR / "table_previews"

# Specific File Paths
LEAGUE_TABLE_RAW_CSV = LEAGUE_DIR / "wsl_table_test.csv"
FBREF_DICTIONARY_JSON = SOURCE_FBREF_DIR / "fbref_data_dictionary.json"
TEAMS_METADATA_JSON = SITE_DATA_DIR / "teams_metadata.json"
PERFORMANCE_EVAL_JSON = SITE_DATA_DIR / "performance_evaluations.json"
BASELINE_SUMMARY_JSON = SITE_DATA_DIR / "baseline_q1_summary.json"


def ensure_all_directories():
    """Create all required directories if they do not exist."""
    dirs = [
        RAW_DIR,
        LEAGUE_DIR,
        SQUADS_DIR,
        OPPONENTS_DIR,
        PLAYERS_DIR,
        SOURCE_FBREF_DIR,
        TEAMS_DIR,
        LCL_DIR,
        SITE_DATA_DIR,
        SITE_SQUADS_DIR,
        ASSETS_DATA_DIR,
        EVALUATIONS_CHARTS_DIR,
        PREVIEWS_DIR,
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    ensure_all_directories()
    print("All project directories verified and ready.")
