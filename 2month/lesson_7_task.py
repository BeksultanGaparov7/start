import sqlite3

class Library:
    def __init__(self, title=None, author=None):
        self.title = title
        self.author = author
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS library(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                author TEXT,
                title TEXT
            )
        ''')
        self.conn.commit()

    def add_book(self):
        if self.title and self.author:
            self.cursor.execute(
                'INSERT INTO library (title, author) VALUES (?, ?)',
                (self.title, self.author)
            )
            self.conn.commit()
            print(f"Added book: '{self.title}' by {self.author}")
        else:
            print("Error: Title and author must be provided.")

    def delete_book(self, id):
        self.cursor.execute('DELETE FROM library WHERE id = ?', (id,))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print(f"Deleted book with ID: {id}")
        else:
            print(f"No book found with ID: {id}")

    def list_books(self):
        self.cursor.execute('SELECT * FROM library')
        books = self.cursor.fetchall()
        if books:
            print("\nBooks in Library:")
            for book in books:
                print(f"ID: {book[0]}, Title: '{book[2]}', Author: {book[1]}")
        else:
            print("The library is empty.")

    def close(self):
        self.conn.close()

# Example usage
if __name__ == "__main__":
    lib = Library()
    lib.add_book()

    book = Library("Harry Potter", "J.K. Rowling")
    book.add_book()
    book.list_books()


    book.delete_book(1)
    book.list_books()
    book.close()