import requests
from bs4 import BeautifulSoup
import re

soup_pages = []
# name, surname = input().split()
name, surname = 'александр чумилин'.split()
for i in range(3):
    url = f'https://yandex.ru/search/?text="{name}"+"{surname}"&lr=101718&clid=2285101&p={i}'
    resp = requests.get(url)
    soup_page = BeautifulSoup(resp.text, 'html.parser')
    soup_pages.append(soup_page)

links = []
for soup_page in soup_pages:
    for a in soup_page.find_all('a'):
        print(a['href'])
        if 'href' in a.attrs and 'google' not in a['href'] and 'yandex' not in a['href'] and 'search' not in a[
            'href'] and a['href'] not in links:
            links.append(a['href'])

print(links)
