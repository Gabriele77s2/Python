x = 1.55
y = -1.55

# round to the nearest integer
round(x) # 2
round(y) # -2

# the second argument gives how many decimal places to round to (defaults to 0)
round(x, 1) # 1.6
round(y, 1) # -1.6

# math is a module so import it first, then use it.
import math
# get the largest integer less than x
math.floor(x) # 1
math.floor(y) # -2

# get the smallest integer greater than x
math.ceil(x) # 2
math.ceil(y) # -1

# drop fractional part of x
math.trunc(x) # 1, equivalent to math.floor for positive numbers
math.trunc(y) # -1, equivalent to math.ceil for negative numbers

# round
round(1.3) # 1
round(1.33, 1) # 1.3
round(0.5) # 0
round(1.5) # 2
round(2.675, 2) # 2.67, not 2.68!

# pow
from math import pow
pow(5,5) # 3125.0
