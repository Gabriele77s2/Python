# List of keyword
import keyword
print(keyword.kwlist)

# Integer
a = 2
print(a)
# Output: 2

# Integer
b = 9223372036854775807
print(b)
# Output: 9223372036854775807

# Floating point
pi = 3.14
print(pi)
# Output: 3.14

# String
c = 'A'
print(c)
# Output: A

# String
name = 'John Doe'
print(name)
# Output: John Doe

# Boolean
q = True
print(q)
# Output: True

# Empty value or null data type
x = None
print(x)
# Output: None

0 = x
# Output: SyntaxError: can't assign to literal

x = True # valid
_y = True # valid
9x = False # starts with numeral
# Output: SyntaxError: invalid syntax
$y = False # starts with symbol
# Output: SyntaxError: invalid syntax

has_0_in_it = "Still Valid"
print("has_0_in_it")
# Output: Still Valid

# Case sensitive
x = 9
y = X*5
# Output: NameError: name 'X' is not defined

a = 2
print(type(a))
# Output: <type 'int'>

b = 9223372036854775807
print(type(b))
# Output: <type 'int'>

pi = 3.14
print(type(pi))
# Output: <type 'float'>

c = 'A'
print(type(c))
# Output: <type 'str'>

name = 'John Doe'
print(type(name))
# Output: <type 'str'>

q = True
print(type(q))
# Output: <type 'bool'>

x = None
print(type(x))
# Output: <type 'NoneType'>

a, b, c = 1, 2, 3
print(a, b, c)
# Output: 1 2 3

a, b, c = 1, 2
# Output: Traceback (most recent call last):
#         File "name.py", line N, in <module>
#         a, b, c = 1, 2
#         ValueError: need more than 2 values to unpack

a, b = 1, 2, 3
# Output: Traceback (most recent call last):
#         File "name.py", line N, in <module>
#         a, b = 1, 2, 3
#         ValueError: too many values to unpack

a, b, _ = 1, 2, 3
print(a, b)
# Output: 1, 2

a, b, _ = 1, 2, 3, 4
# Output: Traceback (most recent call last):
#         File "name.py", line N, in <module>
#         a, b, _ = 1, 2, 3, 4
#         ValueError: too many values to unpack (expected 3)

a = b = c = 1   # all three names a, b and c refer to same int object with value 1
print(a, b, c)
# Output: 1 1 1
b = 2           # b now refers to another int object, one with a value of 2
print(a, b, c)
# Output: 1 2 1 # so output is as expected.

name = input("What is your name? ")
# Output: What is your name? Gabriele
print(name)
# Output: Gabriele

x = input("Write a number: ")
# Output: Write a number: 10
print(x / 2)
# Output: TypeError: unsupported operand type(s) for /: 'str' and 'int'
print(float(x) / 2)
# Output: 5.0
