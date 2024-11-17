from confluent_kafka.serializing_producer import SerializingProducer
from app.ingestion.abstract_kafka_service import AbstractKafkaService

class KafkaProducerService(AbstractKafkaService):
    def __init__(self):
        self.config = {
            'bootstrap.servers': None,
            'key.serializer': str.encode('utf-8'),
            'value.serializer': self._serialize,
        }
    
    def add_bootstrap_servers(self, servers: str) -> None:
        if not self.config.get('bootstrap.servers'):
            self.config.__setitem__('bootstrap.servers', servers)
        else:
            self.config.get('bootstrap.servers').split(',').append(servers).join(',')
        self.producer = SerializingProducer(self.config)

    def __repr__(self):
        return f'KafkaProducerService(conf={self.config.get("bootstrap.servers")})'
    
    def send_message(self, topic: str, message: dict):
        self.producer.produce(topic=topic, value=self._serialize(message), on_delivery=self._delivery_report)
    
    def _delivery_report(self, err, msg):
        if err:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')
    