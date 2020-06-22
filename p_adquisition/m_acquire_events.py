from bs4 import BeautifulSoup
import requests


def obtain_links(url: str):
    print(f"Obtaining links from events")
    event = paged_url(url)
    links_bs = BeautifulSoup(str(event), 'lxml')
    links = [a['href'] for a in links_bs.find_all('a', href=True)]

    return links


def paged_url(url: str):
    path_all_pages = [url, ]
    html = ""
    for i in range(2, 11):
        path_all_pages.append(f'{url}?page={i}')
    for i in path_all_pages:
        print(f'Obtaining event {i}')
        html = html + ' ' + str(requests.get(i).content)

    soup = BeautifulSoup(html, 'lxml')
    events = set(soup.find_all('aside', {'class': 'eds-event-card-content__image-container'}))
    events = list(events)
    return events
