import requests
import json
from pprint import pprint
target = ['Hulk', 'Captain America', 'Thanos']
url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
content = response.json()
hero_dict = {}
for index in content:
    if index['name'] in target:
        name = index['name']
        hero_dict[name] = index['powerstats']['intelligence']
new_dict = list(sorted(hero_dict.items(), key=lambda item: item[1]))
print(f"{new_dict[-1][0]} has the most intelligence of {new_dict[-1][1]} units")