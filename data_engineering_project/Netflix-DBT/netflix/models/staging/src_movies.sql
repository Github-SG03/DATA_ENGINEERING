with raw_movies as
(
	select
        *
	from
		movielens.raw.raw_movies  --select * from {{source('netflix','r_movies')}} are same as we have crated the sources
)
select 
    movieid as movie_id,
    title,
    genres
from
    raw_movies
