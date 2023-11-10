```guests_per_ep
select 
    episode_title, 
    episode_number, 
    release_date, 
    date_part('year', release_date) as release_year,
    best_of_flag, 
    special_episode,
    lower_guest_href[7:] as guest_link, 
    guest_name,
    guest_id,

    count(*) as guests

from fct_episode 
inner join xref_episode_guest
using (episode_id)
inner join dim_guest
using (guest_id)

where upper(episode_title) not like 'BEST OF%'

group by all
```
# <Value data={guests_per_ep.filter(d => d.guest_link === $page.params.guest)} column=guest_name />

```guest_totals
select 
    guest_id,
    guest_link, 
    guest_name,
    count(*) as episodes,
    sum(case when best_of_flag then 1 else 0 end) as best_of_episodes,
    sum(case when best_of_flag then 1 else 0 end) / count(*) as best_of_rate,
    sum(case when special_episode then 1 else 0 end) as special_episodes

from ${guests_per_ep}

group by all
```

<BigValue data={guest_totals.filter(d => d.guest_link === $page.params.guest)} value=episodes />
<BigValue data={guest_totals.filter(d => d.guest_link === $page.params.guest)} value=best_of_episodes />
<BigValue data={guest_totals.filter(d => d.guest_link === $page.params.guest)} value=best_of_rate fmt=pct0 />
<BigValue data={guest_totals.filter(d => d.guest_link === $page.params.guest)} value=special_episodes />

## CBB Summary

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

## Episodes 

<DataTable data="{guests_per_ep.filter(d => d.guest_link === $page.params.guest)}" >
    <Column id="episode_title" />
    <Column id="episode_number" />
    <Column id="release_date" />
    <Column id="guest_name" />
    <Column id="best_of_flag" />
    <Column id="special_episode" />
</DataTable>



