# Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)



print()
# join list with append 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list1:
    list2.append(x)
print(list2)



print()
# join list with 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)