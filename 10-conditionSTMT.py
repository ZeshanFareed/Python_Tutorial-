
#----------------------IF Statement-----------------------

value = int(input("Enter Value : "))
if value % 2 == 0:
    print("Number is Even")
    
    
#----------------------IF ELSE Statement-----------------------

value = int(input("Enter Value : "))
if value % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")
    
    
    
#----------------------IF ELSE Statement-----------------------

value = int(input("Enter Value : "))
if value > 0:
    print("Number is Positive")
elif value < 0:
    print("Number is Negative")
else:
    print("Number is Zero")


#----------------------Another Example-----------------------

value = int(input("Enter Value : "))
if value >= 24 and value <=32:
    print("Your Grade is D")
elif value >= 33 and value <=37:
    print("Your Grade is C")
elif value >= 38 and value <=47:
    print("Your Grade is B")
elif value >= 48 and value <=60:
    print("Your Grade is A")
else:
    print("Grade is fail")



#----------------------Nested IF-----------------------

bill = int(input("Enter number : "))
if bill >= 2000:
    if bill <= 5000:
        print("20% Discount")
    else:
        print("10% Discount")
else:
    print("No Discount")