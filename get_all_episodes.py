from bs4 import BeautifulSoup 
import json
import requests 

HOST = "https://comedybangbang.fandom.com/"
  

def get_soup(url):
    r = requests.get(url) 
    soup = BeautifulSoup(r.content, 'html5lib')

    return soup

def get_episodes(soup):
    episodes_raw = soup.find_all('div', attrs = {'class':'wikia-gallery-item'}) 

    print(len(episodes_raw))

    return episodes_raw

def parse_people_data(raw_list):
    people = []
    
    for a_tag in raw_list.find_all('a'):

        people.append({
            'name': a_tag.get_text(),
            'href': a_tag.get('href')
        })

    for span_tag in raw_list.find_all('span'):
        people.append({
            'name': span_tag.get_text(),
            'href': 'N/A'
        })

    return people


def get_episode(episode_raw):
    href = episode_raw.find(
            'div', attrs = {'class': 'lightbox-caption'}
        ).find('a').get('href')

    episode_soup = get_soup(F'{HOST}{href}')


    table = episode_soup.find('table', attrs = {'class':'wikia-infobox'})

    table_rows = table.find_all('tr')
    table_len = len(table_rows)

    episode = {
        'title': table_rows[0].get_text().strip(),
        'episode_href': href,
        'episode_number': table_rows[table_len - 10].get_text().strip(),
        'release_date': table_rows[table_len - 8].find('td').get_text().strip(),
        'hosted_by': parse_people_data(table_rows[table_len - 7]),
        'guests': parse_people_data(table_rows[table_len - 6]),
        'characters': parse_people_data(table_rows[table_len - 5])
    }


    return episode


def create_episodes_list(episodes_raw):
    episodes = []
    for episode_raw in episodes_raw:
        episode = get_episode(episode_raw)

        episodes.append(episode)

    return episodes


def main():
    soup = get_soup(f"{HOST}wiki/Category:Episodes")

    episodes_raw = get_episodes(soup)

    episodes = create_episodes_list(episodes_raw)

    with open('cbb_episodes.jsonl', 'w') as file:
        json.dump(episodes, file)

    
main()