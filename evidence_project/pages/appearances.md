## CBB Guests

```guests_ep_total
select 
    guest_name, 
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
having episodes >= 25
```

<BarChart 
    data={guests_ep_total} 
    x=guest_name 
    y={['best_of_episodes','non_best_of_episodes']}
    swapXY=true
/>

## CBB Characters

```characters_ep_total
select 
    character_name, 
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
having episodes >= 10
```

<BarChart 
    data={characters_ep_total} 
    x=character_name 
    y={['best_of_episodes','non_best_of_episodes']}
    swapXY=true
/>
