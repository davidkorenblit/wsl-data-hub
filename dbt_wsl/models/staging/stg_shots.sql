with source_data as (
    select
        shot_id,
        match_id,
        team_id,
        player_id,
        player_name,
        minute,
        minute_added,
        period,
        x,
        y,
        xg,
        xgot,
        event_type,
        shot_type,
        situation,
        is_blocked,
        is_on_target,
        is_from_inside_box,
        is_own_goal,
        season
    from {{ source('raw', 'shots') }}
)

select * from source_data
