FROM node:8.15.0-alpine

RUN mkdir /rentalapp/

WORKDIR /rentalapp/

ADD package.json yarn.lock *.js /rentalapp/

RUN yarn

COPY . .