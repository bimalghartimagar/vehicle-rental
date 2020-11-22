FROM node:14.6.0-alpine3.12

RUN mkdir /rentalapp/

WORKDIR /rentalapp/

ADD package.json yarn.lock *.js /rentalapp/

RUN yarn

COPY . .