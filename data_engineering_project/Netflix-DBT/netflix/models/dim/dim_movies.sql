with movies as (
    select * from src_movies
)
select
    movie_id,
    INITCAP(TRIM(title)) as movie_title,
    SPLIT(genres,'|') as genres_array,
    genres
from movies