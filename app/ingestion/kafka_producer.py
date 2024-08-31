from kafka import KafkaProducer

def send_message(bootstrap_servers:str, topic:str, message:str):
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    producer.send(topic, message.encode('utf-8'))
    producer.flush()
    producer.close()
