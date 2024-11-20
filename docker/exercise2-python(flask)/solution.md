Example Dockerfile:

```Dockerfile
FROM python:latest
RUN mkdir -p /app
WORKDIR /app
COPY app.py /app
RUN pip install flask
CMD ["python", "app.py"]
```
