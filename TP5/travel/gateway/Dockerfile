FROM python:3.11

RUN mkdir -p /usr/app
WORKDIR /usr/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["nameko", "run", "--config", "config.yml", "gateway"]
