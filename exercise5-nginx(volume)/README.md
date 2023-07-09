Exercise 5: This image will run an nginx server that serves files from a volume.

Before Starting your Dockerfile:

1. Create a directory named `exercise5-nginx`.
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

1. Use the nginx image as your base.
2. Create a new directory, `/usr/share/nginx/my_site`, for your web content.
3. Copy nginx.conf file to the default nginx configuration directory - /etc/nginx/conf.d/default.conf
4. Expose port 80." option
5. Set the default command for the image to run nginx in the foreground - "nginx -g daemon off;"
6. In Docker run, mount the newly created directory to the container's `/var/www` directory.So that the files in the container are mapped to the files in the host machine directory with the index.html.

Docker commands:

```bash
docker build -t my-nginx-volume .
```
