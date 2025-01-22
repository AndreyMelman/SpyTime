FROM python:3.12-slim

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-root

COPY ./app /code/app

WORKDIR /code/app

EXPOSE 8000

#CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]