from requests import get
from bs4 import BeautifulSoup

resposta = get("https://www.python.org/jobs/")
tags = BeautifulSoup(resposta.text, "html5lib")

title = tags.find("title")
# print(title, title.text)

'''
subtitles1 = tags.find_all("h2")
print([h2.text for h2 in subtitles1])
'''

subtitles = tags.find_all("h2", attrs={"class": "listing-company"})
print([h2.a.text for h2 in subtitles])

para_visit = ["https://www.python.org/" + h2.a["href"] for h2 in subtitles]
sites = []

for pv in para_visit:
    acesso = get(pv)
    sites.append(acesso)

print(para_visit)