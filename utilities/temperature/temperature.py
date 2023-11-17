from requests import get
import pprint


def weather():
    API_KEY = "0ee948d27afb44736e21a838accd3097"

    city_name = input("City Name: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = get(url)
    data = response.json()
    temperature = data['main']['temp']
    fells_like = data['main']['feels_like']
    
    print(f"Temperature: {temperature:.0f}°C")
    print(f"Feels like: {fells_like:.0f}°C")
