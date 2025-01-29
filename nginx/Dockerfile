FROM nginx:alpine

RUN apk --no-cache add certbot

COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80