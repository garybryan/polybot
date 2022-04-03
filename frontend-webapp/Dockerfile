# Build process
FROM node:16.14.2-alpine as build-deps

WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json /app/package.json

RUN npm install
CMD ["npm", "start"]
