import psycopg
from dotenv import load_dotenv
import os

load_dotenv()

connection = psycopg.connect(
    host=os.getenv("DATABASE_HOST"),
    port=os.getenv("DATABASE_PORT"),
    dbname=os.getenv("DATABASE_NAME"),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD")
)

cursor = connection.cursor()

cursor.execute(
    """
    INSERT INTO tasks(title)
    VALUES (%s)
    """,
    ("Learn FastAPI",)
)

connection.commit()

print("Task inserted successfully!")

cursor.close()
connection.close()