FROM python:3.9-alpine

WORKDIR /app

COPY . /app

EXPOSE 3000

CMD ["python", "server.py"]

