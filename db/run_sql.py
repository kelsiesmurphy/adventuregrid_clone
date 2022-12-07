import psycopg2
import psycopg2.extras as ext
import os



def run_sql(sql, values = None):
    conn = None
    results = []

    try:
        postgres_password = os.getenv('POSTGRES_PASSWORD')
        postgres_dbname = os.getenv('POSTGRES_DBNAME')
        postgres_host = os.getenv('POSTGRES_HOST')
        postgres_port = os.getenv('POSTGRES_PORT')
        postgres_sslmode = os.getenv('POSTGRES_SSLMODE')
        postgres_user = os.getenv('POSTGRES_USER')
        conn=psycopg2.connect(
            dbname=postgres_dbname, 
            user=postgres_user, 
            password=postgres_password, 
            host=postgres_host,
            port=postgres_port,
            sslmode=postgres_sslmode
        )
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results
