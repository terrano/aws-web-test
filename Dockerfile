FROM python:3.9-alpine

WORKDIR /app

COPY . /app

ENTRYPOINT ["python", "server.py"]

