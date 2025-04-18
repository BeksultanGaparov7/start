from abc import abstractmethod, ABC
import sqlite3
class Person(ABC):
    @abstractmethod
    def __init__(self):
        pass

class DatabaseModel(ABC):
    @abstractmethod
    def __init__(self, db = 'database.db'):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def create_table(self):
        pass
    def add(self):
        pass
    def info(self):
        pass

class Student(Person, DatabaseModel):
    def __init__(self):
        pass
    def create_table_student(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        age INT)''')

    def add(self, full_name, age):
        self.cursor.execute('INSERT INTO students (full_name, age) VALUES (?,?)', (full_name, age))
        print('Updated Students')

    def info(self):
        self.cursor.execute('SELECT * FROM students')
        a = self.cursor.fetchall()
        for i in a:
            print(i)

class Course(DatabaseModel):
    def __init__(self):
        pass

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        teacher TEXT)''')

    def add(self, title, teacher):
        self.cursor.execute('INSERT INTO courses (title, teacher)')
        print('Updated Course')

    def info(self):
        self.cursor.execute('SELECT * FROM courses')
        a = self.cursor.fetchall()
        for i in a:
            print(i)




class Enrollment(DatabaseModel):
    def __init__(self):
        pass

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS enrollment(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT PRIMARY KEY,
        course_id TEXT PRIMARY KEY,
        grade INT)''')

    def add(self, title, teacher):
        self.cursor.execute('INSERT INTO courses (title, teacher)')
        print('Updated Course')


