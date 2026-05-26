import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            host="db",
            port=5432,
            dbname='db',
            user='hdh',
            password='my_pass'
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database connection failed: {e}")
        raise