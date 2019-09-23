# == development stage ==
FROM node:11.6.0-alpine AS dev
RUN apk add --no-cache bash
WORKDIR /usr/src/app
COPY package*.json ./
RUN mkdir ../node_modules && ln -s ../node_modules && npm install && rm ./node_modules

# == production stage ==
FROM dev AS prod
COPY . .
RUN npm run test
RUN npm run build
