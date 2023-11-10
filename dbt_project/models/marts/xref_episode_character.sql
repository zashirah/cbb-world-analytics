select character_id, episode_id 
from {{ ref('explode_characters_from_episodes') }}
where character_name is not null