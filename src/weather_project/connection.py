import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5000,
            dbname='mydb',
            user='hdh',
            password='my_pass'
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database connection failed: {e}")
        raise