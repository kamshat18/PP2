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

# Добавление данных с консоли
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
            conn.commit()
    print(" Contact added.")

# Поиск
def search_by_name(name):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{name}%",))
            results = cur.fetchall()
            print(" Results:")
            for row in results:
                print(row)

# Поиск по шаблону
def search_pattern(pattern):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM phonebook
                WHERE name ILIKE %s OR phone ILIKE %s
            """, (f"%{pattern}%", f"%{pattern}%"))
            results = cur.fetchall()
            print("Pattern search results:")
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

# Функция: добавить или обновить

def insert_or_update_user(name, phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
            if cur.fetchone():
                cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (phone, name))
            else:
                cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
            conn.commit()
    print("User inserted/updated.")

# Массовая вставка

def insert_many_users(users):
    incorrect = []
    with connect() as conn:
        with conn.cursor() as cur:
            for name, phone in users:
                if phone.isdigit():
# if phone.isdigit() and 10 <= len(phone) <= 15: для лимита

                    cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
                    if cur.fetchone():
                        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (phone, name))
                    else:
                        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
                else:
                    incorrect.append((name, phone))
            conn.commit()
    print("Batch insert done. Incorrect entries:", incorrect)

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

# Меню
def menu():
    while True:
        print("\n PHONEBOOK MENU:")
        print("1. Add contact from console")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Search pattern")
        print("7. Insert/update one user")
        print("8. Insert many users")
        print("9. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            insert_from_console()
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
            pattern = input("Enter pattern to search: ")
            search_pattern(pattern)
        elif choice == "7":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            insert_or_update_user(name, phone)
        elif choice == "8":
            count = int(input("How many users to insert? "))
            users = []
            for _ in range(count):
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                users.append((name, phone))
            insert_many_users(users)
        elif choice == "9":
            print(" Byebye")
            break
        else:
            print("Invalid option!")

# Запуск
if __name__ == "__main__":
    menu()