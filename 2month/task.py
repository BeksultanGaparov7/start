class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f'{self.name} eats')
    def sleep(self):
        print(f'{self.name} sleeps')

class Walker:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name} walks')

class Swimmer:
    def __init__(self, name):
        self.name = name
        print(f'{self.name} swims')

    def swim(self):
        print(f'{self.name} swims')

class Flyer:
    def __init__(self, name):
        self.name = name
        print(f'{self.name} flies')

    def fly(self):
        print(f'{self.name} flies')

class Penguin(Animal, Walker, Swimmer):
    def __init__(self,name):
        super().__init__(name)
    def descripe(self):
        super().swim()
        super().walk()

class Duck(Animal, Walker, Swimmer, Flyer):
    def __init__(self, name):
        super().__init__(name)

    def descripe(self):
        super().swim()
        super().walk()
        super().fly()


class Bat(Animal, Flyer):
    def __init__(self, name):
        super().__init__(name)

    def descripe(self):
        super().fly()

animal = Animal('Penguin')
animal.eat()
animal.sleep()

duck = Duck('Duck')
duck.walk()
duck.swim()
duck.fly()
duck.descripe()

penguin = Penguin('penguin')
penguin.descripe()

bat = Bat('Bat')
penguin.descripe()