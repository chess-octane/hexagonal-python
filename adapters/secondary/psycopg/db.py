from contextlib import contextmanager
import psycopg2

@contextmanager
def get_connection():
    conn = psycopg2.connect(dbname="octane", user="octane", password="octane", host="127.0.0.1")

    try:
        yield conn
    finally:
        conn.close()
