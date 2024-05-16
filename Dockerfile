FROM python:3.12.3-slim

WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

CMD python dsmr-relay.py