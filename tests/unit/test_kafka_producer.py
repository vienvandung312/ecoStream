import pytest
from app.ingestion.kafka_producer import KafkaProducerService

def test_serialize_message_with_normal_input():
    service = KafkaProducerService('localhost:9092')
    message = {'key': 'value'}
    serialized_message = service._serialize(message)
    assert serialized_message == b'{"key": "value"}'

def test_serialize_message_with_empty_input():
    service = KafkaProducerService('localhost:9092')
    message = {}
    with pytest.raises(Exception):
        service._serialize(message)

    message = None 
    with pytest.raises(Exception):
        service._serialize(message)
