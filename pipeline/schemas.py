"""
WSL Data Platform - Data Contracts & Schemas
============================================
Pydantic validation models for raw ingress data from FotMob API.
Ensures schema integrity before persisting into the Data Lake.
"""
from typing import Optional
from pydantic import BaseModel, Field, field_validator


class MatchRecord(BaseModel):
    """Schema contract for a single WSL match / fixture."""
    id: int = Field(..., description="Unique match identifier from source")
    round: Optional[int] = Field(None, description="Matchweek round number (1-22)")
    date: Optional[str] = Field(None, description="UTC match start timestamp")
    home: str = Field(..., description="Home team display name")
    home_id: Optional[int] = Field(None, description="Home team unique ID")
    home_score: Optional[int] = Field(None, description="Home goals scored")
    away: str = Field(..., description="Away team display name")
    away_id: Optional[int] = Field(None, description="Away team unique ID")
    away_score: Optional[int] = Field(None, description="Away goals scored")
    score: Optional[str] = Field(None, description="Formatted score string (e.g. '2 - 1')")
    finished: bool = Field(False, description="Whether match has completed")
    started: bool = Field(False, description="Whether match has kicked off")
    reason: Optional[str] = Field(None, description="Cancellation or postponement reason if any")
    season: str = Field(..., description="Season slug, e.g. 2026/2027")


class StandingRecord(BaseModel):
    """Schema contract for a single team row in league standings."""
    rk: int = Field(..., ge=1, le=20, description="Rank in table")
    squad: str = Field(..., description="Team display name")
    slug: str = Field(..., description="URL-friendly team slug")
    mp: int = Field(..., ge=0, description="Matches played")
    w: int = Field(..., ge=0, description="Wins")
    d: int = Field(..., ge=0, description="Draws")
    l: int = Field(..., ge=0, description="Losses")
    gf: int = Field(..., ge=0, description="Goals for (scored)")
    ga: int = Field(..., ge=0, description="Goals against (conceded)")
    gd: int = Field(..., description="Goal difference (gf - ga)")
    pts: int = Field(..., ge=0, description="Total points")
    season: str = Field(..., description="Season slug, e.g. 2026/2027")

    @field_validator("gd")
    @classmethod
    def validate_goal_diff(cls, v, info):
        gf = info.data.get("gf")
        ga = info.data.get("ga")
        if gf is not None and ga is not None:
            expected = gf - ga
            if v != expected:
                # auto-correct if slight source discrepancy
                return expected
        return v


class PlayerMatchStatRecord(BaseModel):
    """Schema contract for a player's per-match micro-statistics from FotMob matchDetails."""
    match_id: int = Field(..., description="Unique match identifier")
    player_id: int = Field(..., description="Unique FotMob player identifier")
    player_name: str = Field(..., description="Player display name")
    team_id: int = Field(..., description="Team unique identifier")
    team_name: Optional[str] = Field(None, description="Team display name")
    is_goalkeeper: bool = Field(False, description="Whether player is a goalkeeper")
    position_id: Optional[int] = Field(None, description="Match position ID")
    season: str = Field(..., description="Season slug, e.g. 2026/2027")

    # Core & Rating
    minutes_played: int = Field(0, ge=0, description="Minutes played")
    fotmob_rating: Optional[float] = Field(None, description="FotMob match rating")
    touches: int = Field(0, ge=0, description="Total touches")

    # Attack & Creation
    goals: int = Field(0, ge=0)
    assists: int = Field(0, ge=0)
    xg: float = Field(0.0, ge=0.0, description="Expected goals (xG)")
    xgot: float = Field(0.0, ge=0.0, description="Expected goals on target (xGOT)")
    xa: float = Field(0.0, ge=0.0, description="Expected assists (xA)")
    npxg: float = Field(0.0, ge=0.0, description="Non-penalty xG")
    total_shots: int = Field(0, ge=0)
    shots_on_target: int = Field(0, ge=0)
    chances_created: int = Field(0, ge=0)
    big_chances_created: int = Field(0, ge=0)
    touches_opp_box: int = Field(0, ge=0, description="Touches in opposition box")
    dribbles_succeeded: int = Field(0, ge=0)
    dribbles_attempted: int = Field(0, ge=0)
    dispossessed: int = Field(0, ge=0)

    # Passing
    accurate_passes: int = Field(0, ge=0)
    passes_attempted: int = Field(0, ge=0)
    passes_final_third: int = Field(0, ge=0)
    accurate_long_balls: int = Field(0, ge=0)
    long_balls_attempted: int = Field(0, ge=0)

    # Defense & Duels
    defensive_actions: int = Field(0, ge=0)
    tackles: int = Field(0, ge=0)
    blocks: int = Field(0, ge=0)
    clearances: int = Field(0, ge=0)
    interceptions: int = Field(0, ge=0)
    recoveries: int = Field(0, ge=0)
    dribbled_past: int = Field(0, ge=0)
    ground_duels_won: int = Field(0, ge=0)
    ground_duels_attempted: int = Field(0, ge=0)
    aerial_duels_won: int = Field(0, ge=0)
    aerial_duels_attempted: int = Field(0, ge=0)
    duels_won: int = Field(0, ge=0)
    duels_lost: int = Field(0, ge=0)
    was_fouled: int = Field(0, ge=0)
    fouls_committed: int = Field(0, ge=0)


class ShotRecord(BaseModel):
    """Schema contract for a single shot event from FotMob matchDetails shotmap."""
    shot_id: int = Field(..., description="Unique shot event ID")
    match_id: int = Field(..., description="Unique match identifier")
    team_id: int = Field(..., description="Shooting team ID")
    player_id: int = Field(..., description="Shooter player ID")
    player_name: str = Field(..., description="Shooter display name")
    minute: int = Field(..., ge=0, description="Match minute")
    minute_added: Optional[int] = Field(None, description="Stoppage time added minutes")
    period: Optional[str] = Field(None, description="Match period (FirstHalf, SecondHalf, etc.)")
    x: float = Field(..., description="Pitch X coordinate (0-105)")
    y: float = Field(..., description="Pitch Y coordinate (0-68)")
    xg: float = Field(0.0, ge=0.0, description="Shot expected goals (xG)")
    xgot: float = Field(0.0, ge=0.0, description="Shot expected goals on target (xGOT)")
    event_type: str = Field(..., description="Goal, AttemptSaved, Miss, Post")
    shot_type: Optional[str] = Field(None, description="RightFoot, LeftFoot, Header, etc.")
    situation: Optional[str] = Field(None, description="RegularPlay, FromCorner, FastBreak, etc.")
    is_blocked: bool = Field(False)
    is_on_target: bool = Field(False)
    is_from_inside_box: bool = Field(False)
    is_own_goal: bool = Field(False)
    season: str = Field(..., description="Season slug, e.g. 2026/2027")
