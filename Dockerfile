FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y python3 python3-dev python3-pip 

RUN pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

CMD python3 main.py

EXPOSE 5000



