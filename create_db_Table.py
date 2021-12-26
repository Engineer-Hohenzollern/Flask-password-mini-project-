import psycopg2.extras
import psycopg2

host = 'localhost'
database = 'my_password_project'
username = 'postgres'
pas = 'richy'
port = 5432
conn = None

try:
    with psycopg2.connect(
            host=host,
            dbname=database,
            user=username,
            password=pas,
            port=port) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute('DROP TABLE IF EXISTS ric')

            create_script = ''' CREATE TABLE IF NOT EXISTS ric (
                                    id      int PRIMARY KEY,
                                    name    varchar(45) NOT NULL,
                                    password  varchar(45) NOT NULL)'''

            cur.execute(create_script)

            insert_script = 'INSERT INTO ric (id, name,password) VALUES (%s, %s, %s, %s)'
            insert_values = [(1, 'Name1', 'pass1'), (2, 'Name2', 'pass2'), (3, 'Name3', 'pas3')]
            for record in insert_values:
                cur.execute(insert_script, record)


except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
