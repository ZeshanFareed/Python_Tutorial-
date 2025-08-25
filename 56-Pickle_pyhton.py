'''
Pickle powerfull algorithm for 
serializing (store data into folder) or dump(), wb and 
deserializing (read data) or load(), rb

Storing Data with pickles
 Boolean , Integers
 Float  ,  Complex no
 tupple  ,  list
 Dictionaries , set
 
'''

import pickle

l = [10, 20, 30, 40]

file = open("write_data.txt", "wb")
pickle.dump(l, file)
file.close()