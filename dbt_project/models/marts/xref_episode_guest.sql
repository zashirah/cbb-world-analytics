select guest_id, episode_id 
from {{ ref('explode_guests_from_episodes') }}
where guest_name is not null