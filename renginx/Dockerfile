# == production stage ==
FROM nginx:alpine AS prod
WORKDIR /www/
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=airstorage/frontend:prod /usr/src/app/dist ./data/dist
