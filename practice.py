import requests

api_key = 'bfeb41b4-3d37-46cb-aa40-b4add98e32c8'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)