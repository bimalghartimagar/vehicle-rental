FROM node:14.3.0-alpine3.11

RUN mkdir /rentalapp/

WORKDIR /rentalapp/

ADD package.json yarn.lock *.js /rentalapp/

RUN yarn

COPY . .