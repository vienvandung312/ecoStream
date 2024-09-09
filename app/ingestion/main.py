from app.ingestion import open_weather, kafka_producer

if __name__ == "__main__":
    geocoding = open_weather.get_geocoding_by_name("Ha Noi")[0]
    weather_data = open_weather.get_weather_by_coordinates(lat=geocoding['lat'], lon=geocoding['lon'])

    kafka_producer.send_message(
        bootstrap_servers="localhost:9092",
        topic="open_weather",
        key=str(weather_data['id']),
        value=str(weather_data)
    )
