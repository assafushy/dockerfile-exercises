FROM python:3.9
WORKDIR /app
RUN pip install psycopg2
COPY reader.py /app/reader.py
CMD ["python", "/app/reader.py"]
