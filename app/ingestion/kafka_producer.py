import json
from kafka import KafkaProducer

class KafkaProducerService: 
    def __init__(self, bootstrap_servers: str) -> None:
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def send_message(self, topic: str, message: dict) -> None:
        self.producer.send(topic, value=message)
        self.producer.flush()