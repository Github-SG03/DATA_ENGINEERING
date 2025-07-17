{{ config(
    materialized = 'table'
) }}

WITH fact_ratings AS (
    SELECT * FROM {{ ref('fact_ratings') }}
),
seed_dates as(SELECT * FROM {{ref("seed_movies_release_date")}})

select
      f.*,
      case
          when d.release_date is null then 'unknown' else 'known'
      end as release_info_available
from
    fact_ratings f
LEFT JOIN seed_dates d
on f.movie_id=d.movie_id


