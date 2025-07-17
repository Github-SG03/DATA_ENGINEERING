{{ config(
    materialized = 'table'
) }}

WITH fact_movies_with_tags AS (
    SELECT * FROM {{ ref('dim_movies_with_tags') }}
)

SELECT * FROM fact_movies_with_tags
