import pandas as pd
import requests
from bs4 import BeautifulSoup

def event_info(url: str):
    print(f"Obtaining info from event {url}")

    ### Storing links from url ###
    links = obtain_links(url)
    html_from_links = []
    for i in links:
        html_from_links.append(requests.get(i).content)
        print(f"obtaining html from link: {links.index[i]} / {len(links)}")
    ### Scraping titles from links ###
    soup = []
    for a in html_from_links:
        soup.append(BeautifulSoup(a, 'lxml'))
        print(f'souping element {html_from_links.index(a)} / {len(html_from_links)}')

    title = [(a.find_all('h1', {'data-automation': 'listing-title'})) for a in soup]

    hackaton_titles = []
    for a in title:
        string = re.findall(r'\>(.*?)\<', str(a))
        hackaton_titles.append(string)




def info_to_df(url: str):
    links_df = pd.DataFrame(info, columns=['link'])
    links_df.to_csv('/home/david/Documents/scraping_project/data/links.csv')

    return links_df
