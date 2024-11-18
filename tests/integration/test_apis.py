import requests

def test_get_forcast_endpoint():
    test_data = {
        'latitude': 52.52,
        'longitude': 13.41,
        'hourly': 'temperature_2m', 
    }
    parsed_url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly={}".format(str(test_data['latitude']), str(test_data['longitude']), test_data['hourly'])
    response = requests.get(parsed_url)
    
    assert parsed_url == """https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"""
    assert response.status_code == 200
    # assert response.json().get('latitude') == test_data['latitude']
    # assert response.json().get('longitude') == test_data['longitude']
    # assert response.json().get('current_weather') == test_data['current_weather']