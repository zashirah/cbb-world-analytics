select 
    best_of_year,
    href as episode_href,
    {{ dbt_utils.generate_surrogate_key(['href']) }} as episode_id

from {{ source('raw', 'best_ofs')}}
