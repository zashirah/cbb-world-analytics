with unioned as (
    select * from {{ ref('base_cbb_episodes')}}
    union
    select * from {{ ref('base_special_episodes')}}
)
select distinct *
from unioned