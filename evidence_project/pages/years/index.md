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
