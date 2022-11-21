FROM python:3.10.1-bullseye

WORKDIR /app
RUN git clone https://github.com/edenhill/librdkafka
WORKDIR /app/librdkafka/
RUN apt update
RUN apt install build-essential
RUN ./configure
RUN make
RUN make install
RUN ldconfig
WORKDIR /consumer

COPY requirements.txt .


RUN python3 -m pip install -r requirements.txt --no-cache-dir


COPY . .


CMD ["python","kafkaConsumer.py"]
