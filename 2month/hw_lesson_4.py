class Transport:
    def __init__(self):
        self._speed = 0

    def move(self):
        print('Transport is moving')

    def set_speed(self, speed):
        self._speed = speed

    def get_speed(self):
        return self._speed

class Car(Transport):
    def move(self):
        print('Car is moving')


class Bicycle(Transport):
    def move(self):
        print('Bicycle is moving')


transport_list = [Car(), Bicycle()]

transport_list[0].set_speed(60)
transport_list[1].set_speed(20)

for transport in transport_list:
    transport.move()
    print(f"Скорость: {transport.get_speed()} км/ч\n")