import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gokul@1405",
    database="hr_database"
)


if connection.is_connected():
    print("MySQL Connected Successfully")