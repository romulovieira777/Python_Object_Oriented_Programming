import pickle
from ducke import *


obj = Duck("Bob", "Quack 1")

bin_file = open("dump.bin", mode="wb")
dump = pickle.dump(obj, bin_file)
bin_file.close()
