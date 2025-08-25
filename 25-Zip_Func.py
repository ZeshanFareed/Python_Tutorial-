# do loop ko ik sath itrate krwany k leay zip function ka use krty hy
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

for a,b in zip(list1,list2):
    print(a,b)


print()
# jb dosri list k item zyada ho tb
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8, 9]
t = len(list2)

for h in range(t):
    print(list1[h],list2[h])