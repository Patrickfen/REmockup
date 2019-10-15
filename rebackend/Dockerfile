# == development stage ==
FROM python:3.7-alpine AS dev
RUN apk add --no-cache bash
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# == production stage ==
FROM dev AS prod
COPY . .
RUN pip install --no-cache-dir gunicorn
