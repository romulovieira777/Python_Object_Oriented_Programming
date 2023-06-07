class Engine:
    gears = 1


class Vehicle:
    speed = 100
    color = 'Red'


class Car(Vehicle, Engine):
    wheels = 4


class Motorbike(Vehicle, Engine):
    wheels = 2


obj = Motorbike()
print(obj.speed)
print(obj.gears)
print(obj.color)
