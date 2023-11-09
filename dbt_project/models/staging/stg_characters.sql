select distinct
    {{ dbt_utils.generate_surrogate_key(['href', 'name']) }} as character_id,
    href as character_href,
    name as character_name,
    number_of_appearances as number_of_wiki_appearances, 
    first_episode,
    latest_episode

from {{ source('raw', 'characters') }}