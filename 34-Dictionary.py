# A dictionary is a collection which is ordered*,
# changeable and do not allow duplicates.
# Dictionaries are used to store data values in key:value pairs.
# written with curly brackets

thisdict = {
    "name" : "Xeeshan",
    "age" : 32,
    "height" : 6.1
}
print(thisdict)


print()
# Print the "brand" value of the dictionary:
thisdict = {
    "name" : "Xeeshan",
    "age" : 32,
    "height" : 6.1
}
print(thisdict['name'])



print()
# Duplicate values will overwrite existing values:
thisdict = {
    "name" : "Xeeshan",
    "age" : 32,
    "height" : 6.1,
    "name" : "rooshan"
    
}
print(thisdict)



print()
# Print the number of items in the dictionary:
this_dict = {
    "name" : "Xeeshan",
    "age" : 32,
    "height" : 6.1,
    "name" : "rooshan"
    
}
print(len(this_dict))



print()
# String, int, boolean, and list data types:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)



print()
# Print the data type of a dictionary:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict))


print()
# Using the dict() method to make a dictionary:
thisdict = dict(name = "xeeshan", age = 32, country = "pakistan")
print(thisdict)