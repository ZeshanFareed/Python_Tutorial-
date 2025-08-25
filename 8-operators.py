#---------------------Python Arithmetic Operators-------------------------

# Addition
x = 5
y = 3
print(x + y)


# Subtraction
x = 5
y = 3
print(x - y)


# Multiplication
x = 5
y = 3
print(x * y)


# division
x = 5
y = 3
print(x / y)


# Modulus
x = 5
y = 3
print(x % y)


print()
print()
#---------------------Python Assignment Operators-------------------------

s = 5
print(s)

# s = s + 3
# print(s)


# or same as below
s += 3
print(s)


s -= 2
print(s)



print()
print()
#---------------------Python Comparison Operators-------------------------

# Equal
x = 5
y = 3
print(x == y)


# Not Equal
x = 5
y = 3
print(x != y)


# Greater than
x = 5
y = 3
print(x > y)


# less than
x = 5
y = 3
print(x < y)


# Greater than or equal to
x = 5
y = 3
print(x >= y)


# less than or equal to
x = 5
y = 3
print(x <= y)

print()
print()
#---------------------Python Logical Operators-------------------------


z = 5
print(z == 5 and z > 4)  # and
print(z < 5 or z > 4)    # or
print(not(x > 3 and x > 10))  # not


print()
print()
#---------------------Python Membership Operators-------------------------

# in operator
name = "My name is Xeeshan"
print("zeeshan" in name)

# not in operator
name = "My name is Xeeshan"
print("zeeshan" not in name)

l = [20, 30, 21, 15]
print(15 in l)



print()
print()
#---------------------Python Identity Operators-------------------------

# is operator
w = 10
m = 10
print(w is m, w==m)


# is not operator
w = 10
m = 5
print(w is not m, w!=m)


print()
print()
#---------------------Python Bitwise Operators-------------------------

# & (AND) operator
d = 10
f = 2
print(bin(d))
print(bin(f))
print(d & f, bin(d&f))

print()
# | (OR) operator
d = 10
f = 2
print(bin(d))
print(bin(f))
print(d | f, bin(d|f))


print()
# ~ (XOR) operator formula is  -(n + 1)
d = 10
f = 2
print(bin(d))
print(bin(f))
print(~d, bin(~d))
print(~f, bin(~f))
