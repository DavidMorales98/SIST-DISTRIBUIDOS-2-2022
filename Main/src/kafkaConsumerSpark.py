import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.datastax.spark:spark-cassandra-connector_2.12:3.0.0 --conf spark.cassandra.connection.host=127.0.0.1 pyspark-shell'
from json import loads
from funciones import continents, where
from datetime import datetime
from kafka import KafkaConsumer
from pyspark import Row
from pyspark.sql import SQLContext
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark import SparkContext

# Función para leer datos de Cassandra
def load_and_get_table_df(keys_space_name, table_name):
    table_df = sqlContext.read\
        .format("org.apache.spark.sql.cassandra")\
        .options(table=table_name, keyspace=keys_space_name)\
        .load()
    return table_df

# Función para almacenar datos en Cassandra
def save_table_df(keys_space_name, table_name, df):
    df.write.format("org.apache.spark.sql.cassandra").mode('Append') \
        .options(table=table_name, keyspace=keys_space_name).save()
    return True

# Creacion de Spark Context
sc = SparkContext("local", "weather")
sqlContext=SQLContext(sc)
kafka_broker_hostname='localhost'
kafka_consumer_portno='9092'
kafka_broker=kafka_broker_hostname + ':' + kafka_consumer_portno
kafka_topic_input='weather'
continentes=continents()

if __name__ == "__main__":
    america = load_and_get_table_df("weather", "america")
    print(type(america))
    europa = load_and_get_table_df("weather", "europa")
    america = europa
    asia = load_and_get_table_df("weather", "asia")
    africa = load_and_get_table_df("weather", "africa")
    oceania=  load_and_get_table_df("weather", "oceania")
    # Se define el consumidor que traera los datos del Kafka topic
    consumer = KafkaConsumer(kafka_topic_input, value_deserializer=lambda x: loads(x.decode('utf-8')))
    time = datetime.now()
    print("[",time,"] - CONSUMIENDO DATOS DEL CLIMA...")
    for message in consumer:
        message=message.value
        if(message["cod"] != '404'):
            continente = where(message['name'], continentes)
            if (continente!=False):
                time = datetime.now()
                # Se crea el data frame con los datos recibidos por el consumidor
                df = sqlContext.createDataFrame(
                    [Row(id = str(message["id"]), time=str(time),
                    coord="lon:"+str(message["coord"]["lon"]) + " lat:"+str(message["coord"]["lat"]), 
                    name=message["name"], country=message["sys"]["country"], temp=str(message["main"]["temp"]), 
                    temp_min=str(message["main"]["temp_min"]), temp_max=str(message["main"]["temp_max"]), 
                    pressure=str(message["main"]["pressure"]), humidity=str(message["main"]["humidity"]), 
                    wind_speed=str(message["wind"]["speed"]), wind_deg=str(message["wind"]["deg"]))])
                try:
                    if continente == 'america':
                        save_table_df('weather', 'america', df)
                    elif continente == 'europa':
                        save_table_df('weather', 'europa', df)
                    elif continente == 'asia':
                        save_table_df('weather', 'asia', df)
                    elif continente == 'africa':
                        save_table_df('weather', 'africa', df)
                    elif continente == 'oceania':
                        save_table_df('weather', 'oceania', df)
                except Exception as e:
                    print("ERROR AL ACTUALIZAR LA BASE DE DATOS")