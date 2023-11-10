select distinct
    {{ dbt_utils.generate_surrogate_key(['href']) }} as guest_id,
    href as guest_href,
    lower(href) as lower_guest_href,
    name as guest_name,
    number_of_appearances as number_of_wiki_appearances, 
    characters,
    first_episode,
    latest_episode

from {{ source('raw', 'guests') }}