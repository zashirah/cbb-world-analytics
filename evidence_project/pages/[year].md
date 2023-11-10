{$page.params.year}

## Yearly Summary

```guests_per_ep
select 
    episode_title, 
    episode_number, 
    release_date, 
    date_part('year', release_date)::string as release_year,
    case when best_of_flag then 25 else 0 end as best_of_flag, 
    case when special_episode then 25 else 0 end as special_episode_flag, 
    count(*) as characters

from fct_episode 
inner join xref_episode_guest
using (episode_id)
inner join dim_guest
using (guest_id)

where upper(episode_title) not like 'BEST OF%'

group by all

order by release_date desc
```

<Chart 
    data={guests_per_ep.filter(d => d.release_year === $page.params.year)} 
    x=release_date 
    yMax=20
>
    <Line y=characters/>
    <Bar y=best_of_flag/>
    <Bar y=special_episode_flag/>
</Chart >

## CBB Guests

```guests_ep_total
select 
    guest_name, 
    date_part('year', release_date)::string as release_year,
    sum(case when best_of_flag then 1 else 0 end) as best_of_episodes, 
    sum(case when not best_of_flag then 1 else 0 end) as non_best_of_episodes, 
    count(*) as episodes
from fct_episode 
inner join xref_episode_guest
using (episode_id)
inner join dim_guest
using (guest_id)
where upper(episode_title) not like 'BEST OF%'
group by all
```

<BarChart 
    data={guests_ep_total.filter(d => d.release_year === $page.params.year)} 
    x=guest_name 
    y={['best_of_episodes','non_best_of_episodes']}
    swapXY=true
/>

## CBB Characters

```characters_ep_total
select 
    character_name, 
    date_part('year', release_date)::string as release_year,
    sum(case when best_of_flag then 1 else 0 end) as best_of_episodes, 
    sum(case when not best_of_flag then 1 else 0 end) as non_best_of_episodes, 
    count(*) as episodes
from fct_episode 
inner join xref_episode_character
using (episode_id)
inner join dim_character
using (character_id)
where upper(episode_title) not like 'BEST OF%'
group by all
```

<BarChart 
    data={characters_ep_total.filter(d => d.release_year === $page.params.year)} 
    x=character_name 
    y={['best_of_episodes','non_best_of_episodes']}
    swapXY=true
/>
