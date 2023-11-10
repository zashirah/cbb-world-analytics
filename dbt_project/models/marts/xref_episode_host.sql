select host_id, episode_id, host_name, episode_title
from {{ ref('explode_hosts_from_episodes') }}
where host_name is not null