import psycopg2
import time

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
    time.sleep(10)
    read_data()