FROM python:alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

RUN mkdir /rentalapi/ 

WORKDIR /rentalapi/

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY . .
