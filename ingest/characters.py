from datetime import datetime 
import json
import string
import sys

from utils import get_soup, parse_people_data

HOST = "https://comedybangbang.fandom.com/"

def get_character(href, store=False):
    if href in ['/wiki/Earwolf_interns', '/wiki/The_Washington_Monugents']:
        return None

    print(href)
    soup = get_soup(f'{HOST}{href}')

    table_tag = soup.find('table', attrs={'class':'wikia-infobox'})
    number_of_appearances = None
    played_by = []
    first_episode = None
    latest_episode = None
    for tr_tag in table_tag.find_all('tr'):
        if tr_tag.find('th') and tr_tag.find('th').get_text().strip() == 'Number of Appearances':
            number_of_appearances = tr_tag.find('td').get_text().strip()
        if tr_tag.find('th') and tr_tag.find('th').get_text().strip() == 'Played by':
            played_by = parse_people_data(tr_tag.find('td'))
        if tr_tag.find('th') and tr_tag.find('th').get_text().strip() == 'First Episode':
            first_episode = tr_tag.find('td').get_text().strip()
        if tr_tag.find('th') and tr_tag.find('th').get_text().strip() == 'Latest Episode':
            latest_episode = tr_tag.find('td').get_text().strip()

    character = {
        'href': href,
        'name': table_tag.find('tr').get_text().strip(),
        'number_of_appearances': number_of_appearances,
        'played_by': played_by,
        'first_episode': first_episode,
        'latest_episode': latest_episode
    }


    return character

def get_characters_by_last_initial(last_initial, get_details=False, store=False):
    soup = get_soup(f'{HOST}wiki/Category:Characters?from={last_initial}')

    characters = []

    for li_tag in soup.find_all('li', attrs={'class': 'category-page__member'}):
        a_tag = li_tag.find('a')

        if get_details:
            character = get_character(a_tag.get('href'), False)
        else:
            character = {
                'href': a_tag.get('href'),
                'name': a_tag.get('title')
            }

        if character:
            characters.append(character)

    if store:
        with open(f'characters_{last_initial}.json', 'w') as file:
            json.dump(characters, file)

    return characters

def get_all_characters(get_details=False, store=False):
    characters = []
    for letter in string.ascii_uppercase:
        characters += get_characters_by_last_initial(letter, get_details, False)
    
    characters += get_characters_by_last_initial('É', get_details, False)
    characters += get_characters_by_last_initial("'", get_details, False)

    if store:
        with open(f'characters.json', 'w') as file:
            json.dump(characters, file)

get_all_characters(True, True)
