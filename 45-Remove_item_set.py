# To remove an item in a set, use the remove(), or the discard() method.
# Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


# Remove "banana" by using the discard() method:
print()
thisset = {"apple", "banana", "cherry"}
thisset.discard("apple")
print(thisset)


# Remove a random item by using the pop() method:
print()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)



# The clear() method empties the set:
print()
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


# The del keyword will delete the set completely:
print()
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
