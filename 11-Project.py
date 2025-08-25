#-------------------------Simple Calculator Project-------------------#

num1 = int(input("Enter Your Number : "))
num2 = int(input("Enter Your Number :"))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

submit = input("You want to add, sub, mul, div : ")

if submit == "add":
    print("Addition is ", add)
elif submit == "sub":
    print("Subtraction is ", sub)
elif submit == "mul":
    print("Multiplication is ", mul)
elif submit == "div":
    print("Division is ", div)
else:
    print("Your Input is not Correct")