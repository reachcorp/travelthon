import requests
import logging
import urllib as ul

def getCoordFromLocation(locationName,url):
    session = requests.Session()
    location_encode=ul.parse.quote(locationName)
    url_location=url +"/"+location_encode
    #appel a geotrouvethon http://127.0.0.1:9966/locate/<place>
    get_response = session.get(url_location)
    if get_response.status_code == 200:
        logging.info("SUCCESSFUL REQUEST :  " + str(get_response))
        latitude = get_response.json()[0]
        longitude = get_response.json()[1]
        locationCoordinates = str(latitude)+","+str(longitude)
        logging.info("REPONSE :  " + locationCoordinates)
        return locationCoordinates