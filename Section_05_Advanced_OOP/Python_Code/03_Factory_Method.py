class MyFacto0ry:
    def factory(self, type):
        if type == "Word":
            return Word()
        else:
            return PDF()


class Word:
    version = 1


class PDF:
    version = 2


theFactory = MyFacto0ry()
obj = theFactory.factory("PDF")
print(obj.version)
