# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


print()
# The popitem() method removes the last inserted item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "red"
}
thisdict.popitem()
print(thisdict)


print()
# The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "red"
}

del thisdict["brand"]
print(thisdict)


print()
# The del keyword can also delete the dictionary completely:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict)  #this will cause an error because "thisdict" no longer exists.


print()
# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "red"
}

thisdict.clear()
print(thisdict)