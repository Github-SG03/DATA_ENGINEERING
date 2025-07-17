with raw_genome_scores as
(
	select
        *
	from
		movielens.raw.raw_genome_scores
)
select 
    movieid as movie_id,
    tagid as tag_id,
    relevance
from
    raw_genome_scores
