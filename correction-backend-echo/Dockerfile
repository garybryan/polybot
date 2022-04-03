FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ARG ENV

ENV ENV=${ENV} \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.0.10

RUN apt update && apt install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN pip install "poetry==$POETRY_VERSION"

RUN poetry config virtualenvs.create false \
    && poetry install $(test "$ENV" == production && echo "--no-dev") --no-interaction --no-root --no-ansi

# TODO don't copy tests when env==production
COPY . ./
