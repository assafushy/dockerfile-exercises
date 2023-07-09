Exercise 1: Creating a Basic Web Server Image

Description: This Docker image will serve a static web page via nginx.

Before Starting your Dockerfile:

1. Create a directory named `exercise1-nginx`.
2. create a file named `index.html` with the following contents.
3. Create a file called `nginx.conf` with the following contents.

File: index.html

```html
<!DOCTYPE html>
<html>
  <body>
    <h1>Hello, Docker!</h1>
  </body>
</html>
```

File: nginx.conf

```nginx
server {
    listen 80;
    server_name localhost;

    location / {
        root   /usr/share/nginx/my_site;
        index  index.html index.htm;
    }

    error_page   500 502 503 504  /50x.html;

    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}
```

Instructions:

1. Base your Dockerfile on the latest official nginx image.
2. Create a directory named `my_site` for your web content.using the command - "mkdir -p /usr/share/nginx/my_site"
3. Set this directory as your work directory.
4. Copy a custom index.html file into the newly created directory.
5. Copy nginx.conf file to the default nginx configuration directory - /etc/nginx/conf.d/default.conf
6. Expose port 80." option
7. Set the default command for the image to run nginx in the foreground - "nginx -g daemon off;"

Build and run your image with the following:

```bash
  docker build -t my-nginx-image .
  docker run -d -p 8080:80 my-nginx-image
```
