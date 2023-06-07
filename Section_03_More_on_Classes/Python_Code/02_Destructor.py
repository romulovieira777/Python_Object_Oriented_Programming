class Car:
    wheels = 4
    speed = 100

    def __init__(self):
        print("Constructor is called")

    def __del__(self):
        print("Destructor is called")


obj = Car()
del obj
print("Program is finished")
