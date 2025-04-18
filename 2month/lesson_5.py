import sqlite3

connect = sqlite3.connect("geeks.db")
cursor = connect.cursor()

cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name VARCHAR (50) NOT NULL,
            age INT DEFAULT NULL, 
            direction TEXT,
            is_have BOOLEAN NOT NULL DEFAULT FALSE,
            birth_date DATE,
            rating DOUBLE (4,2) DEFAULT (0.0)        
        )                       
""")


def register():
    full_name = input("Введите ФИО: ")
    age = int(input("Введите возраст: "))
    direction = input("Введите направление: ")
    is_have = bool(input("Наличие ноутбука: "))
    birth_date = input("Введите дату рождения: ")
    rating = float(input("Введите свой рейтинг: "))

    # cursor.execute(f""" INSERT INTO users
    #                (full_name, age, direction, is_have, birth_date, rating)
    #                VALUES ('{full_name}', {age}, '{direction}', {is_have}, '{birth_date}', {rating})""")

    # connect.commit() # Сохранение измения в бд

    # Использование форматированных строк (f"") для вставки значений в SQL-запрос может привести к уязвимости типа SQL-инъекция, если пользователь вводит специальные символы в текстовые поля.

    cursor.execute(""" INSERT INTO users
                   (full_name, age, direction, is_have, birth_date, rating)
                   VALUES (?, ?, ?, ?, ?, ?)""", (full_name, age, direction, is_have, birth_date, rating))

    connect.commit()


# def all_students():
#     cursor.execute("SELECT * FROM users")
#     students = cursor.fetchall()
#     print(students)

def all_students():
    cursor.execute("SELECT * FROM users WHERE id > 0")
    students = cursor.fetchone()
    print(students)


def delete_students(id):
    cursor.execute("DELETE FROM users WHERE id=?", (id,))
    connect.commit()
    print(f"Пользователь {id}, был успешно удален")


#register()
all_students()

# all_students(3)
# register()

