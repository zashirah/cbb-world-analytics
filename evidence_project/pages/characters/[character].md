# {$page.params.character}

## CBB Summary

```characters_per_ep
select 
    episode_title, 
    episode_number, 
    release_date, 
    date_part('year', release_date) as release_year,
    best_of_flag, 
    special_episode,
    lower_character_href[7:] as character_link, 
    count(*) as characters

from fct_episode 
inner join xref_episode_character
using (episode_id)
inner join dim_character
using (character_id)

where upper(episode_title) not like 'BEST OF%'

group by all

order by release_date desc
```

<BarChart 
    data={characters_per_ep.filter(d => d.character_link === $page.params.character)} 
    x=release_date 
    y={['characters', 'best_of_flag', 'special_episode']} 
    type=grouped
    yMax=1
/>

## Episodes per Year 

```character_yearly_totals
select 
    release_year,
    character_link, 
    count(*) as episodes

from ${characters_per_ep}

group by all

order by 1 desc
```

<BarChart 
    data={character_yearly_totals.filter(d => d.character_link === $page.params.character)} 
    x=release_year
    y={['episodes']}
    type=grouped
/>
