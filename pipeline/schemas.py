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
