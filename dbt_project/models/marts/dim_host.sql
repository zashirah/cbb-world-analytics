select distinct host_id, host_href, host_name
from {{ ref('explode_hosts') }}
where host_name is not null