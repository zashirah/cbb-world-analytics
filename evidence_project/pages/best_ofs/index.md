## Guests per Episode

```guests_per_ep
select 
    episode_title, episode_number, release_date, 
    case when best_of_flag then 100 else 0 end as best_of_flag, count(*) as characters

from fct_episode 
inner join xref_episode_guest
using (episode_id)
inner join dim_guest
using (guest_id)

where upper(episode_title) not like 'BEST OF%'

group by all

order by release_date desc
```

<Chart data={guests_per_ep} x=release_date yMax=25>
    <Line
        y=characters
    />
    <Bar
        y=best_of_flag
    />
</Chart >

```best_ofs
select 
    best_of_year, best_of_flag, count(*) episode_count

from fct_episode 

group by all
order by best_of_year desc
```

<DataTable data="{best_ofs}" >
    <Column id="best_of_year" />
    <Column id="episode_count" />
</DataTable>