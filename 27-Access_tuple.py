# Acess The Tupple Item

# Print the second item in the tuple:
thistuple = ("xeeshan", "rooshiii", "imran")
print(thistuple[1])


print()
# Print the second item in the tuple:
thistuple = ("xeeshan", "rooshiii", "imran")
print(thistuple[-1])


print()
# Return the third, fourth, and fifth item:
thistuple =thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])



print()
# This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


print()
# This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


print()
# This example returns the items from index -4
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


print()
# Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")