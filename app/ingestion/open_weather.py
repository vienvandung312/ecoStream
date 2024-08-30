import os
import requests
from dotenv import load_dotenv
from app.constants import WorkingPath

load_dotenv(dotenv_path=WorkingPath.ROOT.value.joinpath('env/.env'))
OPEN_WEATHER_API_KEY = os.getenv('OPEN_WEATHER_API_KEY')
OPEN_WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/{endpoint}?lat={lat}&lon={lon}&appid={api_key}"
GEOCODING_API_URL = "https://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}"

def get_geocoding_by_name(city_name: str) -> dict:
    response = requests.get(f"{GEOCODING_API_URL.format(city_name=city_name, api_key=OPEN_WEATHER_API_KEY)}")
    return response.json()

def get_weather_by_coordinates(lat: float, lon: float) -> list[dict]:
    response = requests.get(f"{OPEN_WEATHER_API_URL.format(endpoint='weather', lat=lat, lon=lon, api_key=OPEN_WEATHER_API_KEY)}")
    return response.json()
