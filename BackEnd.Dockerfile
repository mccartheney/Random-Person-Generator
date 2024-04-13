FROM python:3.12-slim

WORKDIR /app

COPY ./backend ./app

RUN pip install poetry

RUN poetry config virtualenvs.create false

VOLUME [ "/app" ]

EXPOSE 8004
