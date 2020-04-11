FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN apt update && apt install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY ./app /app
