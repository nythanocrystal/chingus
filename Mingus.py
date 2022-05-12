#Welcome to life
import requests
cats = []
request = requests.get('https://catfact.ninja/fact').json()
cats.append(request['fact'])
for i in range(4):
    request = requests.get('https://catfact.ninja/fact').json()
    if request['fact'] in cats:
        continue
    else:
        cats.append(request['fact'])

print(cats)