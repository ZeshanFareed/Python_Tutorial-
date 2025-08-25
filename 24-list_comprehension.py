l = []
for a in range(1,51):
    l.append(a)
print(l)


# or 
print()
n = [h for h in range(1,51) if h%2==0]
print(n)

print()
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)