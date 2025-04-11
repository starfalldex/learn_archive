FROM node:22-alpine

WORKDIR /app

COPY package.json .
#important for image caching
RUN npm install

COPY . .

EXPOSE 4000
# required for docker desktop port mapping

CMD ["node", "app.js"]