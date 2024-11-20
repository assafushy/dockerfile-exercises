import psycopg2
from time import sleep

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
    print("Sample data inserted")

if __name__ == "__main__":
    sleep(10)
    insert_data()