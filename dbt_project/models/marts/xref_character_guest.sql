select guest_id, character_id, guest_name, case when character_name = 'Gino Lambardo' then 'Gino Lombardo' else character_name end as character_name
from {{ ref('explode_guests_from_characters') }}
where played_by_name is not null