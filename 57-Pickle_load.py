import pickle

file = open("write_data.txt", "rb")
L = pickle.load(file)
print(L)
