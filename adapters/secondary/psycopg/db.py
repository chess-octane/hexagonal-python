from contextlib import contextmanager
import psycopg2

@contextmanager
def get_connection():
    conn = psycopg2.connect(dbname="octane", user="octane", password="octane", host="db")

    try:
        yield conn
    finally:
        conn.close()
