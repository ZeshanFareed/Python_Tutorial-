# Loop Through a List
list = ["xeeshan", "fareed", "khan"]
for i in list:
    print(i)
    
print()
# through indexing or length   
list = ["xeeshan", "fareed", "khan"]
t = len(list)
for i in range(t):
    print(list[i])
    
print()
# Print all items, using a while loop to go through all the index numbers
list = ["xeeshan", "fareed", "khan"]
i = 0
while i < len(list):
    print(list[i])
    i += 1



print()
#--------------------------------Example---------------------------
# Print only numbers greater than 10:
numbers = [5, 12, 7, 18, 3, 21]
for i in numbers:
    if i >= 10:
        print(i)
        
    
    
print()
# Count how many even numbers are in the list:
numbers = [2, 5, 8, 11, 14, 17, 20]   
count = 0 
for i in numbers:
    if i % 2 == 0:
        count = count + 1

print("Total even numbers:", count)


print()
# Make a new list of squares of each number:
numbers = [1, 2, 3, 4]
squares = []
for num in numbers:
    squares.append(num ** 2)
print(squares)



print()
# Print each element of a list in reverse order:
fruits = ["apple", "banana", "cherry"]
reversed = fruits[-1::-1]

for i in reversed:
    print(i)
    
    
print()
# Merge two lists into one (without duplicates):
list1 = [1, 2, 3]
list2 = [3, 4, 5]

merged = list1.copy()

for item in list2:
    if item not in merged:
        merged.append(item)

print(merged)



print()
# Ask the user to enter 5 numbers and store them in a list, then print the list.
# list = []

# for i in range(5):
#     user = int(input("Enter number " + str(i+1) + ": "))
#     list.append(user)
    
# print(list)




print()
# Check which names in a list start with a vowel.
names = ["Ali", "Umer", "Bilal", "Omer"]
vowels = ["a", "e", "i", "o", "u"]
list = []

for i in names:
     if i[0].lower() in vowels:
        list.append(i)
print(list)