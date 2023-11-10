
```guests
select *,
    '/guests/' || guest_href[7:] as guest_link,
from dim_guest
where guest_href != 'N/A'
order by guest_name
```

## Featured Guests

* [Lauren Lapkus](Lauren_Lapkus)
* [Paul F. Tompkins](Paul_F._Tompkins)
* [Shaun Diston](Shaun_Diston)
* [Ego Nwodim](Ego_Nwodim)

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