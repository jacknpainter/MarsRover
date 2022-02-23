# syntax=docker/dockerfile:1

FROM python:latest

WORKDIR /app

COPY . .
CMD ["python3", "main.py"]