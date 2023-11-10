select distinct host_id, host_href, host_name
from {{ ref('explode_hosts_from_episodes') }}
where host_name is not null