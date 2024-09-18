FROM alpine:latest

ENV POCKETBASE_HOST=0.0.0.0
ENV POCKETBASE_PORT=8090

RUN apk add --no-cache curl sqlite

RUN curl -L https://github.com/pocketbase/pocketbase/releases/download/v0.13.0/pocketbase_0.13.0_linux_amd64.zip -o pocketbase.zip

RUN unzip pocketbase.zip -d /usr/local/bin/ && rm pocketbase.zip

RUN mkdir -p /pb_data

WORKDIR /pb_data

EXPOSE 8090

CMD ["pocketbase", "serve", "--http=0.0.0.0:8090", "--dir=/pb_data"]
