# Number Guessing game in python using Random Module 

import random
comp_number = random.randrange(1,101)

UserInput = int(input("Enter Your Number :-> "))

if UserInput > comp_number:
    print("Computer number is ", comp_number)
    print("Your guessing No is too High")
    
elif UserInput < comp_number:
    print("Computer number is ", comp_number)
    print("Your guessing No is too Low")
    
else:
    print("Computer number is ", comp_number)
    print("Your guessing No is Equal")