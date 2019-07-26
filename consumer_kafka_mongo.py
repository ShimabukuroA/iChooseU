from kafka import KafkaConsumer
import json
import pymongo
from json import loads, dumps

consumer = KafkaConsumer(
    'pokemon',
    bootstrap_servers=['localhost:29092'],
    enable_auto_commit=True,
    auto_commit_interval_ms=5000,
    value_deserializer=lambda x: loads(x.decode('utf-8')),
    auto_offset_reset='earliest')

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pokemons"]
mycollect = mydb["pokemon"]

for msg in consumer:
    pokemon_name = msg.value['forms'][0]['name']
    print(pokemon_name)
    mycollect.insert_one(msg.value)
    print('Inserted into MongoDB!')
