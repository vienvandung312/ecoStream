import requests 

class OpenMeteoAPI:
    def __init__(self):
        self.url  = 'https://api.open-meteo.com'
        self.version = 'v1'

    def _set_latitute(self, latitude: float):
        self.latitude = latitude

    def _set_longitude(self, longitude: float):
        self.longitude = longitude

    def _set_city(self, city: str):
        latitude, longitude = self._city_to_coordinates(city)
        self._set_latitute(latitude)
        self._set_longitude(longitude)
        self.city = city

    def _city_to_coordinates(self, city: str):
        geocode_url = f"https://geocoding-api.open-meteo.com/{self.version}/search?name={city}&count=1&language=en&format=json"
        response = requests.get(geocode_url).json()
        return response['results'][0]['latitude'], response['results'][0]['longitude']

    def get_weather_by_country(self, city: str):
        self._set_city(city)
        response = requests.get(f"{self.url}/{self.version}/forecast?latitude={self.latitude}&longitude={self.longitude}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,weather_code,wind_speed_10m,wind_direction_10m,wind_gusts_10m&hourly=apparent_temperature,precipitation_probability,weather_code,uv_index&models=best_match").json()
        return response
    
    


    


