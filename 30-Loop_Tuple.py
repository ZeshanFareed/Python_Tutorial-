# Iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
    
    
    
print()
# Use the range() and len() functions to create a suitable iterable.
thistuple = ("apple", "banana", "cherry")
for x in range(len(thistuple)):
    print(thistuple[x])
    

print()
# Print all items, using a while loop to go through all the index numbers:
thistuple = ("apple", "banana", "cherry")
len = len(thistuple)
i = 0
while i < len:
  print(thistuple[i])
  i = i + 1