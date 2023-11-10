```characters
select *,
    '/characters/' || lower_character_href[7:] as character_link,
from dim_character
where character_href != 'N/A'
order by character_name
```

## Featured Guests

* [Sprague The Whisperer](sprague_the_whisperer)
* [Ho Ho the Elf](ho_ho_the_elf)
* [Gino Lambardo](gino_lombardo)
* [Charles Barkley](charles_barkley)

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