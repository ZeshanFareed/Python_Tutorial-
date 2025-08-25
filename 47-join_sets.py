# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.


# The union() method returns a new set with all items from both sets.
# Join set1 and set2 into a new set:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)



# You can use the | operator instead of the union() method, and you will get the same result.
print()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)


# Join multiple sets with the union() method:
print()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

set5 = set1.union(set2,set3,set4)
print(set5)



# When using the | operator, separate the sets with more | operators:
print()
set_5 = set1 | set2 | set3 | set4 
print(set_5)


# The union() method allows you to join a set with other data types, like lists or tuples.
print()
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.


# The intersection() method will return a new set, that only contains the items that are present in both sets.
print()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)



# Use & to join two sets:
print()
set3 = set1 & set2
print(set3)



# The values True and 1 are considered the same value. The same goes for False and 0.
print()
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
print(set3)



# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
print()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)



# You can use the - operator instead of the difference() method, and you will get the same result.
print()
set3 = set1 - set2
print(set3)



# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
print()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)


# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
print()
set3 = set1 ^ set2
print(set3)