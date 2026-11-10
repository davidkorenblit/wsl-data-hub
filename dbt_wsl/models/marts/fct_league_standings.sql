with standings as (
    select * from {{ ref('stg_standings') }}
)

select
    league_rank,
    team_name,
    team_slug,
    season,
    matches_played,
    wins,
    draws,
    losses,
    goals_for,
    goals_against,
    goal_difference,
    points,
    -- Advanced Analytics Metrics
    round(cast(points as numeric) / nullif(matches_played, 0), 2) as points_per_match,
    round(cast(goals_for as numeric) / nullif(matches_played, 0), 2) as goals_scored_per_match,
    round(cast(goals_against as numeric) / nullif(matches_played, 0), 2) as goals_conceded_per_match
from standings
order by league_rank asc
