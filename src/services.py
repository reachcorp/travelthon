import requests

def getCoordFromLocation(locationName,url):
    session = requests.Session()
    url_location=url +"/"+locationName
    #appel a geotrouvethon http://127.0.0.1:9966/locate/<place>
    get_response = session.get(url_location)
    if get_response.status_code == 200:
        locationCoordinates = str(get_response.content, "utf-8")
        print("SUCCESSFUL REQUEST :  " + str(get_response))
        return locationCoordinates