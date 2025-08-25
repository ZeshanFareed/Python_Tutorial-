'''
abs() in Python:
abs() ek built-in function hai jo kisi number ka absolute value return karta hai.
Agar number positive hai → wohi number return hoga.
Agar number negative hai → uska positive version return hoga.
'''
x = 5
y = 10

result = abs(x -y)
print(result)



print()
'''
all() in Python: AND
all() ek built-in function hai jo iterable (list, tuple, set, etc.) check karta hai.
Agar saray elements True hain → True return karega.
Agar koi ek bhi False ho → False return karega.
Agar iterable empty ho → True return karega.
'''
# Example 1: List of booleans

l = [True, True, True]
print(all(l))

l1 = [True, False, True]
print(all(l1))


# Example 2: Numbers
# Python mein 0 = False aur non-zero = True
l = [0, 1, 3]
print(all(l))

l = [2, 1, 3]
print(all(l))


# Example 3: Strings
# Empty string = False, non-empty string = True
print(all(["Ali", "Sara", ""]))   
print(all(["Ali", "Sara", "Ahmed"]))



'''
any() in Python: OR
any() bhi ek built-in function hai jo iterable (list, tuple, set, etc.) check karta hai.
Agar koi ek element bhi True ho → True return karega.
Agar saray elements False ho → False return karega.
Agar iterable empty ho → False return karega.
'''
print(any([False, False, True]))   # True (kyunki ek True hai)
print(any([False, False, False]))  # False (sab False)

print(any([0, 0, 5]))    # True (5 non-zero hai)
print(any([0, 0, 0]))    # False (sab 0 hain)

print(any(["", "", "Hello"]))   # True (ek string non-empty hai)
print(any(["", "", ""]))        # False (sab empty strings)




# text = "Python ♥"
# print(ascii(text))   Output: 'Python \u2665'




print()
'''
bin() Function in Python
bin() ka kaam hota hai kisi integer ko binary string me convert karna.
'''
print(bin(5))  
print(bin(10))  
print(bin(255)) 

# 10 / 2 = 5 reminder 0
# 5 / 2 = 2 reminder 1
# 2 / 2 = 1 reminder 0
# 1 / 2 = 0 reminder 1
# count from end 1010




print()
'''
bytearray() kya karta hai?
Python mein bytearray() ek list jaisa box banata hai jisme sirf bytes (0–255 numbers) rakhe ja sakte hain.
Ye mutable hai → matlab aap iske andar values change kar sakte ho.
bytes -> immutable hota hy
'''
# Example 1: Simple banate hain
arr = bytearray([65, 66, 67])
print(arr)
print(arr.decode())
# 👉 65 = A, 66 = B, 67 = C (ASCII codes).

# Example 3: Change karna
arr = bytearray(b"HI")
arr[0] = 65
print(arr)
print(arr.decode())




print()
'''
callable() in Python:
callable() ek built-in function hai.
Ye check karta hai ke koi object function ki tarah call ho sakta hai ya nahi.
Agar object ko () (brackets) laga kar call kar sakte ho → True.
Agar call nahi kar sakte → False.
'''
# Example 1: Normal function
def hello():
    return "HI"

print(callable(hello))  
print(callable(5)) 


print()
# Example 2: Class

class MyClass:
    pass

print(callable(MyClass))  
obj = MyClass()            # yeh call hai
print(callable(obj)) # False (object ko call nahi kar sakte)




print()
# Example 3: Special __call__ method

# Agar class ke andar __call__ method likh do, 
# to uska object bhi callable ban jaata hai:
class MyClass:
    def __call__(self):
        return "Object called!"


print(callable(MyClass))  
obj = MyClass()          
print(callable(obj))    # True (kyunki __call__ hai)



'''
chr() in Python:
chr() ek built-in function hai.
Ye ek number (Unicode code point) ko uska character bana deta hai.
'''
print(chr(65))   # A
print(chr(66))   # B
print(chr(97))   # a
print(chr(36))   # $
print(chr(64))   # @
print(chr(35))   # #
print(chr(8364))   # €
print(chr(128512)) # 😀




'''
classmethod() in Python:
classmethod() ek built-in decorator hai (@classmethod).
Ye function ko class se bind karta hai, object se nahi.
Matlab: is method ko class ke through bhi call kar sakte ho, aur object ke through bhi.
Pehla parameter hamesha cls hota hai (class ko represent karta hai), jaise self object ko karta hai.
'''

class Student:
    school = "ABC School"
    
    def __init__(self,name):
        self.name = name
     
    # normal method   
    def show(self):
         return f"Student: {self.name}, School: {Student.school}"
     
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
        
        
s1 = Student("Ali")
print(s1.show())   # Student: Ali, School: ABC School

# Class method call through class
Student.change_school("XYZ School")

print(s1.show())   # Student: Ali, School: XYZ School





print()
'''
compile() in Python:
compile() ek built-in function hai.
string code ko Python ke samajhne layak banata hai (bytecode).
Bytecode wo hota hai jo Python internally run karta hai.
compile(source, filename, mode)
mode → teen options hote hain:

"exec" → multiple lines of code (statements)
"eval" → single expression
"single" → single interactive statement (jaise Python shell input).
'''

# Example 1: Using "eval"
x = 5
code = "x + 10"
compiled = compile(code, "", "eval")
print(eval(compiled)) 


# Example 2: Using "exec"
code = """
for i in range(3):
    print("Hello", i)
"""
compiled = compile(code, "", "exec")
exec(compiled)


# Example 3: Using "single"
code = "print('Hi!')"
compiled = compile(code, "", "single")
exec(compiled)









