# develop stage
FROM node:14 as develop-stage
WORKDIR /app
COPY package*.json ./
RUN yarn global add @quasar/cli
RUN yarn install
COPY . .