FROM node:14.6.0-alpine3.12 as base

RUN mkdir /rentalapp/

WORKDIR /rentalapp/

ADD package.json  *.js /rentalapp/

RUN yarn

COPY . .

FROM base as development
CMD ["yarn", "serve"]

FROM base as builder
ENV NODE_ENV=production
RUN yarn build

FROM nginx:1.21.0-alpine as production
COPY --from=builder /rentalapp/dist /usr/share/nginx/html