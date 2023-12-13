import psycopg2
from config import config
from settings import password

conn = psycopg2.connect(
    host='localhost',
    database='suppliers',
    user='postgres',
    password=password)

def connect():
    """ Connect to the PostgreSQL database server"""
    conn = None
    try:
        # Read Connection Parameters
        params = config()

        # Connect to the PostgreSQL server
        print('Connecting to the PostgreSQL Database...')
        conn = psycopg2.connect(**params)

        # Create Cursor
        cur = conn.cursor()

        # Execute a Statement
        print('PostgreSQL database Version:')
        cur.execute('SELECT version()')

        # Display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # Close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database Connection Closed')

if __name__ == '__main__':
    connect()
