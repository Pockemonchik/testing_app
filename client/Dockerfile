FROM node:19-alpine
EXPOSE 8080
RUN npm install -g nodemon
WORKDIR /app
COPY package.json .
RUN npm install
RUN npm install -g @vue/cli
COPY . .
CMD ["npm", "run", "serve"]