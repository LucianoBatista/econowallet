FROM python:3.9.2-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

RUN pip install --upgrade pip \
  && pip install pipenv
COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv install --deploy --system

COPY . .