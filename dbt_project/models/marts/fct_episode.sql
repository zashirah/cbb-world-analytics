select 
    episodes.episode_id,
    episodes.episode_title,
    episodes.episode_href,
    episodes.episode_number,
    episodes.release_date,
    case when best_ofs.episode_id is not null then True else False end as best_of_flag,
    best_ofs.best_of_year

from {{ ref('stg_episodes') }} as episodes
left join {{ ref('stg_best_ofs') }} as best_ofs
using (episode_id)