# maximun number by max function
list = [15, 10, 12, 88, 22]
m = max(list)
print(m)


print()
# maximun string by max function
names  = ["balouch", "Xeeshan", "Ali"]
list = [name.lower() for name in names]
m = max(list)
print(m)


print()
# maximun number by max function
list = [15, 10, 12, 88, 22]
m = min(list)
print(m)


print()
# maximun string by max function
names  = ["balouch", "Xeeshan", "Ali"]
list = [name.lower() for name in names]
m = min(list)
print(m)


print()
# find the third largest number
list = [222, 10, 32, 36, 1 , 33]
list.sort(reverse=True)
print(list)
third_largest = list[2]
print(third_largest)



print()
# 2nd method to find third largest number
list = [222, 10, 32, 36, 1 , 33]
list.sort()
list.reverse()
third_largest = list[2]
print(third_largest)



#  find index of any given in the list
l = [15, 10, 12, 88, 22]
index = l.index(88)
print(index)