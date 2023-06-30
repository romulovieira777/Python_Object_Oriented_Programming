from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        print("Driving a car")


class Truck(Vehicle):
    def drive(self):
        print("Driving a truck")


automobile = Car()
automobile.drive()
