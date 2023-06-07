class Vehicle:
    speed = 100


class Car(Vehicle):
    wheels = 4


class Motorbike(Vehicle):
    wheels = 2


obj = Motorbike()
print(obj.speed)
