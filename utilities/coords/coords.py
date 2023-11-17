import requests


def CWD():
    API_KEY = "0ee948d27afb44736e21a838accd3097"

    city_name = input('City name: ')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    coord = data['coord']

    print(coord)
