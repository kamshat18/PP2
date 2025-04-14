import psycopg2
import csv

# 🔌 Подключение к базе
def connect():
    return psycopg2.connect(

       database="postgres",
       user="postgres",
       host="localhost",
       password="12345678",
       port=5432

    )

# Создание таблицы
def create_table():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    phone VARCHAR(20)
                )
            """)
            conn.commit()
    print(" Таблица phonebook успешно создана!")

# Вызов функции
create_table()

#  Добавление данных с консоли
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
            conn.commit()
    print(" Contact added.")

#  Загрузка из CSV
def insert_from_csv(filename
                ):
    with connect() as conn:
        with conn.cursor() as cur:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
            conn.commit()
    print(" Contacts imported from CSV.")

#  Поиск
def search_by_name(name):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{name}%",))
            results = cur.fetchall()
            print(" Results:")
            for row in results:
                print(row)

# Обновление данных
def update_contact(old_name, new_name=None, new_phone=None):
    with connect() as conn:
        with conn.cursor() as cur:
            if new_name:
                cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (new_name, old_name))
            if new_phone:
                cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, old_name))
            conn.commit()
    print("Contact updated.")

# Удаление
def delete_contact(name=None, phone=None):
    with connect() as conn:
        with conn.cursor() as cur:
            if name:
                cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
            elif phone:
                cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
            conn.commit()
    print(" Contact deleted.")

#  Пример меню
def menu():
    create_table()
    while True:
        print("\n PHONEBOOK MENU:")
        print("1. Add contact from console")
        print("2. Import from CSV")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            filename = input("Enter CSV filename: ")
            insert_from_csv(filename)
        elif choice == "3":
            name = input("Enter name to search: ")
            search_by_name(name)
        elif choice == "4":
            old_name = input("Old name: ")
            new_name = input("New name (press Enter to skip): ") or None
            new_phone = input("New phone (press Enter to skip): ") or None
            update_contact(old_name, new_name, new_phone)
        elif choice == "5":
            delete_by = input("Delete by (name/phone): ")
            value = input("Enter value: ")
            if delete_by == "name":
                delete_contact(name=value)
            elif delete_by == "phone":
                delete_contact(phone=value)
        elif choice == "6":
            print(" Bye!")
            break
        else:
            print("Invalid option!")

#  Запуск
if __name__ == "__main__":
    menu()
