# stack is Linear ds work on FILO & LIFO 
# stack Operation
# 1- push -> insert the item 
# 2- pop -> remove the last item 
# 3- peek -> display the last item
# 4- dispaly -> display the whole list

l = []

while True:
    c = int(input('''
            1- Push the items
            2- Pop the item
            3- Peek the Item
            4- Display Stack 
            5- Exit
            
                '''))
    if c == 1:
        n = input("Enter the Value : ")
        l.append(n)
        print(l)
    elif c == 2:
        if len(l) == 0:
            print("Stack is Empty")
        else:
            p = l.pop()
            print(p)
            print(l)
    elif c == 3:
        if len(l) == 0:
            print("Stack is Empty")
        else:
            print("Last Element is : ", l[-1])
            print(l)
    elif c == 4:
        print("Display Stack : ", l)
    elif c == 5:
        break
    else:
        print("Inavlid Operation.....")