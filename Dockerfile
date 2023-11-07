FROM python:3.10
RUN mkdir /server && apt-get update && apt-get install -y git libpq-dev postgresql-client

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

copy . /code
