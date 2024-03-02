import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("\n*** Get Current Weahter conditions ***\n")

    city = input("\nPlease enter a city name:\n")

    requests_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    #print(requests_url)
    weather_data = requests.get(requests_url).json()
    pprint(weather_data)

    print(f'\nCurrent weather for {weather_data["name"]}')
    print(f'\nThe temp is {weather_data["main"]["temp"]}')
    print(f'Fees like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"].capitalize()}')

if __name__ == "__main__":
    get_current_weather()