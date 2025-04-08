import sqlite3

conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30),
        product TEXT,
        quantity INT
    )
''')


cursor.execute('DELETE FROM orders')
cursor.execute('UPDATE sqlite_sequence SET seq = 0 WHERE name="orders"')
conn.commit()

def register(name, product, quantity):
    cursor.execute('INSERT INTO orders(name, product, quantity) VALUES(?,?,?)',
                  (name, product, quantity))
    conn.commit()

def delete(id):
    cursor.execute('DELETE FROM orders WHERE id = ?', (id,))
    conn.commit()
    print(f'Order {id} successfully deleted')

def fetch(id):
    cursor.execute('SELECT * FROM orders WHERE id = ?', (id,))
    print(cursor.fetchone())


register('Isko1', 'Shoes', 100)
register('Isko2', 'underwear', 10000000)
register('Isko3', 'Vodka', 1)


print("\nAll orders:")
cursor.execute('SELECT * FROM orders')
for order in cursor.fetchall():
    print(order)


cursor.execute('UPDATE orders SET quantity = ? WHERE product = "Vodka"', (10,))
conn.commit()


delete(2)


print("\nRemaining orders:")
cursor.execute('SELECT * FROM orders')
for order in cursor.fetchall():
    print(order)

conn.close()