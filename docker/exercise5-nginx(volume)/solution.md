E
Example Dockerfile:

```Dockerfile
FROM nginx:latest
RUN mkdir -p /var/www
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

```bash
docker run -d -p 8080:80 -v $(pwd):/usr/share/nginx/my_site my-nginx-volume
```
