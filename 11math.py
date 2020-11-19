# Division
a, b, c, d, e = 3, 2, 2.0, -3, 10
print(a / b)
# = 1.5
print(e / b)
# = 5.0
print(a // b)
# = 1
print(a // c)
# = 1.0

import operator
print(operator.truediv(a, b))
# = 1.5
print(operator.floordiv(a, b))
# = 1
print(operator.floordiv(a, c))
# = 1.0

# Addition
a, b = 1, 2
print(a + b)
# = 3
a += b      # a = a + b
print(a)
# 3

import operator
print(operator.add(a, b))
# = 5
a = operator.add(a, b)     # a = a + b
print(a)
# = 5

string = "first string " + "second string"
print(string)
# = 'first string second string'

list = [1, 2, 3] + [4, 5, 6]
print(list)
# = [1, 2, 3, 4, 5, 6]

# Subtraction
a, b = 1, 2
print(b - a)
# = 1
print(operator.sub(b, a))
# = 1

# Multiplication
a, b = 2, 3
print(a * b)
# = 6
print(operator.mul(a, b))
# = 6

string = 3 * 'ab'
print(string)
# = ababab
string = 3 * ('a', 'b')
print(string)
# = ('a', 'b', 'a', 'b', 'a', 'b')

# Modulus
print(3 % 4)
# = 3
print(10 % 2)
# = 0
print(6 % 4)
# = 2
print(operator.mod(3, 4))
# = 3
print(-9 % 7)
# = 5
print(9 % -7)
# = -5
print(-9 % -7)
# -2

quotient, remainder = divmod(9, 4)
print(quotient, remainder)
# 2 1

# Exponentation
a, b = 2, 3
print(a ** b)
# = 8
print(pow(a, b))
# = 8

import math
import cmath
c = 4
print(math.sqrt(c)) # always float
# = 2.0
print(cmath.sqrt(c)) # always complex
# = (2 + 0j)
print(math.pow(a, b))
# = 8.0

x = 8
print(math.pow(x, 1/3))
# = 2.0
print(x ** (1/3))
# = 2.0

import operator
print(operator.pow(a, b))
# = 8

a, b, c = 2, 3, 2
print(pow(a, b, c))     # (2 ** 3) % 2
# = 0

# Operator precedence
a, b, c, d = 2, 3, 5, 7
print(a ** (b + c))
# = 256
print(a * (b ** c))
# = 486
print(a * b ** c)
# = 486
print(a + b * c / d)
# = 4.142857142857142
