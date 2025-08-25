# A set is a collection which is unordered, unchangeable*, and unindexed.
# Sets are written with curly brackets {}.
# do not allow duplicate values.

# Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)


print()
# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "banana"}
print(thisset)



print()
# The values True and 1 are considered the same value in sets,
# and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)


print()
# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, 0, 2}
print(thisset)


print()
# Get the number of items in a set:
thisset = {"apple", "banana", "cherry", "banana"}
print(len(thisset))


print()
# A set with strings, integers and boolean values:
set1 = {"xeeshan", 21, 32.1, True}
print(set1)


print()
# What is the data type of a set?
myset = {"xeeshan", 21, 32.1, True}
print(type(myset))


print()
# Using the set() constructor to make a set:
thiset = set(("xeeshan", 32, True))
print(thiset)
print(type(myset))