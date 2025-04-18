import sqlite3

class Database:
    def __init__(self, db):
        self.db = db
        self.connect()
    def connect(self):
        self.conn = sqlite3.connect(self.db)
        return self.conn
    def disconnect(self):
        self.conn.close()



class User:
    def __init__(self):
        self.conn = sqlite3.connect('big.db')
        self.create()

    def create(self):
       self.conn.cursor().execute('''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        email VARCHAR (30)
        )
        ''')

    def add(self, full_name, email):
        self.conn.cursor().execute('INSERT INTO users (full_name, email) VALUES (?, ?)',
                                   (full_name, email))
        self.conn.commit()
        print('Success')

    def delete(self, id):
        self.conn.cursor().execute('DELETE users WHERE id = ?', (id,))
        self.conn.commit()

    def update(self, fullname, id):
        self.conn.cursor().execute('UPDATE users SET full_name = ? WHERE id = ?', (fullname,id))
        self.conn.commit()

class Costumer(User):
    def __init__(self):
        self.conn = sqlite3.connect('big.db')
        self.create()

    def create(self):
        self.conn.cursor().execute('''
            CREATE TABLE IF NOT EXISTS costumer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            email VARCHAR (30),
            dick_size INT
            )
            ''')

    def add(self, full_name, email, dick_size):
        self.conn.cursor().execute('INSERT INTO costumer (full_name, email, dick_size) VALUES (?, ?, ?)', (full_name, email, dick_size))
        self.conn.commit()
        print('Success')

    def delete(self, id):
        self.conn.cursor().execute('DELETE costumer WHERE id = ?', (id,))
        self.conn.commit()

    def update(self, dick_size, id):
        self.conn.cursor().execute('UPDATE costumer SET dick_size = ? WHERE id = ?',(dick_size,id))
        self.conn.commit()

class Admin(User):
    def __init__(self):
        self.conn = sqlite3.connect('big.db')
        self.create()

    def create(self):
        self.conn.cursor().execute('''
            CREATE TABLE IF NOT EXISTS admin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            email VARCHAR (30),
            status VARCHAR (30)
            )
            ''')
    def add(self, full_name, email, status):
        self.conn.cursor().execute('INSERT INTO admin (full_name, email, status) VALUES (?,?,?)', (full_name, email, status))
        self.conn.commit()
        print('Success')

    def update(self, status,id):
        self.conn.cursor().execute('UPDATE admins SET status = ? WHERE id = ?', (status,id))
        self.conn.commit()
        print('Success')




db = Database('big.db')
costumer = Costumer()
costumer.add('bg', 'bg@gmail.com', 28)

user = User()
user.add('bg', 'jfjkf@gmail')
user.update('bg2', 1)
costumer.update(25, 1)

