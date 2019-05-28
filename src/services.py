import requests

def getCoordFromLocation(locationName,url):
    session = requests.Session()
    url_location=url +"/"+locationName
    get_response = session.get(url_location)
    if get_response.status_code == 200:
        print("SUCCESSFUL REQUEST :  " + get_response)
        return get_response