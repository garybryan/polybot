# Build process
FROM node:12.13.1-alpine as build-deps

WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json /app/package.json

RUN npm install
CMD ["npm", "start"]
