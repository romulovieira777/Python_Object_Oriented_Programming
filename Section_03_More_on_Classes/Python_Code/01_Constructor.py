class Bird:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fly(self):
        print("flying")

    def tweet(self):
        print("tweet")


parrot = Bird('Alice', 2)
pigeon = Bird('Bob', 3)
eagle = Bird('Ezy', 1)

eagle.tweet()
eagle.fly()

print(eagle.name)
print(pigeon.age)

pigeon.tweet()
eagle.fly()
