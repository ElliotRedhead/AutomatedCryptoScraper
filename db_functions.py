import psycopg2
from psycopg2 import Error


def connect_db(db_name):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="username",
                                      password="secret",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="database")
        return connection
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)


def get_records(db_name, table_name):
    connection = connect_db(db_name)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name};")
    records = cursor.fetchone()
    return records


def insert_announcement_record(db_name, column_values):
    connection = connect_db(db_name)
    cursor = connection.cursor()
    try:
        SQL = f"INSERT INTO announcements (title, coin, datetime_added) VALUES(%s, %s, %s)"
        # Execute SQL query
        cursor.execute(SQL, (column_values))
        # Commit to reflect inserted data
        connection.commit()
    except (Exception, Error) as error:
        print("Error while executing SQL query", error)
    finally:
        cursor.close()
        connection.close()


def get_latest_announcement_record_title(db_name):
    connection = connect_db(db_name)
    cursor = connection.cursor()
    try:
        SQL = f"SELECT title FROM announcements ORDER BY datetime_added DESC LIMIT 1;"
        # Execute SQL query
        cursor.execute(SQL)
        result = cursor.fetchall()
    except (Exception, Error) as error:
        print("Error while executing SQL query", error)
    finally:
        cursor.close()
        connection.close()
        if(result):
            return result[0][0]


get_latest_announcement_record_title("database")
