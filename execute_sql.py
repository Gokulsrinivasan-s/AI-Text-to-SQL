import mysql.connector
from tabulate import tabulate


def execute_sql(query):

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gokul@1405",
        database="hr_database"
    )

    cursor = connection.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    # Get column names
    column_names = [column[0] for column in cursor.description]

    cursor.close()
    connection.close()

    return rows, column_names