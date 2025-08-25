# The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(0, "watermelon")
print(thislist)
print(thislist[1])



print()
# Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "grapes")
print(thislist)


print()
# To add an item to the end of the list, use the append() method:
# append jiss type ka data hoga wesy he append kr deta hy
thislist = [10, 20, 30, 40]
list2 = (30, 40)
thislist.append(list2)
print(thislist)


print()
# To append elements from another list to the current list, use the extend() method.
# extend andar ka data pe kam krta hy na k data ki type pe

thislist = [10, 20, 30, 40]
list2 = [30, 40]
thislist.extend(list2)
print(thislist)



print()
# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thisTuple = ("mango", "pineapple")

thislist.extend(thisTuple)
print(thislist)



print()
# with set 
thislist = ["apple", "banana", "cherry"]
thisSet = {"mango", "pineapple"}

thislist.extend(thisSet)
print(thislist)
