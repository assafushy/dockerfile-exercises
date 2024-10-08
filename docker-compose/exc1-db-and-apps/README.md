### **Exercise 1: PostgresDB, Python App Writer, Python App Reader**

#### **Description**

In this exercise, you will create a setup with three services: a PostgreSQL database, a Python app that writes data to the database, and a Python app that reads from it. The `writer` app inserts data into the `postgres` database, while the `reader` app retrieves and displays it.

Before starting, create a project directory named `exercise1-postgres-python`.

#### **File: ./write/writer.py**

```python
import psycopg2

def insert_data():
    conn = psycopg2.connect(
        dbname="mydb", user="user", password="password", host="postgresdb"
    )
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data (id SERIAL PRIMARY KEY, info TEXT);")
    cur.execute("INSERT INTO data (info) VALUES ('Sample data');")
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    insert_data()
```

#### **File: ./reader/reader.py**

```python
import psycopg2

def read_data():
    conn = psycopg2.connect(
        dbname="mydb", user="user", password="password", host="postgresdb"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM data;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    read_data()
```

---

#### **Instructions for Dockerfile**

1. **For Postgres:**

   - Use the official Postgres image

2. **For Python Writer App:**

   - Base the Dockerfile on a Python image(python:3.9)
   - Set Workdir to `/app`.
   - install the necessary dependencies (`pip install psycopg2`).
   - Copy the `writer.py` file to the image.
   - Set the default command to start the writer app.(python /app/writer.py)

3. **For Python Reader App:**
   - Same steps as the writer app - but for reader.py

#### **Instructions for Docker Compose**

1. Create a `docker-compose.yml` file in the root project directory.
2. docker-compose version is 3
3. Create 3 services: `postgresdb`, `writer`, and `reader`.
4. for the postgres service:
   1. Define the `postgresdb` service with the official Postgres image.
   2. define the environment variables for the Postgres user, password, and database name.
      1. POSTGRES_USER = user
      2. POSTGRES_PASSWORD = password
      3. POSTGRES_DB = mydb
      4. expose the port 5432
5. For the writer service:
   1. Define the `writer` service build property with the Dockerfile in the `writer` directory.
   2. set the `depends_on` property to `postgresdb`.
6. For the reader service:
   1. Define the `reader` service build property with the Dockerfile in the `reader` directory.
   2. set the `depends_on` property to `postgresdb`.

#### **Solution Example**

1. Build and run the services:

   ```bash
   docker-compose up --build
   ```
