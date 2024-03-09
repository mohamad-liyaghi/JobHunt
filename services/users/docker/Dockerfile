FROM python:3.12-alpine

WORKDIR /backend

COPY pyproject.toml poetry.lock /backend/

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-root

COPY . /backend/

ENV PYTHONPATH=/backend/src