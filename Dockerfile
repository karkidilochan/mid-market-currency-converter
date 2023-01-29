FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim

WORKDIR /app/

RUN pip install -U pip setuptools wheel
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ /app

ENV PYTHONPATH=/app

ENV MODULE_NAME=src.main
