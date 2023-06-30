import jsonpickle


class Thing(object):
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type


obj = Thing("My Thing", 1.25, 'Product')

# save
s = jsonpickle.encode(obj)
encoded_data = s.encode('utf-8')

with open("../Files/thing.obj", "wb") as f:
    f.write(encoded_data)

# load
data = ""

with open("../Files/thing.obj", "rb") as fobj:
    data = fobj.readline()

decoded_data = data.decode('utf-8')
loadedObj = jsonpickle.decode(decoded_data)

print(loadedObj.name)
print(loadedObj.price)
print(loadedObj.type)
