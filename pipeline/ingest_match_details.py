#!/usr/bin/env python3
"""
WSL Data Platform - Generic Micro-Data Ingestion Engine (Match Details)
=======================================================================
Incrementally fetches full FotMob matchDetails JSONs for finished matches,
persists the raw JSON payloads into the S3 Data Lake (Bronze Layer), and
normalizes the core 80-90% recurring metrics into columnar Parquet tables:
  - bronze/fotmob/matches/season=<season>/match_<id>.json (Raw Bronze)
  - bronze/match_player_stats/season=<season>/match_player_stats.parquet
  - bronze/shots/season=<season>/shots.parquet

Usage:
    python pipeline/ingest_match_details.py
    python pipeline/ingest_match_details.py --season 2026/2027
    python pipeline/ingest_match_details.py --local-only
"""

import os
import sys
import json
import time
import logging
import argparse
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from fotmob_api_client import FotMobAPIClient
from wsl_lake.storage import DataLakeStorage
from pipeline.schemas import PlayerMatchStatRecord, ShotRecord

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("MatchDetailsIngest")


def sanitize_season(season_str: str) -> str:
    """Converts '2026/2027' -> '2026_2027' for safe lake partition paths."""
    return season_str.replace("/", "_").replace("-", "_")


def _to_int(val: Any, default: int = 0) -> int:
    if val is None or val == "":
        return default
    try:
        return int(float(val))
    except (ValueError, TypeError):
        return default


def _to_float(val: Any, default: Optional[float] = 0.0) -> Optional[float]:
    if val is None or val == "":
        return default
    try:
        return float(val)
    except (ValueError, TypeError):
        return default


def _extract_stat_map(player_obj: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """Flattens all stat sections of a FotMob playerStats entry into {title: stat_dict}."""
    flat: Dict[str, Dict[str, Any]] = {}
    for section in player_obj.get("stats") or []:
        stats_dict = section.get("stats") or {}
        if isinstance(stats_dict, dict):
            for key, item in stats_dict.items():
                if isinstance(item, dict) and "stat" in item:
                    flat[key] = item["stat"] or {}
    return flat


def _val(smap: Dict[str, Dict[str, Any]], key: str) -> Any:
    return (smap.get(key) or {}).get("value")


def _frac(smap: Dict[str, Dict[str, Any]], key: str) -> Tuple[int, int]:
    entry = smap.get(key) or {}
    return _to_int(entry.get("value"), 0), _to_int(entry.get("total"), 0)


def parse_match_player_stats(
    match_id: int, raw_match: Dict[str, Any], season: str
) -> List[Dict[str, Any]]:
    """Extracts and validates per-player match statistics from matchDetails JSON."""
    content = raw_match.get("content") or {}
    player_stats = content.get("playerStats") or {}
    if not isinstance(player_stats, dict):
        return []

    records: List[Dict[str, Any]] = []
    for pid_str, p in player_stats.items():
        if not isinstance(p, dict):
            continue
        smap = _extract_stat_map(p)

        acc_passes, att_passes = _frac(smap, "Accurate passes")
        acc_long, att_long = _frac(smap, "Accurate long balls")
        drib_succ, drib_att = _frac(smap, "Successful dribbles")
        g_duels_won, g_duels_att = _frac(smap, "Ground duels won")
        a_duels_won, a_duels_att = _frac(smap, "Aerial duels won")

        try:
            rec = PlayerMatchStatRecord(
                match_id=match_id,
                player_id=_to_int(p.get("id") or pid_str),
                player_name=p.get("name") or "Unknown",
                team_id=_to_int(p.get("teamId")),
                team_name=p.get("teamName"),
                is_goalkeeper=bool(p.get("isGoalkeeper", False)),
                position_id=_to_int(p.get("positionId"), default=0) or None,
                season=season,
                minutes_played=_to_int(_val(smap, "Minutes played"), 0),
                fotmob_rating=_to_float(_val(smap, "FotMob rating"), default=None),
                touches=_to_int(_val(smap, "Touches"), 0),
                goals=_to_int(_val(smap, "Goals"), 0),
                assists=_to_int(_val(smap, "Assists"), 0),
                xg=_to_float(_val(smap, "Expected goals (xG)"), 0.0) or 0.0,
                xgot=_to_float(_val(smap, "Expected goals on target (xGOT)"), 0.0) or 0.0,
                xa=_to_float(_val(smap, "Expected assists (xA)"), 0.0) or 0.0,
                npxg=_to_float(_val(smap, "xG Non-penalty"), 0.0) or 0.0,
                total_shots=_to_int(_val(smap, "Total shots"), 0),
                shots_on_target=_to_int(_val(smap, "Shots on target"), 0),
                chances_created=_to_int(_val(smap, "Chances created"), 0),
                big_chances_created=_to_int(_val(smap, "Big chances created"), 0),
                touches_opp_box=_to_int(_val(smap, "Touches in opposition box"), 0),
                dribbles_succeeded=drib_succ,
                dribbles_attempted=drib_att,
                dispossessed=_to_int(_val(smap, "Dispossessed"), 0),
                accurate_passes=acc_passes,
                passes_attempted=att_passes,
                passes_final_third=_to_int(_val(smap, "Passes into final third"), 0),
                accurate_long_balls=acc_long,
                long_balls_attempted=att_long,
                defensive_actions=_to_int(_val(smap, "Defensive actions"), 0),
                tackles=_to_int(_val(smap, "Tackles"), 0),
                blocks=_to_int(_val(smap, "Blocks"), 0),
                clearances=_to_int(_val(smap, "Clearances"), 0),
                interceptions=_to_int(_val(smap, "Interceptions"), 0),
                recoveries=_to_int(_val(smap, "Recoveries"), 0),
                dribbled_past=_to_int(_val(smap, "Dribbled past"), 0),
                ground_duels_won=g_duels_won,
                ground_duels_attempted=g_duels_att,
                aerial_duels_won=a_duels_won,
                aerial_duels_attempted=a_duels_att,
                duels_won=_to_int(_val(smap, "Duels won"), 0),
                duels_lost=_to_int(_val(smap, "Duels lost"), 0),
                was_fouled=_to_int(_val(smap, "Was fouled"), 0),
                fouls_committed=_to_int(_val(smap, "Fouls committed"), 0),
            )
            records.append(rec.model_dump())
        except Exception as e:
            logger.warning(f"PlayerMatchStat validation error (match={match_id}, player={pid_str}): {e}")

    return records


def parse_match_shots(
    match_id: int, raw_match: Dict[str, Any], season: str
) -> List[Dict[str, Any]]:
    """Extracts and validates shotmap events from matchDetails JSON."""
    content = raw_match.get("content") or {}
    shotmap = content.get("shotmap") or {}
    shots = shotmap.get("shots") or []
    if not isinstance(shots, list):
        return []

    records: List[Dict[str, Any]] = []
    for s in shots:
        if not isinstance(s, dict):
            continue
        try:
            rec = ShotRecord(
                shot_id=_to_int(s.get("id")),
                match_id=match_id,
                team_id=_to_int(s.get("teamId")),
                player_id=_to_int(s.get("playerId")),
                player_name=s.get("playerName") or s.get("fullName") or "Unknown",
                minute=_to_int(s.get("min"), 0),
                minute_added=s.get("minAdded"),
                period=s.get("period"),
                x=_to_float(s.get("x"), 0.0) or 0.0,
                y=_to_float(s.get("y"), 0.0) or 0.0,
                xg=_to_float(s.get("expectedGoals"), 0.0) or 0.0,
                xgot=_to_float(s.get("expectedGoalsOnTarget"), 0.0) or 0.0,
                event_type=s.get("eventType") or "Unknown",
                shot_type=s.get("shotType"),
                situation=s.get("situation"),
                is_blocked=bool(s.get("isBlocked", False)),
                is_on_target=bool(s.get("isOnTarget", False)),
                is_from_inside_box=bool(s.get("isFromInsideBox", False)),
                is_own_goal=bool(s.get("isOwnGoal", False)),
                season=season,
            )
            records.append(rec.model_dump())
        except Exception as e:
            logger.warning(f"Shot validation error (match={match_id}, shot={s.get('id')}): {e}")

    return records


def _index_local_match_files() -> Dict[int, Path]:
    """Maps match_id -> local JSON path for any cached files in data/raw/fotmob/matches/."""
    local_dir = PROJECT_ROOT / "data" / "raw" / "fotmob" / "matches"
    mapping: Dict[int, Path] = {}
    if not local_dir.exists():
        return mapping
    for p in local_dir.glob("*.json"):
        stem_parts = p.stem.split("_")
        if stem_parts and stem_parts[-1].isdigit():
            mapping[int(stem_parts[-1])] = p
    return mapping


def run_match_details_ingest(
    season: str = "2026/2027",
    upload_lake: bool = True,
    local_only: bool = False,
    sleep_sec: float = 0.4,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Incremental matchDetails ingestion:
    1. Finds finished matches for the season.
    2. Uploads any missing match_<id>.json to S3 Data Lake Bronze.
    3. Parses all match JSONs into consolidated player_stats and shots Parquet datasets.
    """
    season_safe = sanitize_season(season)
    local_cache = _index_local_match_files()
    all_player_stats: List[Dict[str, Any]] = []
    all_shots: List[Dict[str, Any]] = []

    if local_only:
        logger.info(f"Running in --local-only mode over {len(local_cache)} cached match JSONs...")
        for match_id, path in sorted(local_cache.items()):
            with open(path, encoding="utf-8") as fp:
                raw_match = json.load(fp)
            all_player_stats.extend(parse_match_player_stats(match_id, raw_match, season))
            all_shots.extend(parse_match_shots(match_id, raw_match, season))
        df_ps = pd.DataFrame(all_player_stats)
        df_sh = pd.DataFrame(all_shots)
        logger.info(f"Parsed {len(df_ps)} player-match rows and {len(df_sh)} shot rows locally.")
        return df_ps, df_sh

    lake = DataLakeStorage()
    client = FotMobAPIClient()

    # 1. Get finished match IDs from Lake bronze/matches
    matches_key = f"bronze/matches/season={season_safe}/matches.parquet"
    df_matches = lake.download_parquet(key=matches_key)
    finished_ids = [
        int(mid)
        for mid in df_matches.loc[df_matches["finished"] == True, "id"].tolist()
    ]
    logger.info(f"Found {len(finished_ids)} finished matches in {matches_key}.")

    # 2. Check which match JSONs already exist in Lake Bronze
    prefix = f"bronze/fotmob/matches/season={season_safe}/"
    existing_keys = set(lake.list_objects(prefix=prefix))

    for match_id in finished_ids:
        key = f"{prefix}match_{match_id}.json"
        if key in existing_keys:
            raw_match = lake.download_json(key=key)
        elif match_id in local_cache:
            logger.info(f"Uploading local cached match_{match_id}.json to Data Lake...")
            with open(local_cache[match_id], encoding="utf-8") as fp:
                raw_match = json.load(fp)
            if upload_lake:
                lake.upload_json(raw_match, key=key)
        else:
            logger.info(f"Fetching matchDetails from FotMob API for match {match_id}...")
            raw_match = client.fetch_match_details(match_id)
            if not raw_match:
                logger.warning(f"Skipping match {match_id} (empty API response).")
                continue
            if upload_lake:
                lake.upload_json(raw_match, key=key)
            time.sleep(sleep_sec)

        all_player_stats.extend(parse_match_player_stats(match_id, raw_match, season))
        all_shots.extend(parse_match_shots(match_id, raw_match, season))

    df_ps = pd.DataFrame(all_player_stats)
    df_sh = pd.DataFrame(all_shots)

    if upload_lake:
        if not df_ps.empty:
            ps_key = f"bronze/match_player_stats/season={season_safe}/match_player_stats.parquet"
            lake.upload_parquet(df_ps, key=ps_key)
        if not df_sh.empty:
            sh_key = f"bronze/shots/season={season_safe}/shots.parquet"
            lake.upload_parquet(df_sh, key=sh_key)

    logger.info(
        f"🎉 MatchDetails ingest complete: {len(df_ps)} player-match rows, {len(df_sh)} shots."
    )
    return df_ps, df_sh


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WSL Match Details Micro-Data Ingestion")
    parser.add_argument("--season", type=str, default="2026/2027", help="Target season")
    parser.add_argument("--no-lake", action="store_true", help="Skip S3 Lake upload")
    parser.add_argument("--local-only", action="store_true", help="Parse local cached JSONs only")
    args = parser.parse_args()

    run_match_details_ingest(
        season=args.season,
        upload_lake=not args.no_lake,
        local_only=args.local_only,
    )
