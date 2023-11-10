select guest_id, episode_id, guest_name, episode_title
from {{ ref('explode_guests_from_episodes') }}
where guest_name is not null