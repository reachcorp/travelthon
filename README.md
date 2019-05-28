# travelthon

consomme une file kafka definit dans variable d'environnement
TRAVELTHON_IN
extrait le nom de la destination et l'id Bio de chaque message de la file
utilise le service REST de geotrouvethon (via les variable d'environnement GEOTROUVETHON_IP 
et GEOTROUVETHON_PORT) pour recuperer les coordonnées de la destination
rempli une file kafka dans variable d'environnement TRAVELTHON_OUT
avec l'id bio, la destination et ces coordonnées

variable d'environnement
KAFKA_IP
KAFKA_PORT
TRAVELTHON_IN
TRAVELTHON_OUT
GEOTROUVETHON_IP
GEOTROUVETHON_PORT

lancement:
python travelthon.py