FROM python:3.9.0-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc \
  # mysql dependencies
  && apt-get -y install default-libmysqlclient-dev build-essential \
  && apt-get clean

RUN pip install --upgrade pip \
  && pip install pipenv
COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv install --deploy --system

COPY . .

# entrypoint
COPY ./local-entrypoint.sh /usr/src/app/local-entrypoint.sh
RUN chmod +x /usr/src/app/local-entrypoint.sh

CMD ["/bin/bash", "-c", "./local-entrypoint.sh"]