FROM node:lts-alpine

MAINTAINER arkanister "arkanister.dev@gmail.com"

# install simple http server for serving static content
RUN npm install -g http-server

WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY frontend/ .

# install project dependencies
RUN npm install

# build app for production with minification
RUN npm run build

ENTRYPOINT ["http-server", "dist"]
EXPOSE 8080
