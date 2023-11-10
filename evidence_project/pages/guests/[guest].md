# {$page.params.guest}

```guests
select *
from dim_guest
```

## CBB Summary

```guests_per_ep
select 
    episode_title, 
    episode_number, 
    release_date, 
    date_part('year', release_date) as release_year,
    best_of_flag, 
    special_episode,
    guest_href[7:] as guest_link, 
    count(*) as guests

from fct_episode 
inner join xref_episode_guest
using (episode_id)
inner join dim_guest
using (guest_id)

where upper(episode_title) not like 'BEST OF%'

group by all
```

<BarChart 
    data={guests_per_ep.filter(d => d.guest_link === $page.params.guest)} 
    x=release_date 
    y={['guests', 'best_of_flag', 'special_episode']} 
    type=grouped
    yMax=1
/>

## Episodes per Year 

```guest_yearly_totals
select 
    release_year,
    guest_link, 
    count(*) as episodes

from ${guests_per_ep}

group by all

order by 1 desc
```

<BarChart 
    data={guest_yearly_totals.filter(d => d.guest_link === $page.params.guest)} 
    x=release_year
    y={['episodes']}
    type=grouped
/>
