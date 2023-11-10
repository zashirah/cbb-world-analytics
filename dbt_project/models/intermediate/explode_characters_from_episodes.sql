{#
    {% call statement('get_loops', fetch_result=True) %}
        SELECT max(len(guests)) FROM {{ ref('stg_episodes') }}
    {% endcall %}

    {% set loops = load_result('get_loops')['data'][0][0] %}
#}

{% set loops = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23] %}

with unioned as (

{% for num in loops %}
    select 
        characters[{{ num }}].href as character_href,
        characters[{{ num }}].name as character_name,
        episode_href

    from {{ ref('stg_episodes') }}
    
    {%- if not loop.last %} union {% endif -%}
{% endfor %}
)

select 
    {{ dbt_utils.generate_surrogate_key(['character_href']) }} as character_id,
    {{ dbt_utils.generate_surrogate_key(['episode_href']) }} as episode_id,
    *

from unioned 

