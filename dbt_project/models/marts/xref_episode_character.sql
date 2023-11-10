select character_id, episode_id, case when character_name = 'Gino Lambardo' then 'Gino Lombardo' else character_name end as character_name, episode_title
from {{ ref('explode_characters_from_episodes') }}
where character_name is not null