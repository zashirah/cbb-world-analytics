
```characters_per_ep
select 
    episode_title, 
    episode_number, 
    release_date, 
    date_part('year', release_date) as release_year,
    best_of_flag, 
    special_episode,
    lower_character_href[7:] as character_link, 
    character_name,
    character_id,
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

# <Value data={characters_per_ep.filter(d => d.character_link === $page.params.character)} column=character_name />

```character_totals
select 
    character_id,
    character_link, 
    character_name,
    count(*) as episodes,
    sum(case when best_of_flag then 1 else 0 end) as best_of_episodes,
    sum(case when best_of_flag then 1 else 0 end) / count(*) as best_of_rate,
    sum(case when special_episode then 1 else 0 end) as special_episodes

from ${characters_per_ep}

group by all
```

<BigValue data={character_totals.filter(d => d.character_link === $page.params.character)} value=episodes />
<BigValue data={character_totals.filter(d => d.character_link === $page.params.character)} value=best_of_episodes />
<BigValue data={character_totals.filter(d => d.character_link === $page.params.character)} value=best_of_rate fmt=pct0 />
<BigValue data={character_totals.filter(d => d.character_link === $page.params.character)} value=special_episodes />

## CBB Summary

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

## Episodes 

<DataTable data="{characters_per_ep.filter(d => d.character_link === $page.params.character)}" >
    <Column id="episode_title" />
    <Column id="episode_number" />
    <Column id="release_date" />
    <Column id="character_name" />
    <Column id="best_of_flag" />
    <Column id="special_episode" />
</DataTable>
