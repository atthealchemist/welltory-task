FROM python:3.9.2-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH .

EXPOSE 8080
WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . ./
ENTRYPOINT ["python", "app/main.py"]