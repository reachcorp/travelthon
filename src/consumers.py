#!/usr/bin/env python
import logging
import threading
import json
import src.services as services
from json import dumps

from kafka import KafkaConsumer, KafkaProducer

class Consumer(threading.Thread):

    def __init__(self, kafka_endpoint, topic_in, topic_out, geotrouvethon_url_locate):
        threading.Thread.__init__(self)
        self.kafka_endpoint=kafka_endpoint
        self.topic_in=topic_in
        self.topic_out=topic_out
        self.geotrouvethon_url_locate=geotrouvethon_url_locate


    def run(self):
        logging.info("Lancement du thread pour depiler file kafka "+self.topic_in)
        consumer = KafkaConsumer(bootstrap_servers=self.kafka_endpoint,
                                 value_deserializer=lambda x: json.loads(x.decode('utf-8')),
                                 auto_offset_reset='latest')

        producer = KafkaProducer(bootstrap_servers=[self.kafka_endpoint], value_serializer=lambda v: json.dumps(v).encode('utf-8'))

        consumer.subscribe([self.topic_in])

        for message in consumer:
                logging.info("Nouveau message du topic ["+str(self.topic_in)+"]")
                #recuperation des donneés du json
                data = message.value
                destination = data['destination']
                idBio=data['idBio']
                #recupération des coordonnee de la destination en appellant service rest de geotrouvethon
                locationCoordinates=services.getCoordFromLocation(destination, self.geotrouvethon_url_locate)
                logging.info(destination + " " +locationCoordinates)
                #envoi du tout dans la file kafka self.topic_out
                self.fill_kafka_out(idBio,destination,locationCoordinates, producer)

        consumer.close()

    def fill_kafka_out(self, idBio, destination, locationCoordinates, producer):
        json_togo = {
            "idBio" : idBio,
            "locationName": destination,
            "locationCoordinates": locationCoordinates
        }
        producer.send(self.topic_out, value=(json_togo))