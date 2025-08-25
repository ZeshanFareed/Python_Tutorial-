# Tuples are unchangeable, meaning that you cannot change, add, 
# or remove items once the tuple is created.

# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y= list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)



print()
# Since tuples are immutable, they do not have a built-in append() method,
# but there are other ways to add items to a tuple.

# Convert the tuple into a list, add "orange", and convert it back into a tuple
x = ("apple", "banana", "cherry")
y= list(x)
y.append('orange')
x = tuple(y)
print(x)


print()
# Create a new tuple with the value "orange", and add that tuple:
x = ("apple", "banana", "cherry")
z = ("orange",)
x = x + z
print(x)


print()
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
x = ("apple", "banana", "cherry")
y = list(x)
y.remove("banana")
z = tuple(y)
print(z)



print()
# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
