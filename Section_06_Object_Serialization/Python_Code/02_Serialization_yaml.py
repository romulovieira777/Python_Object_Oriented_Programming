import ruamel.yaml


class Thing:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type


obj = Thing("Bottle", 1.25, "Product")

# save obj
s = ruamel.yaml.dump(obj)

with open("../Files/obj.yaml", "wb") as fobj:
    fobj.write(s.encode())

# load obj
data = b""

with open("../Files/obj.yaml", "rb") as fobj:
    data = fobj.read()

deserializedObj = ruamel.yaml.load(data, Loader=ruamel.yaml.Loader)
print(deserializedObj.name)
print(deserializedObj.price)
print(deserializedObj.type)
