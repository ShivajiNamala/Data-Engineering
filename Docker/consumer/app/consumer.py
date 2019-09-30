import os
import json
import time
import pymongo  
from kafka import KafkaConsumer
from pymongo import MongoClient 

kafka_topic = "topic1"

if __name__ == '__main__':
    
    client = MongoClient("mongodb://192.168.99.100:27017")
    db = client.dbtwitter
    
    time.sleep(10)   # wait until Kafka is running
    kafka_service = os.environ['KAFKA_SERVICE']
    print("Consumer is using kafka service {0}".format(kafka_service))

    consumer = KafkaConsumer(bootstrap_servers=[kafka_service],api_version=(0, 10))
    consumer.subscribe(kafka_topic)
    for msg in consumer:
        result = db.tbcanada.insert_one(json.loads(msg.value.decode("utf-8")))
        #print (msg.value.decode("utf-8"))
