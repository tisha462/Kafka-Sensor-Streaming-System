<<<<<<< HEAD
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'telemetry-data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Consumer started... waiting for new data")

for message in consumer:
=======
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'telemetry-data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Consumer started... waiting for new data")

for message in consumer:
>>>>>>> 8056a248fb2a042861590c580c33b6b84135000a
    print("Received:", message.value)