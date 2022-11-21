# Código del Productor

# Librerías
from kafka import KafkaProducer
import json
import requests
import time
from funciones import continents, apiKey
import os.path

# Algoritmo
producer = KafkaProducer(bootstrap_servers = 'localhost:9092') # Se define al productor
API_KEY = apiKey() # Se guarda la key de Open Weather Map
continentes = continents() # Se guardan la lista de continentes con sus paises

# While True, se detiene con ctrl + c
while True:
    for continente in continentes:
        for pais in continente:
            response1 = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+pais+"&appid=" + API_KEY).json()
            producer.send('weather', json.dumps(response1).encode('utf-8'))
            producer.flush()
    time.sleep(60)