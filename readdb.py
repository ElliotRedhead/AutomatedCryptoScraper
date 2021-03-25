import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="username",
                                  password="secret",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="database")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    insert = cursor.execute("INSERT INTO announcements(id, title, coin, datettime_added) VALUES(1, 'testtitle', 'testcoin',now())")
    # Commit to reflect inserted data
    connection.commit()
    cursor.execute("SELECT * FROM announcements;")
    records = cursor.fetchone()
    print(records)

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")