#Инкапсуляция
from os import access


class Public():
    def __init__(self, value):
        self.value = value#public

    def info(self):
        return self.value#public

p = Public('Public class')
print(p.info())#вызов публчного атрибута
print(p.value)#acsess to public atribute

class Protected:
    def __init__(self, _value):
        self._value = _value#protected

    def _info(self):
        return self._value

protected = Protected('Protected class')
print(protected._info()) #it works but, not recommended
print(protected._value)

class Private:
    def __init__(self, value):
        self.__value = value#private
        self.value = self.__value

    def __info(self):
        return self.__value#private

    def access(self):
        return self.__info()#making private method public



private = Private('Private')
#print(private.__info())
print(private.access())

print(private._Private__info())#name managing

"""Полиморфизм"""

num1 = 1
num2 = 2
print(num1 + num2)

str = 'Hello'
str2 = 'Geeks '
print(str + str2)#конкантенация(склеивание)

print(len('Beksultan'))
print(len(['puthon', 'js','c++']))
print(len({'python':'django'}))

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f' I am a cat, my name is {self.name}, my age is {self.age}')

    def make_sound(self):
        print('Meaw')

class Dog:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def info(self):
        print(f' I am a dog, my name is {self.name}, my age is {self.age}')

    def make_sound(self):
        print('Gaf')

cat = Cat('Vasli', 2)
dog = Dog(4, 'Gaf')

for animal in (cat, dog):
    animal.info()
    animal.make_sound()









