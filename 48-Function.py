# Function ek aisa block (hissa) hota hai code ka jo koi kaam (task) karta hai.
# Jab bhi humein woh kaam chahiye hota hai,
# hum sirf function ka naam likh kar use chala lete hain.


# creating a function 
def myfunction():
    print("Hey Xeeshan")
    
    
# calling a function
myfunction()



print()
# Information can be passed into functions as arguments.
def my_function(name):
    print("Hey", name)
    
my_function("Imran")
my_function("Eisa")
my_function("Dani")



print()
# This function expects 2 arguments, and gets 2 arguments:
def functionName(F_Name, L_Name):
    print(F_Name , L_Name)
    
functionName("Xeeshan", "Fareed")



print()
# If the number of arguments is unknown, add a * before the parameter name:
# Jab aap * lagate ho parameter ke aagay, jaise *boys,
# to Python sab values ko ek tuple mein daal deta hai.

def my_function(*boys):
  print("The youngest child is " + boys[-1])

my_function("Xeeshan", "Imran", "Eisa")



print()
# Another Example
def shopping_cart(*items):
    print("You added", len(items), "items to the cart.")
    print("First item:", items[0])
    print("Last item:", items[-1])

shopping_cart("Milk", "Bread", "Eggs")




print()
# You can also send arguments with the key = value syntax.
def my_function(child3, child1, child2):
    print("The beautiful child is",child3)
    
my_function(child1 = "Imran", child2 = "Eisa", child3 = "Dani")



print()
# If the number of keyword arguments is unknown,
# add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is ", kid["lname"])

my_function(fname = "Xeeshan", lname = "Fareed")



print()
# Default Parameter Value
def my_function(country = "Pakistan"):
  print("I am from", country)
  
my_function("China")
my_function()
my_function("Brazil")



print()
#  if you send a List as an argument
def print_order(items):
    for item in items:
        print("You ordered:", item)

my_items = ["Pizza", "Burger", "Fries"]
print_order(my_items)




print()
# Jab koi function koi result nikaalta hai aur aap us result ko baad mein use karna chahte ho — 
# to aap return ka use karte ho.
def add(a,b):
    return a + b

result = add(2,3)
print(result)




print()
# another example
def multiply(a):
    return a * 5
 
print(multiply(2))



print()
#  a function can have only positional arguments, add , / after the arguments:
def multiply(x , /):
    print(x)
 
multiply(3)



print()
# Keyword-Only Arguments
def my_function(*, x):
  print(x)

my_function(x = 3)



print()
# Any argument before the / , are positional-only,3
# and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)




print()
# Recursion Is mein function khud ko repeatedly call karta hai jab tak
# koi end condition (base case) na mil jaye.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(3)




# tri_recursion(3)
# = 3 + tri_recursion(2)

# tri_recursion(2)
# = 2 + tri_recursion(1)

# tri_recursion(1)
# = 1 + tri_recursion(0)

# tri_recursion(0)
# = 0   ← base case
