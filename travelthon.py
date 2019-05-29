
import os
import logging
import src.consumers as consumers


topic_in=os.environ['TOPIC_IN']
topic_out = os.environ["TOPIC_OUT"]
geotrouvethon_url_locate="http://"+str(os.environ['GEOTROUVETHON_IP'])+":"+str(os.environ['GEOTROUVETHON_PORT'])+"/locate"
kafka_endpoint = str(os.environ["KAFKA_IP"]) + ":" + str(os.environ["KAFKA_PORT"])
debug_level = os.environ["DEBUG_LEVEL"]
# pour dev
#topic_in = "housToTravel"
#topic_out = "locToColissi"
#geotrouvethon_url_locate="http://192.168.0.31:9966/locate"
#kafka_endpoint =  "192.168.0.31:8092"
#debug_level ="INFO"

if debug_level == "DEBUG":
    logging.basicConfig(level=logging.DEBUG)
elif debug_level == "INFO":
    logging.basicConfig(level=logging.INFO)
elif debug_level == "WARNING":
    logging.basicConfig(level=logging.WARNING)
elif debug_level == "ERROR":
    logging.basicConfig(level=logging.ERROR)
elif debug_level == "CRITICAL":
    logging.basicConfig(level=logging.CRITICAL)


if __name__ == '__main__':
    tasks = [
        consumers.Consumer(kafka_endpoint,topic_in,topic_out,geotrouvethon_url_locate)
    ]
    #lancement du thread de consomation du topic
    for t in tasks:
        t.start()