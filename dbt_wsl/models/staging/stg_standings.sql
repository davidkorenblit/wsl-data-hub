with source_data as (
    select
        rk as league_rank,
        squad as team_name,
        slug as team_slug,
        mp as matches_played,
        w as wins,
        d as draws,
        l as losses,
        gf as goals_for,
        ga as goals_against,
        gd as goal_difference,
        pts as points,
        season
    from {{ source('raw', 'standings') }}
)

select * from source_data
