select 
    distinct a.guest_id, 
    a.guest_href, 
    lower(a.guest_href) as lower_guest_href, 
    a.guest_name,
    b.number_of_wiki_appearances,
    b.first_episode,
    b.latest_episode

from {{ ref('explode_guests_from_episodes') }} a 
left join {{ ref('stg_guests') }} b
using (guest_id)

where a.guest_name is not null