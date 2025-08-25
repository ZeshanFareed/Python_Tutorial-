# You can access the items of a dictionary by referring to its key name

thisdict = {
  "name": "Xeeshan",
  "f_name": "fareed",
  "year": 2005
}
print(thisdict["f_name"])


print()
# There is also a method called get() that will give you the same result:
x = thisdict.get("name")
print(x)


print()
# The keys() method will return a list of all the keys in the dictionary.
y = thisdict.keys()
print(y)


print()
# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change



print()
# Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print("Before insert dict :-> ", car)

car["color"] = "black"
print("After insert dict :-> ", car)


print()
# Get a list of the key:value pairs
thisdict = {
  "name": "Xeeshan",
  "f_name": "fareed",
  "year": 2005
}
x = thisdict.items()
print(x)



print()
# Make a change in the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020
print(x) #after the change



print()
#
thisdict = {
  "brand": "Ford",
  "model1": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
else:
    print("Not in dictionary")
