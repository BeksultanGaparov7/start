'''Абстракция'''

class Transport:
    def __init__(self, speed, brand):
        self.speed = speed
        self.brand = brand
    def info(self):
        print(f'{self.brand}, {self.speed}')

    def move(self):
        print("Транспорт движется")


class Car(Transport):

    def move(self):
        print("Машина едет по дороге")

    def honk(self):
        print("Машина сигналит")


class Bike(Transport):
    def move(self):
        print( "Велосипед едет по тропинке")

    def ring_bell(self):
        print("Велосипед звенит звонком")

class Airplane(Transport):
    def move(self):
        print("Самолет летит в небе")
    def take_off(self):
        print( "Самолет взлетает")


a = Transport('200km/h', 'mers')
b = Car('200000000km/h', 'BMW')
c = Bike('200km/h', 'motorbike')
d = Airplane('20000000000000000000000km/h', 'SAMALET')

for transports in (a,b,c,d):
    transports.info()
    transports.move()

b.honk()
c.ring_bell()
d.take_off()

'''Database'''

import sqlite3

conn = sqlite3.connect('beks.db')
cur = conn.cursor()







