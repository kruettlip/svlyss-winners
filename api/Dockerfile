# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
COPY static/ .
COPY certs/ .

CMD [ "python3", "-m" , "flask", "--app", "api", "run", "--host=0.0.0.0", "--cert=certs/fullchain.pem", "--key=certs/fullchain.pem"]