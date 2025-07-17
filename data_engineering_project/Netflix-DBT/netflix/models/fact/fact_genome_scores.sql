with src_scores as (
    select * from src_genome_score
)
select 
      movie_id,
      tag_id,
      Round(relevance,4) as relevance_score
from
    src_scores
where
     relevance > 0