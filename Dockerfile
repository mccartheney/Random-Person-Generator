FROM python:3.12-slim

WORKDIR /app

COPY ./backend/pyproject.toml /app/

COPY ./backend /app/

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install

EXPOSE 8000

CMD [ "python", "src/main.py" ]