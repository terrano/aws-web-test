FROM python:3.9-alpine

WORKDIR /app

COPY . /app

EXPOSE 80

ENTRYPOINT ["python", "server.py"]

