import pytest
from app.ingestion.kafka_producer import KafkaProducerService

def test_serialize_message_with_normal_input():
    service = KafkaProducerService()
    service.add_bootstrap_servers('localhost:9092')
    message = {'key': 'value'}
    serialized_message = service._serialize(message)
    assert serialized_message == b'{"key": "value"}'

def test_serialize_message_with_empty_input():
    service = KafkaProducerService()
    service.add_bootstrap_servers('localhost:9092')
    message = {}
    with pytest.raises(Exception):
        service._serialize(message)

    message = None 
    with pytest.raises(Exception):
        service._serialize(message)

def test_add_bootstrap_servers():
    service = KafkaProducerService()
    service.add_bootstrap_servers('localhost:9092')
    assert service.config.get('bootstrap.servers') == 'localhost:9092'

    service.add_bootstrap_servers('localhost:9093')
    assert service.config.get('bootstrap.servers') == 'localhost:9092,localhost:9093'

def test_add_bootstrap_servers_with_multiple_servers():
    service = KafkaProducerService()
    service.add_bootstrap_servers('localhost:9092')
    service.add_bootstrap_servers('localhost:9093, localhost:9094, localhost:9095')
    assert service.config.get('bootstrap.servers') == 'localhost:9092,localhost:9093,localhost:9094,localhost:9095'


    service = KafkaProducerService()
    service.add_bootstrap_servers('localhost:9092, localhost:9093, localhost:9094')
    assert service.config.get('bootstrap.servers') == 'localhost:9092,localhost:9093,localhost:9094'

def test_deserialize_message_with_normal_input():
    service = KafkaProducerService()
    service.add_bootstrap_servers('localhost:9092')
    message = {'key': 'value'}
    serialized_message = service._serialize(message)
    deserialized_message = service._deserialize(serialized_message)
    assert deserialized_message == message

def test_deserialize_message_with_empty_input():
    service = KafkaProducerService()
    service.add_bootstrap_servers('localhost:9092')
    message = b''
    with pytest.raises(Exception):
        service._deserialize(message)
    
    message = None
    with pytest.raises(Exception):
        service._deserialize(message)

def test_repr():
    service = KafkaProducerService()
    service.add_bootstrap_servers('localhost:9092')
    assert service.__repr__() == 'KafkaProducerService(conf=localhost:9092)'
