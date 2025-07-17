{{ config(
    materialized = 'ephemeral'
) }}

WITH src_ratings AS (
    SELECT * FROM {{ ref('dim_movies') }}
),
tags as (
    select * from {{ref('dim_genome_tags')}}
),
scores as (
    select * fro {{ref('fact_genome_scores')}}
)

SELECT
     m.movie_id,
     m.movie_title,
     m.genres,
     t.tag_name,
     s.relevance_score
FROM 
     movies m
LEFT JOIN SCORES S ON m.movie_id=s.movie_id
LEFT JOIN tags t on t.tag_id=s.tag_id

