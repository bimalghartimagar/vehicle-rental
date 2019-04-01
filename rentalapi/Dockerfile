FROM python:alpine

RUN mkdir /rentalapi/ 

WORKDIR /rentalapi/

ADD requirements.txt /rentalapi/

RUN pip install -r /rentalapi/requirements.txt

ADD . /rentalapi/
