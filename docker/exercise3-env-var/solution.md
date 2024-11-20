Example Dockerfile:

```Dockerfile
FROM alpine
RUN mkdir /env
WORKDIR /env
ENV myVar="Hello, Docker!"
CMD ["sh", "-c", "echo Current directory: $(pwd) && echo $myVar"]
```
