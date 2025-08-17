import mysql.connector
from mysql.connector import errorcode
import os

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'your_username')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'your_password')
DATABASE_NAME = "alx_book_store"
CREATE DATABASE IF NOT EXISTS alx_book_store

def create_database(cursor):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DATABASE_NAME}`")
        print(f"Database '{DATABASE_NAME}' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed to create database: {err}")


def main():
    mydb = None
    try:
        print(f"Attempting to connect to MySQL server at {DB_HOST}...")
        mydb = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )


        if mydb.is_connected():
            print("Successfully connected to MySQL server.")
            cursor = mydb.cursor()
            create_database(cursor)
            cursor.close()
        else:
            print("Failed to connect to MySQL server.")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: Could not connect to the database. Reason: {err}")

    finally:
        if mydb and mydb.is_connected():
            mydb.close()
            print("MySQL connection closed.")


if __name__ == "__main__":
    main()

