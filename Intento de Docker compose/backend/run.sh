#!/bin/bash

exec python3 kafkaConsumer.py &
exec python3 kafkaProducer.py &
echo SERVICIOS PYTHON INICIALIZADOS
