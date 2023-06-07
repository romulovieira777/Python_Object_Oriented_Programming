class Vehicle:
    speed = 100
    color = 'Red'

    def start(self):
        print('Starting engine...')

    def stop(self):
        print('Stopping engine...')


class Car(Vehicle):
    wheels = 4


class Motorbike(Vehicle):
    wheels = 2

    def accelerate(self):
        print('Accelerating...')


obj = Motorbike()
obj.start()
obj.stop()
obj.accelerate()
