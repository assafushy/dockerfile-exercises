Example Dockerfile:

```Dockerfile
FROM node:latest
RUN mkdir -p /app
WORKDIR /app
COPY package.json .
RUN npm install
COPY app.js .
EXPOSE 3000
CMD ["npm", "start"]
```
