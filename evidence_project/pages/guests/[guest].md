```guests_per_ep
select 
    fct_episode.episode_title, 
    fct_episode.episode_number, 
    fct_episode.release_date, 
    date_part('year', fct_episode.release_date) as release_year,
    fct_episode.best_of_flag, 
    fct_episode.special_episode,
    dim_guest.lower_guest_href[7:] as guest_link, 
    dim_guest.guest_name,
    dim_guest.guest_id,

    count(*) as guests

from fct_episode 
inner join xref_episode_guest
using (episode_title)
inner join dim_guest
using (guest_name)

where upper(fct_episode.episode_title) not like 'BEST OF%'

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

## Characters

```character_guests
select
    dim_guest.guest_name,
    dim_character.character_name,
    dim_guest.lower_guest_href[7:] as guest_link, 
    '/characters/' || lower_character_href[7:] as character_link,
    count(*) as episodes,
    sum(case when fct_episode.best_of_flag then 1 else 0 end) as best_of_episodes,
    sum(case when fct_episode.best_of_flag then 1 else 0 end) / count(*) as best_of_rate,
    sum(case when fct_episode.special_episode then 1 else 0 end) as special_episodes

from dim_guest
inner join xref_character_guest
using (guest_name)
inner join dim_character 
using (character_name)
inner join xref_episode_character
using (character_name)
inner join fct_episode
using (episode_title)

group by all

order by episodes desc
```

<DataTable data="{character_guests.filter(d => d.guest_link === $page.params.guest)}" link=character_link>
    <Column id="character_name" />
    <Column id="episodes" />
    <Column id="best_of_episodes" />
    <Column id="best_of_rate" fmt=pct0/>
    <Column id="special_episodes" />
</DataTable>