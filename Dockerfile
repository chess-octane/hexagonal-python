FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt /app/

RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y postgresql-client

COPY scripts/wait-for-db.sh scripts/rundjango.sh /app/
