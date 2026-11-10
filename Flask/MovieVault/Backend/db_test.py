import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
if not connection:
    print("Connection did not Established.")
else:    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies")
    result = cursor.fetchall()
    print(result)
    cursor.close()
    connection.close()
