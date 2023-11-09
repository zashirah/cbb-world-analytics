select 
    title as episode_title,
    episode_href,
    episode_number,
    {{ dbt_utils.generate_surrogate_key(['episode_href']) }} as episode_id,
    release_date::date as release_date,
    hosted_by as hosts,
    guests,
    characters

from {{ source('raw', 'cbb_episodes')}}
