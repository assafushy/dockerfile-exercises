Example Dockerfile:

```Dockerfile
FROM nginx:latest
RUN mkdir -p /usr/share/nginx/my_site
WORKDIR /usr/share/nginx/my_site
COPY index.html /usr/share/nginx/my_site
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```
