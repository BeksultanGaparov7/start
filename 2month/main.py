"ООП"
class Game:
    def __init__(self, name, year, company, graphics):
        self.name = name
        self.year = year
        self.company = company
        self.graphics = graphics

    def info(self):
        print(f'Game - {self.name} - {self.year} - {self.company} - {self.graphics}')

game = Game('Minecraft', 2017, 'Mojang', 'Full HD')
game.info()
class Roblox(Game):
    def __init__(self, name, year, company, graphics, multiplayer):
        super().__init__(name, year, company, graphics)
        self.multiplayer = multiplayer
        self.name = 'Player'
        self.gender = 'None'
        self.skin = "None"
        self.hp = 100

    #def info(self):
        #return super().info()
    def info(self):
        print(f'Game - {self.name} - {self.year} - {self.company} - {self.graphics} - {self.multiplayer}')

    def info_player(self):
        print(f'Player - {self.player_name} - {self.player_gender} - {self.player_skin} - {self.hp}')

    def edit_player(self):
        player_name = input('Enter name: ')
        player_skin = input('Enter skin: ')
        player_gender = input('Enter gender: ')

        self.player_name = player_name
        self.player_skin = player_skin
        self.player_gender = player_gender


roblox = Roblox('Roblox', 2006, 'Roblox corp.', 'Ultra', '4 people')
#roblox.info()
#roblox.edit_player()
#roblox.info_player()

class Strike(Roblox):
    def __init__(self, name, year, company, graphics, multiplayer):
        super().__init__(name, year, company, graphics, multiplayer)

    def edit_player(self):
        return super().edit_player()
    def info_player(self):
        return super().info_player()

strike = Strike('booo', 232, 'dfd', 'derer', 'ree')




import sqlite3
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (30),
            product TEXT,
            quantity INT
        )
''')

def register(name, product, quantity):
    cursor.execute('INSERT INTO orders(name, product, quantity) VALUES(?,?,?)', (name, product, quantity))
    conn.commit()

def delete(id):
    cursor.execute('DELETE FROM orders WHERE id = ?', (id,))
    conn.commit()
    print(f'Order {id} successfully deleted')

def fetch(id):
    cursor.execute('SELECT * FROM orders WHERE id = ?',(id,))
    fetch = cursor.fetchone()
    print(fetch)

register('Isko1', 'Shoes', 100)
register('Isko2', 'underwear', 10000000)
register('Isko3', 'Vodka', 1)

cursor.execute('SELECT * FROM orders')
all = cursor.fetchall()
for i in all:
 print(i)
cursor.execute('SELECT * FROM orders WHERE quantity > 1')
conn.commit()
select = cursor.fetchall()
print(select)
cursor.execute('UPDATE orders SET quantity = ? WHERE id = ?',(10,3))
delete(2)
cursor.execute('SELECT * FROM orders')
all = cursor.fetchall()
for i in all:
    print(i)

conn.close()


