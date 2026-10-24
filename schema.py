import mysql.connector


def get_schema():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gokul@1405",
        database="hr_database"
    )

    cursor = connection.cursor()


    schema = ""


    cursor.execute("SHOW TABLES")

    tables = cursor.fetchall()


    for table in tables:

        table_name = table[0]

        schema += f"\nTable: {table_name}\n"

        cursor.execute(f"DESCRIBE {table_name}")

        columns = cursor.fetchall()


        schema += "Columns:\n"


        for column in columns:

            column_name = column[0]
            column_type = column[1]

            schema += f"- {column_name} ({column_type})\n"


    cursor.close()
    connection.close()


    return schema



database_schema = get_schema()


print(database_schema)