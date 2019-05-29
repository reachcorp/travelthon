
import os
import src.consumers as consumers


topic_in=os.environ['TOPIC_IN']
topic_out = os.environ["TOPIC_OUT"]
geotrouvethon_url_locate="http://"+str(os.environ['GEOTROUVETHON_IP'])+":"+str(os.environ['GEOTROUVETHON_PORT'])+"/locate"
kafka_endpoint = str(os.environ["KAFKA_IP"]) + ":" + str(os.environ["KAFKA_PORT"])
# pour dev
#travelthon_in = "travelthon_in"
#travelthon_out = "travelthon_out"
#geotrouvethon_url_locate="http://192.168.0.13:9966/locate"
#kafka_endpoint =  "192.168.0.13:8092"


if __name__ == '__main__':
    tasks = [
        consumers.Consumer(kafka_endpoint,topic_in,topic_out,geotrouvethon_url_locate)
    ]
    #lancement du thread de consomation du topic
    for t in tasks:
        t.start()