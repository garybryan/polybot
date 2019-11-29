# Build process
FROM node:12.13.1-alpine as build-deps
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json /app/package.json

# TODO doesn't reinstall when updating package.json?
RUN npm install
RUN npm install react-scripts@3.2.0 -g

CMD ["npm", "start"]
