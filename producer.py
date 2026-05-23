from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='127.0.0.1:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:

    data = {
        "sensor_id": "sensor_1",
        "temperature": random.randint(20, 40)
    }

    producer.send('telemetry-data', value=data)

    producer.flush()

    print("Sent:", data)

    time.sleep(2)