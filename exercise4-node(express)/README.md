Exercise 4: Expose a Port Image

Description: This image will run a Node.js app and expose port 3000.

Before Starting your Dockerfile:

1. Create a directory named `exercise3-env-var`.
2. Create a file named `app.js` with the following contents.
3. Create a file named `package.json` with the following contents.

File: app.js

```javascript
const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  res.send("Hello Docker!");
});

app.listen(port, () => {
  console.log(`App running on http://localhost:${port}`);
});
```

File: package.json

```json
{
  "name": "docker-node",
  "version": "1.0.0",
  "description": "Node.js on Docker",
  "main": "app.js",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.16.1"
  }
}
```

Instructions:

1. Use the Node image as your base.
2. Create a directory named `/app` for your application.
3. Set this directory as your work directory.
4. Copy package.json into the image.
5. Install all dependencies using `npm install` command.
6. Copy your app into the image.
7. Expose port 3000.
8. Start your Node.js app, using `npm start` command.

Docker commands:

```bash
   docker build -t my-node-app .
   docker run -d -p 3000:3000 my-node-app

   //to check if the logs run:
   docker logs <container-id>
```
