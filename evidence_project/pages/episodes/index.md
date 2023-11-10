```episode
select *,
    date_part('year', release_date) as release_year

from fct_episode
```


```yearly_episode
select 
    release_year,
    sum(case when best_of_flag then 1 else 0 end) as best_of_episodes, 
    sum(case when not best_of_flag then 1 else 0 end) as non_best_of_episodes, 

    sum(case when special_episode then 1 else 0 end) as speicial_episodes, 
    sum(case when not special_episode then 1 else 0 end) as non_speicial_episodes, 

    sum(case when best_of_flag and special_episode then 1 else 0 end) as best_of_special_episodes, 
    sum(case when best_of_flag and not special_episode then 1 else 0 end) as best_of_non_special_episodes, 
    sum(case when not best_of_flag and special_episode then 1 else 0 end) as non_best_of_special_episodes, 
    sum(case when not best_of_flag and not special_episode then 1 else 0 end) as non_best_of_non_special_episodes, 

    count(*) as total_episodes

from ${episode}

group by 1
```

<BarChart
    data={yearly_episode}
    x=release_year
    xfmt='yyyy'
    y={[
        'best_of_special_episodes','best_of_non_special_episodes','non_best_of_special_episodes', 'non_best_of_non_special_episodes'
    ]}
/>