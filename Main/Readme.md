Implementación de Spark para el almacenamiento de Datos
- David Morales
- Claudio Muñoz

Para el desarrollo de este código se utilizó el sistema operativo Ubuntu 22.04.

Para la creación de las bases de datos es necesario utilizar Apache Cassandra 4.0.5 o superior 
(Es posible utilizar versiones anteriores pero estas no han sido probadas).
En el terminal utilizar el comando "cqlsh", sin comillas para ingresar a Cassandra
una vez en el entorno de Cassandra se debe crear un Keyspace con el siguiente comando:

create keyspace weather with replication={'class'}:'SimpleStrategy', 'replication_factor':1}

Una vez creado el Keyspace , se debe ingresar a esta usando "USE weather;", y luego utilizar los comandos del archivo "cql.txt", y de esta forma la base de datos estará disponible para ejecutar el código.

Para el correcto funcionamiento de este código, se necesita instalar JDK-11 y Apache Kafka_2.13
Se recomienda el siguiente tutorial: https://tecadmin.net/how-to-install-apache-kafka-on-ubuntu-22-04/

Una vez instalados es necesario iniciar los servicios de Zookeeper y Kafka con los comandos:
sudo systemctl start zookeeper
sudo systemctl start kafka

Luego de esto se debe crear el topic que se utilizará con los siguientes comandos:
    
    cd /usr/local/kafka 
    
    bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic weather

Ahora para la ejecucion del código se necesita Python 3, junto a la instalacion de librerias como:

    pip install kafka-python
    pip install cassandra-driver
    pip install pyspark

Es necesario configurar el archivo KafkaProducer, 


Una vez se tenga instalado lo necesario, se debe ejcutar el consumidor y el productor en terminales diferentes y de forma simultanea, ej:

Terminal 1:
python3 kafkaConsumidor.py

Terminal 2 : 
python3 kafkaProductorSpark.py

Y de esta forma el código se ejecutara y la información se alamacenará en la base de datos de Cassandra, esta información se actualizará con una frecuencia definida según el valor utilizado en el time.sleep(tiempo) en el archivo del productor.

Para ver los cambios se puede utilizar un visualizador de base de datos o la terminal. En la terminal se debe ingresar al entorno de Cassandra con "cqlsh" y luego al Keyspace con "USE weather", ahora como ejemplo, para ver los datos de la tabla de America se debe ingresar lo siguiente:

    SELECT * FROM america

En las tablas de los demas continentes solo se necesita cambiar "america" por el nombre del continente, es decir "europa", "asia", "africa" o "oceania".
