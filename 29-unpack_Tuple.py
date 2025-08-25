# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

# packing a tupple 
fruits = ("apple", "banana", "cherry")


print()
# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, red, orange) = fruits
print(green)
print(orange)
print(red)


print()
# If the number of variables is less than the number of values, you can add an *
fruits = ("apple", "banana", "cherry", "grapes",  "papaya")
(green, red, *orange) = fruits
print(green)
print(red)
print(orange)



print()
# Add a list of values the "tropic" variable:
fruits = ("apple", "papaya", "banana", "cherry", "grapes")
(green, red, *tropic) = fruits
print(green)
print(tropic)
print(red)