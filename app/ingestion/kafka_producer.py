from datetime import time
from confluent_kafka import SerializingProducer

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed for message: {msg.key()}: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def send_message(bootstrap_servers:str, topic:str, key:str|int, value:str):
    producer = SerializingProducer({"bootstrap.servers": bootstrap_servers})
    try:
        producer.produce(
            topic=topic, 
            key=key,
            value=value,
            on_delivery=delivery_report
        )
    except BufferError:
        print(f"Local producer queue is full ({len(producer)} messages awaiting delivery): Waiting...")
        time.sleep(1)
    finally:
        producer.flush()
        producer.close()

