with src_tags as (
    select * from src_genome_tags
)
select 
      tag_id,
      INITCAP(TRIM(tag)) as tag_name
from
    src_tags
