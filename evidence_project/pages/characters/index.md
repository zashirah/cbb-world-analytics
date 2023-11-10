```characters
select *,
    '/characters/' || character_href[7:] as character_link,
from dim_character
where character_href != 'N/A'
order by character_name
```

## Featured Guests

* [Sprague The Whisperer](Sprague_The_Whisperer)
* [Ho Ho the Elf](Ho_Ho_the_Elf)
* [Gino Lambardo](Gino_Lambardo)
* [Charles Barkley](Charles_Barkley)

### Click the character below to see a detailed yearly view

<DataTable data="{characters}" link=character_link search="true">
    <Column id="character_name" />
</DataTable>

### Characters without Wiki pages

```unregistered_characters
select *
from dim_character
where character_href == 'N/A'
order by character_name
```

<DataTable data="{unregistered_characters}" search="true">
    <Column id="character_name" />
</DataTable>