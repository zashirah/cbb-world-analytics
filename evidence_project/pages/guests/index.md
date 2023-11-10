
```guests
select *,
    '/guests/' || lower_guest_href[7:] as guest_link,
from dim_guest
where guest_href != 'N/A'
order by guest_name
```

## Featured Guests

* [Lauren Lapkus](lauren_lapkus)
* [Paul F. Tompkins](paul_f._tompkins)
* [Shaun Diston](shaun_diston)
* [Ego Nwodim](ego_nwodim)

### Click the guest below to see a detailed yearly view

<DataTable data="{guests}" link=guest_link search="true">
    <Column id="guest_name" />
</DataTable>

### Guests without Wiki pages

```unregistered_guests
select *
from dim_guest
where guest_href == 'N/A'
order by guest_name
```

<DataTable data="{unregistered_guests}" search="true">
    <Column id="guest_name" />
</DataTable>