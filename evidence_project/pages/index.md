# Full CBB Episode History

CBB World (or Comedy Bang Bang World) is the product of Scott Aukerman, amongst others. There has been a show, a long running podcase, and a book. I've been a weekly listener since 2016, a subscriber to CBB World since that began, and I greatly appreciate all the work that goes into the program. So I decided to build an app that could show me some metrics around CBB episodes. 

There is a wiki site that all of this data is sourced from: https://comedybangbang.fandom.com/wiki/Main_Page. There are a few python modules that I wrote to help scrape the data from the site. The data on DuckDB/Motherduck and transformed with dbt-duckdb. This site is built with evidence.dev which I have a used a few times and greatly enjoyed. 

Check out the repo here: https://github.com/zashirah/cbb-world-analytics

If you have any ideas for graphics/new data/etc, reach out to me on Twitter (@zachsshirah) or submit an issue on the GitHub repo.

Have fun!

## Click the year below to see a detailed yearly view

```best_ofs
select 
    date_part('year', release_date)::string as release_year, 
    '/years/' || release_year as release_year_link,
    sum(case when best_of_flag then 1 else 0 end) as best_of_count,
    sum(case when special_episode then 1 else 0 end) as special_episode_count,
    count(*) episode_count
from fct_episode 
where release_year != '2023'
group by all
order by release_year desc
```

<DataTable data="{best_ofs}" link=release_year_link>
    <Column id="release_year" />
    <Column id="episode_count" />
    <Column id="best_of_count" />
    <Column id="special_episode_count" />
</DataTable>

## CBB Summary

```guests_per_ep
select 
    episode_title, 
    episode_number, 
    release_date, 
    date_part('year', release_date)::string as release_year,
    case when best_of_flag then 100 else 0 end as best_of_flag, 
    case when special_episode then 100 else 0 end as special_episode_flag, 
    count(*) as characters

from fct_episode 
inner join xref_episode_guest
using (episode_title)
inner join dim_guest
using (guest_name)

where upper(episode_title) not like 'BEST OF%'

group by all

order by release_date desc
```

<Chart 
    data={guests_per_ep} 
    x=release_date 
    yMax=25
>
    <Line y=characters/>
    <Bar y=best_of_flag/>
    <Bar y=special_episode_flag/>
</Chart >

## Top CBB Guests

```guests_ep_total
select 
    dim_guest.guest_name, 
    sum(case when best_of_flag then 1 else 0 end) as best_of_episodes, 
    sum(case when not best_of_flag then 1 else 0 end) as non_best_of_episodes, 
    count(*) as episodes
from fct_episode 
inner join xref_episode_guest
using (episode_id)
inner join dim_guest
using (guest_id)
where upper(fct_episode.episode_title) not like 'BEST OF%'
group by all
having episodes >= 25
```

<BarChart 
    data={guests_ep_total} 
    x=guest_name 
    y={['best_of_episodes','non_best_of_episodes']}
    swapXY=true
/>

## Top CBB Characters

```characters_ep_total
select 
    dim_character.character_name, 
    sum(case when best_of_flag then 1 else 0 end) as best_of_episodes, 
    sum(case when not best_of_flag then 1 else 0 end) as non_best_of_episodes, 
    count(*) as episodes
from fct_episode 
inner join xref_episode_character
using (episode_title)
inner join dim_character
using (character_name)
where upper(fct_episode.episode_title) not like 'BEST OF%'
group by all
having episodes >= 10
```

<BarChart 
    data={characters_ep_total} 
    x=character_name 
    y={['best_of_episodes','non_best_of_episodes']}
    swapXY=true
/>
