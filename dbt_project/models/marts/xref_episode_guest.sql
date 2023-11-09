select guest_id, episode_id 
from {{ ref('explode_guests') }}
where guest_name is not null