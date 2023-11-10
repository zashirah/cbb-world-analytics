{% set loops = [1,2,3,4] %}

with unioned as (

{% for num in loops %}
    select 
        played_by[{{ num }}].href as played_by_href,
        played_by[{{ num }}].name as played_by_name,
        character_id,
        character_name

    from {{ ref('stg_characters') }}
    
    {%- if not loop.last %} union {% endif -%}
{% endfor %}
)

select 
    {{ dbt_utils.generate_surrogate_key(['played_by_href']) }} as guest_id,
    played_by_name as guest_name,
    character_id,
    *

from unioned 

