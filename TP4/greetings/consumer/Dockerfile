FROM python:3.8-slim-buster

ARG DEFAULT_RABBIT_USER=guest
ARG DEFAULT_RABBIT_PASSWORD=guest
ARG DEFAULT_RABBIT_HOST=rabbitmq
ARG DEFAULT_RABBIT_PORT=5672

ENV RABBIT_USER=${DEFAULT_RABBIT_USER}
ENV RABBIT_PASSWORD=${DEFAULT_RABBIT_PASSWORD}
ENV RABBIT_HOST=${DEFAULT_RABBIT_HOST}
ENV RABBIT_PORT=${DEFAULT_RABBIT_PORT}

# Install netcat and remove apt cache to reduce image size
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

WORKDIR /src

COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod a+x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]