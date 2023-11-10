select distinct 
    a.character_id, 
    a.character_href, 
    lower(a.character_href) as lower_character_href, 
    case when a.character_name = 'Gino Lambardo' then 'Gino Lombardo' else a.character_name end as character_name,
    b.number_of_wiki_appearances,
    b.first_episode,
    b.latest_episode

from {{ ref('explode_characters_from_episodes') }} a
left join {{ ref('stg_characters') }} b
using (character_id)

where a.character_name is not null
and a.character_href != '/wiki/Gino_Lambardo'