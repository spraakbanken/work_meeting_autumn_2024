FROM debian:testing-slim

RUN apt-get update \
 && apt-get install -y \
    python3 python3-venv python3-pip \
 && rm -rf /var/lib/apt/lists/*
RUN python3 -m venv env && . ./env/bin/activate && pip install flask
COPY ./app.py app/app.py
ENV LC_ALL=C.UTF-8
EXPOSE 5000
