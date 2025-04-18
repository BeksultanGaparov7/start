import sqlite3
class Database:
    def __init__(self, db_name = 'users.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(20) NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INT
            )
            """)

    def add_user(self, user):
        self.cursor.execute('INSERT INTO users (name, email, age) VALUES(?,?,?)', (user.name, user.email, user.age))
        self.conn.commit()
        print('Successful commit')

    def get_user(self, email):
        self.cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        return self.cursor.fetchone()
    def delete_user(self, email):
        self.cursor.execute('DELETE FROM users WHERE email = ?', (email,))
        self.conn.commit()
        print(f'User with email: {email} has been deleted.')
