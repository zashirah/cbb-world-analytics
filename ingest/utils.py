from bs4 import BeautifulSoup 
import requests 

def get_soup(url):
    r = requests.get(url) 
    soup = BeautifulSoup(r.content, 'html5lib')

    return soup

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

def parse_dates(raw_date):
    raw_date = raw_date.strip().translate({ord(i): None for i in ',.'})
    output_date = datetime.strptime(raw_date, '%B %d %Y').strftime('%Y-%m-%d')

    return output_date