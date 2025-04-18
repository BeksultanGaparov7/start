import sqlite3 as sq


class Task:
    def __init__(self, title, description, is_done):
        self.title = title
        self.description = description
        self.is_done = is_done
        self.db = TaskManager()

    def save(self):
        self.db.cursor.execute('INSERT INTO tasks (title, description, is_done) VALUES (?, ?, ?)',
                               (self.title, self.description, self.is_done))
        self.db.conn.commit()

    def mark_done(self, task_id):
        self.db.cursor.execute('UPDATE tasks SET is_done = 1 WHERE id = ?', (task_id,))
        self.db.conn.commit()
        print('UPDATED')

    def delete(self, task_id):
        self.db.cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        self.db.conn.commit()
        print('DELETED')


class TaskManager:
    def __init__(self, db='tasks.db'):
        self.conn = sq.connect(db)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        is_done BOOLEAN
        )
        ''')
        self.conn.commit()

    def get_all_tasks(self):
        self.cursor.execute('SELECT * FROM tasks')
        info = self.cursor.fetchall()
        for i in info:
            print(i)

    def get_pending_tasks(self):
        self.cursor.execute('SELECT * FROM tasks WHERE is_done = 0')
        info = self.cursor.fetchall()
        for i in info:
            print(i)

    def get_task_by_id(self, task_id):
        self.cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        info = self.cursor.fetchone()
        print(info)

    def delete_task(self, task_id):
        self.cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        self.conn.commit()
        print('SUCCESSFULLY DELETED')



if __name__ == "__main__":
    db = TaskManager()
    task = Task('INFO', 'INFO', True)
    task.save()
    db.get_all_tasks()