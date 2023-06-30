import pickle
from ducke import *


with open("dump.bin") as f:
    obj = pickle.load(f)
    print(obj.name)
    print(obj.quack)
