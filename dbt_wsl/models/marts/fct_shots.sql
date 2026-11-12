with s as (
    select * from {{ ref('stg_shots') }}
),
m as (
    select * from {{ ref('stg_matches') }}
)

select
    s.shot_id,
    s.match_id,
    m.matchweek_round,
    m.match_date_utc,
    s.season,
    s.team_id,
    case
        when s.team_id = m.home_team_id then m.home_team
        when s.team_id = m.away_team_id then m.away_team
        else null
    end as team_name,
    case
        when s.team_id = m.home_team_id then m.away_team
        when s.team_id = m.away_team_id then m.home_team
        else null
    end as opponent_team,
    s.player_id,
    s.player_name,
    s.minute,
    s.minute_added,
    s.period,
    s.x,
    s.y,
    s.xg,
    s.xgot,
    s.event_type,
    (s.event_type = 'Goal') as is_goal,
    s.shot_type,
    s.situation,
    s.is_blocked,
    s.is_on_target,
    s.is_from_inside_box,
    s.is_own_goal
from s
left join m on s.match_id = m.match_id
