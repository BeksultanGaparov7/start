class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        pass
    def info(self):
        print(self.year,self.model,self.brand)

class Car(Vehicle):
    def __init__(self, brand, year, model, doors):
        super().__init__(brand,year,model)
        self.doors = doors

    def start_engine(self):
        print(f'Engine of {self.brand} is working.')

    def info(self):
        print(self.year, self.model, self.brand, self.doors)

class Bike(Vehicle):
    def __init__(self, brand, year, model, doors, bike_type):
        super().__init__(brand, year, model)
        self.doors = doors
        self.type = bike_type

    def start_engine(self):
        print(f'Engine of {self.brand} is working.')

    def info(self):
        print(self.year, self.model, self.brand, self.doors, self.type)


matiz = Vehicle('Matiz', 'daewoo', '1999')
lamborghini = Car('Lamborghini', '2025', 'huracan', 0)
moto = Bike('Neiman Marcus', '2025', 'Limited Edition Fighter', '0', 'expensive')

matiz.info()
lamborghini.info()
lamborghini.start_engine()
moto.info()
moto.start_engine()







