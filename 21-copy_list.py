# You can use the built-in List method copy() to copy a list.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
new_list = thislist.copy()
print(new_list)


print()
# Make a copy of a list with the list() method:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
new_list = list(thislist)
print(new_list)



print()
# You can also make a copy of a list by using the : (slice) operator.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
new_list = thislist[:]
print(new_list)
