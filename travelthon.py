import logging
import os
import threading
from flask import Flask
from flask import request
from json import dumps
from json import loads
from kafka import KafkaConsumer
from kafka import KafkaProducer

app = Flask(__name__)

travelthon_in=os.environ['TRAVELTHON_IN']
travelthon_out = os.environ["TRAVELTHON_OUT"]

kafka_endpoint = str(os.environ["KAFKA_IP"]) + ":" + str(os.environ["KAFKA_PORT"])
producer = KafkaProducer(bootstrap_servers=[kafka_endpoint], value_serializer=lambda x: dumps(x).encode('utf-8'))


def start_travelthon_consummer():
    consumer = KafkaConsumer(
        travelthon_in,
        bootstrap_servers=[kafka_endpoint],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8'))
    )
    logging.info('Kafka Consumer for travelthon started')
    for msg in consumer:
        logging.debug('Consume message from ##travelthon_out')
        topic_json = msg.value
        bio_id = topic_json['idBio']
        location_json = topic_json['location']
        #appel a geotrouvethon http://127.0.0.1:9966/locate/<place>

if __name__ == '__main__':
    app.run()

