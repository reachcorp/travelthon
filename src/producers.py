def fill_travelthon_kafka(destination, idBio, locationCoordinates, topic, producer):
    json_togo = {
        "destination": destination,
        "idBio" : idBio,
        "locationCoordinates": locationCoordinates
    }
    producer.send(topic, value=(json_togo))