FROM python:3.9.0-slim

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000
