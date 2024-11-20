from confluent_kafka.deserializing_consumer import DeserializingConsumer
from confluent_kafka.serialization import StringDeserializer
from app.ingestion.abstract_kafka_service import AbstractKafkaService


class KafkaConsumerService(AbstractKafkaService):
    def __init__(self):
        self.config = self._default_config()
        self.topics_list = []
        self.consumer = self._create_consumer()

    def _create_consumer(self):
        return DeserializingConsumer(self.config)        

    def _default_config(self):
        return {
            'bootstrap.servers': None,
            'key.deserializer': StringDeserializer('utf_8'),
            'value.deserializer': self._deserialize,
            'group.id': 'default_group',
            'auto.offset.reset': 'earliest'
        }

    def subscribe(self, topics: list):
        self.topics_list.extend(topics) 
        self.consumer.subscribe(topics)

    def unsubscribe(self, topics: list):
        self.topics_list = [topic for topic in self.topics_list if topic not in topics]
        self.consumer.unsubscribe(topics)

    def consume_streams(self):
        while True:
            message = self.consumer.poll(timeout=1.0)
            if message is None:
                continue

            if message.error():
                print(f'Consumer error: {message.error()}')
                continue

            print(f'Consumed message: {message.value()}')
            self.consumer.commit(message)
    
    def _delivery_report(self, err, msg):
        if err:
            print(f'Message consumption failed: {err}')
        else:
            print(f'Message consumed: {msg.topic()} [{msg.partition()}]')
