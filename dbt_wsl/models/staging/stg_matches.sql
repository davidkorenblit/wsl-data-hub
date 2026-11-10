with source_data as (
    select
        id as match_id,
        round as matchweek_round,
        date as match_date_utc,
        home as home_team,
        home_id as home_team_id,
        home_score,
        away as away_team,
        away_id as away_team_id,
        away_score,
        score as score_display,
        finished as is_finished,
        started as is_started,
        season
    from {{ source('raw', 'matches') }}
)

select * from source_data
