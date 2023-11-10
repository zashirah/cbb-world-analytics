select distinct 
    a.character_id, 
    a.character_href, 
    b.lower_character_href, 
    a.character_name,
    b.number_of_wiki_appearances,
    b.first_episode,
    b.latest_episode

from {{ ref('explode_characters') }} a
left join {{ ref('stg_characters') }} b
using (character_id)

where a.character_name is not null