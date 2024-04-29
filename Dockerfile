FROM python:3.10-slim

RUN apt-get update && apt-get install -qq -y \
    bash git python3-dev curl wget gcc \
    libpq-dev libssl-dev build-essential \
    openssh-client libcurl4-openssl-dev

RUN pip install uwsgi

ENV HOME=/home/work

RUN useradd -ms /bin/bash work && \
    mkdir -p /root/.ssh && \
    mkdir -p ${HOME}/logs

RUN mkdir -p migrations

# Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
RUN pip install uwsgi

COPY src src
COPY uwsgi.ini uwsgi.ini
COPY wsgi.py wsgi.py
COPY scheduler.py scheduler.py

expose 5000

ENTRYPOINT ["uwsgi", "--ini", "./uwsgi.ini", "--enable-threads", "--single-interpreter"]
