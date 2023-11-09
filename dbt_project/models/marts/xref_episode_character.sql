select character_id, episode_id 
from {{ ref('explode_characters') }}
where character_name is not null