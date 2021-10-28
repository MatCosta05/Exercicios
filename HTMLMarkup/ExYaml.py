from requests import get
from bs4 import BeautifulSoup
from re import findall
from json import dump

link = get("https://www.w3schools.io/file/yaml-sample-example/")
tags = BeautifulSoup(link.text, "html5lib")

contyml = tags.find_all('code', attrs={'class': 'language-Yaml'})
print(contyml)

tcoments = findall(r"\W# (.+)[</]\W", str(contyml))
print(tcoments)

with open("novo_yaml.yml", "w") as file:
    dump(tcoments, file)