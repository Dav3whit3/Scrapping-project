import pandas as pd
import requests
from bs4 import BeautifulSoup
from p_adquisition import m_acquire_events
import re

def get_html_from_links_of_events(url: str): #Applying REQUESTS
    print(f"Obtaining info from event {url}")

    links = m_acquire_events.obtain_links(url)
    html_from_links = []
    for i in links:
        html_from_links.append(requests.get(i).content)
        print(f"obtaining html from link: {links.index(i)} / {len(links)}")

    return html_from_links


def get_info_from_html_of_events(url: str): #Applying BeautifulSoup4
    html_from_links = get_html_from_links_of_events(url)
    soup = []
    for a in html_from_links:
        soup.append(BeautifulSoup(a, 'lxml'))
        print(f'souping element {html_from_links.index(a)} / {len(html_from_links)}')
    return soup

def get_events_name(url: str):
    soup = get_info_from_html_of_events(url)
    title = [(a.find_all('h1', {'data-automation': 'listing-title'})) for a in soup]
    hackaton_titles = []
    for a in title:
        string = re.findall(r'\>(.*?)\<', str(a))
        hackaton_titles.append(string)

    return hackaton_titles


def info_to_df(url: str):


