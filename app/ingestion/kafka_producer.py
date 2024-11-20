from confluent_kafka.serializing_producer import SerializingProducer
from app.ingestion.abstract_kafka_service import AbstractKafkaService

class KafkaProducerService(AbstractKafkaService):
    def __init__(self):
        self.config = self._default_config()
        self.producer = SerializingProducer(self.config)

    def _default_config(self):
        return {
            'bootstrap.servers': None,
            'key.serializer': str.encode,
            'value.serializer': self._serialize,
        }

    def send_message(self, topic: str, message: dict):
        self.producer.produce(topic=topic, value=self._serialize(message), on_delivery=self._delivery_report)
    
    def _delivery_report(self, err, msg):
        if err:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

    