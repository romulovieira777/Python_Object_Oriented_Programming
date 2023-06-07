class Vehicle:
    __speed = 5

    def getSpeed(self):
        return self.__speed

    def setSpeed(self, speed):
        self.__speed = speed


obj = Vehicle()
obj.setSpeed(10)
print(obj.getSpeed())
