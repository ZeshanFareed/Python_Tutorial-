# Remove Specified Item
item_list = ["imran", "xeeshan", "eisa", "dani"]
item_list.remove("xeeshan")
print(item_list)



print()
# remove the First Occurance
item_list = ["imran", "xeeshan", "eisa", "dani","xeeshan"]
item_list.remove("xeeshan")
print(item_list)


print()
# the pop() method removes the last item.
thislist = ["apple", "banana", "grapes", "cherry"]
thislist.pop()
print(thislist)



print()
# The pop() method removes the specified index.
thislist = ["apple", "banana", "grapes", "cherry"]
thislist.pop(1)
print(thislist)



print()
# The del keyword also removes the specified index:
thislist = ["apple", "banana", "grapes", "cherry"]
del thislist[2]
print(thislist)



print()
# also delete the entire list
thislist = ["apple", "banana", "cherry"]
del thislist



print()
# The clear() method empties the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


