FROM python:3.9
WORKDIR /app
RUN pip install psycopg2
COPY writer.py /app/writer.py
CMD ["python", "/app/writer.py"]
