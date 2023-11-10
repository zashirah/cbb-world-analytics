select host_id, episode_id 
from {{ ref('explode_hosts_from_episodes') }}
where host_name is not null