# Queue is linear DS , store item in FIFO
# Queue Operations
# 1- Enqueue -> Add an item to the queue
# 2- Dequeue -> Remove an item from the queue
# 3- Front -> Get the Front item form the queue
# 4- Rear -> Get the last item from the queue



l = []

while True:
    c = int(input('''
            1- Enqueue the items
            2- Dequeue the item
            3- Front the Item
            4- Rear the Item
            5- Display Stack 
            6- Exit
            
                '''))
    if c == 1:
        n = input("Enter the Value : ")
        l.append(n)
        print(l)
    elif c == 2:
        if len(l) == 0:
            print("Queue is Empty")
        else:
            del l[0]
    elif c == 3:
        if len(l) == 0:
            print("Queue is Empty")
        else:
            print("First Element is : ", l[0])
            print(l)
    elif c == 4:
        if len(l) == 0:
            print("Queue is Empty")
        else:
            print("Last Element is : ", l[-1])
            print(l)
    elif c == 5:
        print("Display Queue : ", l)
    elif c == 6:
        break
    else:
        print("Inavlid Operation.....")


