# Código del Productor

# Librerías
from kafka import KafkaProducer
import json
import requests
import time as t
from funciones import continents, apiKey
import os.path
from datetime import datetime

# Algoritmo
producer = KafkaProducer(bootstrap_servers = 'localhost:9092') # Se define al productor
API_KEY = apiKey() # Se guarda la key de Open Weather Map
continentes = continents() # Se guardan la lista de continentes con sus paises

contador = 0
# While True, se detiene con ctrl + c
while True:
    contador += 1
    time = datetime.now()
    print("[",time,"] - EXTRAYENDO DATOS DE OPEN WEATHER MAP...")
    for continente in continentes:
        for pais in continente:
            response1 = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+pais+"&appid=" + API_KEY).json()
            producer.send('weather', json.dumps(response1).encode('utf-8'))
            producer.flush()
            if (response1["cod"] == '404'):
                time = datetime.now()
                print("[",time,"] - " + pais + " response: " + str(response1["cod"]))
    time = datetime.now()
    print("[",time,"] - Termina el ciclo " + str(contador))
    print("\nESPERANDO...\n")
    t.sleep(600)
    time = datetime.now()
    print("[",time,"] - EXTRAYENDO DATOS DE OPEN WEATHER MAP...")