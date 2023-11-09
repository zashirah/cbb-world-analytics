select host_id, episode_id 
from {{ ref('explode_hosts') }}
where host_name is not null