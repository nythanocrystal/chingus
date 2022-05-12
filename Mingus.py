#Welcome to life
import requests


for i in range(5):
    request = requests.get('https://catfact.ninja/fact').json()
    print(request['fact'])