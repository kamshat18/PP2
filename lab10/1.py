import psycopg2
import csv
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    host="localhost",
    password="12345678",
    port=5432
)


def create_tables():
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Phonebook(
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            nomer VARCHAR(20)
        )
        """)
        conn.commit()
    print("table is created")
       
                
def insert_console():
    name = input("Name: ")
    nomer = input("Phone: ")
    with conn.cursor() as cur:
        cur.execute("INSERT INTO Phonebook(name, nomer) VALUES (%s, %s)", (name, nomer))
        conn.commit()
    print("contact added")


#In Python, the %s format specifier is used to represent a placeholder for a string 