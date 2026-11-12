with ps as (
    select * from {{ ref('stg_match_player_stats') }}
),
m as (
    select * from {{ ref('stg_matches') }}
)

select
    ps.match_id || '_' || ps.player_id as player_match_key,
    ps.match_id,
    m.matchweek_round,
    m.match_date_utc,
    ps.season,
    ps.player_id,
    ps.player_name,
    ps.team_id,
    ps.team_name,
    case
        when ps.team_id = m.home_team_id then true
        when ps.team_id = m.away_team_id then false
        else null
    end as is_home,
    case
        when ps.team_id = m.home_team_id then m.away_team
        when ps.team_id = m.away_team_id then m.home_team
        else null
    end as opponent_team,
    ps.is_goalkeeper,
    ps.position_id,
    ps.minutes_played,
    ps.fotmob_rating,
    ps.touches,
    ps.goals,
    ps.assists,
    ps.xg,
    ps.xgot,
    ps.xa,
    ps.npxg,
    ps.total_shots,
    ps.shots_on_target,
    ps.chances_created,
    ps.big_chances_created,
    ps.touches_opp_box,
    ps.dribbles_succeeded,
    ps.dribbles_attempted,
    ps.dispossessed,
    ps.accurate_passes,
    ps.passes_attempted,
    round(cast(ps.accurate_passes as numeric) / nullif(ps.passes_attempted, 0) * 100, 1) as pass_accuracy_pct,
    ps.passes_final_third,
    ps.accurate_long_balls,
    ps.long_balls_attempted,
    ps.defensive_actions,
    ps.tackles,
    ps.blocks,
    ps.clearances,
    ps.interceptions,
    ps.recoveries,
    ps.dribbled_past,
    ps.ground_duels_won,
    ps.ground_duels_attempted,
    ps.aerial_duels_won,
    ps.aerial_duels_attempted,
    ps.duels_won,
    ps.duels_lost,
    ps.was_fouled,
    ps.fouls_committed
from ps
left join m on ps.match_id = m.match_id
