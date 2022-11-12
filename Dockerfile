FROM python:3.10-slim-buster

WORKDIR src/app

RUN addgroup backend && adduser --disabled-password --gecos "" --ingroup backend backend
RUN chown -R backend:backend /src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="${PATH}:/home/backend/.local/bin"

COPY requirements.ini requirements.ini


RUN apt-get update && apt-get install -y netcat

USER backend

RUN pip install --user --upgrade pip && pip install --user -r requirements.ini