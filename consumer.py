from kafka import KafkaConsumer
import json
from json import loads, dumps

consumer = KafkaConsumer(
    'pokemon',
    bootstrap_servers=['localhost:29092'],
    enable_auto_commit=True,
    auto_commit_interval_ms=5000,
    value_deserializer=lambda x: loads(x.decode('utf-8')),
    auto_offset_reset='earliest')

for msg in consumer:
    message = msg.value
    print(message['forms'][0]['name'])
