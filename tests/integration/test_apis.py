from app.ingestion.open_meteo_api import OpenMeteoAPI


class TestOpenMeteoAPI():
    def test_city_to_coordinates(self):
        api = OpenMeteoAPI()
        latitude, longitude = api._city_to_coordinates('Berlin')
        
        assert latitude == 52.52437
        assert longitude == 13.41053

    def test_get_weather_by_country(self):
        api = OpenMeteoAPI()
        response = api.get_weather_by_country('Berlin')
        
        assert 'current' in response
        assert 'hourly' in response

         