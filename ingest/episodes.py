from datetime import datetime 
import json
import sys

from utils import get_soup, parse_people_data

HOST = "https://comedybangbang.fandom.com/"

def get_episodes(soup):
    episodes_raw = soup.find_all('div', attrs = {'class':'wikia-gallery-item'}) 

    print(len(episodes_raw))

    return episodes_raw

def parse_dates(raw_date):
    raw_date = raw_date.strip().translate({ord(i): None for i in ',.'})
    output_date = datetime.strptime(raw_date, '%B %d %Y').strftime('%Y-%m-%d')

    return output_date

def get_episode_href(episode_html):
    href = episode_raw.find(
        'div', attrs = {'class': 'lightbox-caption'}
    ).find('a').get('href')

def get_episode(href, store=False):
    episode_soup = get_soup(F'{HOST}{href}')
    print(href)

    table = episode_soup.find('table', attrs = {'class':'wikia-infobox'})

    table_rows = table.find_all('tr')
    table_len = len(table_rows)

    release_date = table_rows[table_len - 8].find('td').get_text().strip().translate({ord(i): None for i in ',.'})
    duckdb_date = datetime.strptime(release_date, '%B %d %Y').strftime('%Y-%m-%d')

    episode = {
        'title': table_rows[0].get_text().strip(),
        'episode_href': href,
        'episode_number': table_rows[table_len - 10].get_text().strip(),
        'release_date': duckdb_date,
        'hosted_by': parse_people_data(table_rows[table_len - 7]),
        'guests': parse_people_data(table_rows[table_len - 6]),
        'characters': parse_people_data(table_rows[table_len - 5])
    }

    if store:
        with open(f'{episode["title"]}.json', 'w') as file:
            json.dump(episode, file)

    return episode

def create_episodes_list(episodes_raw):
    episodes = []
    for episode_raw in episodes_raw:
        href = get_episode_href(episode_html)
        episode = get_episode(href)

        episodes.append(episode)

    return episodes

def get_special_eps(get_details=False, store=False):
    soup = get_soup(f'{HOST}wiki/Category:Special_Episodes')

    episodes = []

    for table_tag in soup.find_all('div', attrs={'class': 'category-page__members'}):
        for a_tag in table_tag.find_all('a'):
            # skipping /wiki/2013_Tour,_San_Francisco b/c there is a error in the date
            if a_tag.get('href') in [
                '/wiki/Category:Live_Episodes', '/wiki/2013_Tour,_San_Francisco', 
                '/wiki/Category:B-b-b-b-bonus-s-s-s-s!', '/wiki/Category:Video_Episodes']:
                continue
            if get_details:
                episode = get_episode(a_tag.get('href'))
            else:
                episode = {
                    'href': a_tag.get('href')
                }

            episodes.append(episode)

            print(episode)
            print('----')
        
    if store:
        with open('special_eps.json', 'w') as file:
            json.dump(episodes, file)

    # print(episodes)

    return episodes


def get_best_ofs(store=False):
    soup = get_soup(f'{HOST}wiki/Category:Best_Of')

    episodes = []

    for table_tag in soup.find_all('table', attrs={'class': 'article-table'}):
        year = table_tag.find('caption').get_text()
        for a_tag in table_tag.find_all('a'):
            episode = {
                'best_of_year': year.strip(),
                'href': a_tag.get('href')
            }
            episodes.append(episode)

            print(episode)
        
    if store:
        with open('best_ofs.json', 'w') as file:
            json.dump(episodes, file)

    # print(episodes)

    return episodes

def backfill_all_episodes(store=False):
    soup = get_soup(f"{HOST}wiki/Category:Episodes")

    episodes_raw = get_episodes(soup)

    episodes = create_episodes_list(episodes_raw)

    if store:
        with open('cbb_episodes.json', 'w') as file:
            json.dump(episodes, file)

if __name__ == '__main__':
    get_special_eps(True, True)