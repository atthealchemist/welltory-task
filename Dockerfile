FROM python:3.9.2-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH .

EXPOSE 8080
WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install pip==21.3.1 && \
    pip install poetry==1.1.12 && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . ./
ENTRYPOINT ["python", "app/main.py"]