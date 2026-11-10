with standings as (
    select distinct
        team_name,
        team_slug
    from {{ ref('stg_standings') }}
)

select
    row_number() over (order by team_name) as team_id,
    team_name,
    team_slug
from standings
