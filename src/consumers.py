#!/usr/bin/env python

import multiprocessing
import json
import src.services as services
from json import dumps

from kafka import KafkaConsumer, KafkaProducer

class Consumer(multiprocessing.Process):

    def __init__(self, kafka_endpoint, topic_in, topic_out, geotrouvethon_url_locate):
        multiprocessing.Process.__init__(self)
        self.stop_event = multiprocessing.Event()
        self.kafka_endpoint=kafka_endpoint
        self.topic_in=topic_in
        self.topic_out=topic_out
        self.geotrouvethon_url_locate=geotrouvethon_url_locate


    def stop(self):
        self.stop_event.set()

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=self.kafka_endpoint,
                                 auto_offset_reset='latest',
                                 consumer_timeout_ms=1000)
        producer=KafkaProducer(bootstrap_servers=[self.kafka_endpoint], value_serializer=lambda x: dumps(x).encode('utf-8'))

        consumer.subscribe([self.topic_in])

        while not self.stop_event.is_set():
            for message in consumer:
                #decodage du message en byte to string
                msg = message.value.decode('utf8').replace("'", '"')
                #recuperation des donneés du json
                data = json.loads(msg)
                destination = data['destination']
                idBio=data['idBio']
                if self.stop_event.is_set():
                    break
                #recupération des coordonnee de la destination en appellant service rest de geotrouvethon
                locationCoordinates=services.getCoordFromLocation(destination, self.geotrouvethon_url_locate)
                print(destination + " " +locationCoordinates)
                #envoi du tout dans la file kafka self.topic_out
                self.fill_kafka_out(idBio,destination,locationCoordinates, producer)

        consumer.close()

    def fill_kafka_out(self, idBio, destination, locationCoordinates, producer):
        json_togo = {
            "destination": destination,
            "idBio" : idBio,
            "locationCoordinates": locationCoordinates
        }
        producer.send(self.topic_out, value=(json_togo))