import pytest
from app.ingestion.kafka_producer import KafkaProducerService
from app.ingestion.kafka_consumer import KafkaConsumerService
class TestKafkaProducerService:
    def test_serialize_message_with_normal_input(self):
        service = KafkaProducerService()
        service.add_brokers('localhost:9092')
        message = {'key': 'value'}
        serialized_message = service._serialize(message)
        assert serialized_message == b'{"key": "value"}'

    def test_serialize_message_with_empty_input(self):
        service = KafkaProducerService()
        service.add_brokers('localhost:9092')
        message = {}
        with pytest.raises(Exception):
            service._serialize(message)

        message = None 
        with pytest.raises(Exception):
            service._serialize(message)

    def test_add_brokers(self):
        service = KafkaProducerService()
        service.add_brokers('localhost:9092')
        assert service.config.get('bootstrap.servers') == 'localhost:9092'

        service.add_brokers('localhost:9093')
        assert service.config.get('bootstrap.servers') == 'localhost:9092,localhost:9093'

    def test_add_brokers_with_multiple_servers(self):
        service = KafkaProducerService()
        service.add_brokers('localhost:9092')
        service.add_brokers('localhost:9093, localhost:9094, localhost:9095')
        assert service.config.get('bootstrap.servers') == 'localhost:9092,localhost:9093,localhost:9094,localhost:9095'


        service = KafkaProducerService()
        service.add_brokers('localhost:9092, localhost:9093, localhost:9094')
        assert service.config.get('bootstrap.servers') == 'localhost:9092,localhost:9093,localhost:9094'

    def test_deserialize_message_with_normal_input(self):
        service = KafkaProducerService()
        service.add_brokers('localhost:9092')
        message = {'key': 'value'}
        serialized_message = service._serialize(message)
        deserialized_message = service._deserialize(serialized_message)
        assert deserialized_message == message

    def test_deserialize_message_with_empty_input(self):
        service = KafkaProducerService()
        service.add_brokers('localhost:9092')
        message = b''
        with pytest.raises(Exception):
            service._deserialize(message)
        
        message = None
        with pytest.raises(Exception):
            service._deserialize(message)

    def test_repr_on_implementation(self):
        service = KafkaProducerService()
        service.add_brokers('localhost:9092')
        assert service.__repr__() == 'KafkaProducerService(conf=localhost:9092)'

        service = KafkaConsumerService()
        service.add_brokers('localhost:9092')
        assert service.__repr__() == 'KafkaConsumerService(conf=localhost:9092)'