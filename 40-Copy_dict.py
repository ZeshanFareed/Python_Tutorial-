# Make a copy of a dictionary with the copy() method:
thisdict = {
    "name" : "Xeeshan",
    "F_name" : "Fareed",
    "age" : 21
}
copydict = thisdict.copy()
print(copydict)


print()
# Another way to make a copy is to use the built-in function dict().
thisdict = {
    "name" : "Xeeshan",
    "F_name" : "Fareed",
    "age" : 21
}
copydict = dict(thisdict)
print(copydict)