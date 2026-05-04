import requests
from requests import exceptions
import dotenv
import os

dotenv.load_dotenv()

def get_weather(lat, lon):
    weather_url=f'https://www.meteosource.com/api/v1/free/point?lat={lat}&lon={lon}&sections=all&timezone=UTC&language=en&units=metric&key={os.getenv("API_KEY")}'
    try:
        result = requests.get(weather_url)
        if result.ok:
            return result
        return None
    except exceptions.RequestException as e:
        print('Error getting weather data')
        return None

if __name__ == '__main__':
    latitude=55.096632
    longitude=37.155596
    print(get_weather(latitude, longitude).json())