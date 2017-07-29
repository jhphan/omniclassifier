FROM node:8.2.1
WORKDIR /usr/src/app
COPY package.json package-lock.json server.js ./
RUN npm install
EXPOSE 3010
ENTRYPOINT [ "npm", "start" ]
