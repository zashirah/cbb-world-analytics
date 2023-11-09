from datetime import datetime 
import json
import string
import sys

from utils import get_soup, parse_people_data

HOST = "https://comedybangbang.fandom.com/"

def get_guest(href, store=False):
    if 'Category' in href:
        return None
    print(href)
    soup = get_soup(f'{HOST}{href}')

    table_tag = soup.find('table', attrs={'class':'wikia-infobox'})
    characters = []
    number_of_appearances = None
    first_episode = None
    latest_episode = None
    for tr_tag in table_tag.find_all('tr'):
        if tr_tag.find('th') and tr_tag.find('th').get_text().strip() == 'Characters':
            characters = parse_people_data(tr_tag.find('td'))
        if tr_tag.find('th') and tr_tag.find('th').get_text().strip() == 'Number of Appearances':
            number_of_appearances = tr_tag.find('td').get_text().strip()
        if tr_tag.find('th') and tr_tag.find('th').get_text().strip() == 'First Episode':
            first_episode = tr_tag.find('td').get_text().strip()
        if tr_tag.find('th') and tr_tag.find('th').get_text().strip() == 'Latest Episode':
            latest_episode = tr_tag.find('td').get_text().strip()

    guest = {
        'href': href,
        'name': table_tag.find('tr').get_text().strip(),
        'number_of_appearances': number_of_appearances,
        'characters': characters,
        'first_episode': first_episode,
        'latest_episode': latest_episode,
    }

    if store:
        with open(f'{href}.json', 'w') as file:
            json.dump(guest, file)

    return guest

def get_guests_by_last_initial(last_initial, get_details=False, store=False):
    soup = get_soup(f'{HOST}wiki/Category:Guests?from={last_initial}')

    guests = []

    for li_tag in soup.find_all('li', attrs={'class': 'category-page__member'}):
        a_tag = li_tag.find('a')

        if get_details:
            guest = get_guest(a_tag.get('href'), False)
        else:
            guest = {
                'href': a_tag.get('href'),
                'name': a_tag.get('title')
            }

        if guest:
            guests.append(guest)

    if store:
        with open(f'guests_{last_initial}.json', 'w') as file:
            json.dump(guests, file)

    return guests

def get_all_guests(get_details=False, store=False):
    guests = []
    for letter in string.ascii_uppercase:
        guests += get_guests_by_last_initial(letter, get_details, False)

    if store:
        with open(f'guests.json', 'w') as file:
            json.dump(guests, file)

get_all_guests(True, True)
# get_guests_by_last_initial('M', True)