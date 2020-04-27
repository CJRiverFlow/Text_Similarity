FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y python3 python3-dev python3-pip 

RUN pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD python3 main.py





