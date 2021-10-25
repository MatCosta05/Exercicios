from requests import get
from bs4 import BeautifulSoup
import re

site = get("https://pt.wikipedia.org/wiki/League_of_Legends")
tags = BeautifulSoup(site.text, "html5lib")

title = tags.find("title")
title

print("Página Principal:", title.text)

todos_links = tags.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile("(/wiki/)+([A-Za-z0-9_:()])+"))

for link in todos_links:
    print("Titulo:", link.get('title'), "||| Link:", link.get('href'))
