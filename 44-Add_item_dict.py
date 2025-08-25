# Once a set is created, you cannot change its items, but you can add new items.

# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("pineapple")
print(thisset)



# To add items from another set into the current set, use the update() method.
# Add elements from tropical into thisset:
print()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)




# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
print()
thisset = {"apple", "banana", "cherry"}
tropical = ["mango", "papaya"]
thisset.update(tropical)
print(thisset)
