{#
    {% call statement('get_loops', fetch_result=True) %}
        SELECT max(len(guests)) FROM {{ ref('stg_episodes') }}
    {% endcall %}

    {% set loops = load_result('get_loops')['data'][0][0] %}
#}

{% set loops = [1,2] %}

with unioned as (

{% for num in loops %}
    select 
        hosts[{{ num }}].href as host_href,
        hosts[{{ num }}].name as host_name,
        episode_href,
        episode_title

    from {{ ref('stg_episodes') }}
    
    {%- if not loop.last %} union {% endif -%}
{% endfor %}
)

select 
    {{ dbt_utils.generate_surrogate_key(['host_href', 'host_name']) }} as host_id,
    {{ dbt_utils.generate_surrogate_key(['episode_href']) }} as episode_id,
    *

from unioned 

