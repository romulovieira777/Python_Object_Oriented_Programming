class Vehicle:
    def drive(self):
        print('Superclass drive!')


class Car(Vehicle):
    wheels = 4
    speed = 100

    def drive(self):
        print('Driving')


obj = Car()
obj.drive()
