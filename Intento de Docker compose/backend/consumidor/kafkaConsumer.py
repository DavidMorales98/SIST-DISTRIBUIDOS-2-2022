# Código del consumidor

# Librerías
from json import loads
from kafka import KafkaConsumer
from cassandra.cluster import Cluster
from funciones import continents, where
from datetime import datetime

# Algoritmo
cluster = Cluster()
session= cluster.connect('weather')
continentes=continents()
kafka_broker_hostname='localhost'
kafka_consumer_portno='9092'
kafka_broker=kafka_broker_hostname + ':' + kafka_consumer_portno
kafka_topic_input='weather'
# Se define el consumidor que traera los datos del Kafka topic
consumer = KafkaConsumer(kafka_topic_input, value_deserializer=lambda x: loads(x.decode('utf-8')))

# While True, se detiene con ctrl + c
while True:
    time = datetime.now()
    print("[",time,"] - CONSUMIENDO DATOS DEL CLIMA...")
    for message in consumer:
        message=message.value
        if(message["cod"] != '404'):
            continente = where(message['name'], continentes)
            if (continente!=False):
                time = datetime.now()
                try:
                    session.execute("INSERT INTO "+continente+" (id, time,coord, name, country, temp, temp_min, temp_max, pressure, humidity, wind_speed, wind_deg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (str(message["id"]), str(time),"lon:"+str(message["coord"]["lon"]) + " lat:"+str(message["coord"]["lat"]), message["name"], message["sys"]["country"], str(message["main"]["temp"]), str(message["main"]["temp_min"]), str(message["main"]["temp_max"]), str(message["main"]["pressure"]), str(message["main"]["humidity"]), str(message["wind"]["speed"]), str(message["wind"]["deg"])))
                except Exception as e:
                    #session.execute("UPDATE "+continente+" SET time=%s, temp=%s, temp_min=%s, temp_max=%s, pressure=%s, humidity=%s, wind_speed=%s, wind_deg=%s WHERE id=%s;", (str(time),str(message["main"]["temp"]), str(message["main"]["temp_min"]), str(message["main"]["temp_max"]), str(message["main"]["pressure"]),str(message["main"]["humidity"]), str(message["wind"]["speed"]), str(message["wind"]["deg"]),str(message['id'])))
                    print("ERROR AL ACTUALIZAR LA BASE DE DATOS")