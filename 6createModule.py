# List of default function
print(dir(__builtins__))
# Output: All list

# To know the functionally of any function
help(max)
# Output: Help on built-in function max in module __builtin__:
#         max(...)
#           max(iterable[, key=func]) -> value
#           max(a, b, c, ...[, key=func]) -> value
#           With a single iterable argument, return its largest item.
#           With two or more arguments, return the largest argument.

import math
print(math.sqrt(16))
# Output: 4.0

print(dir(math))
# Output: All list

print(math.__doc__)
# Output: This module is always available.
#         It provides access to the mathematical functions defined by the C standard

# Define a class
class MyClassObject(object):
    pass

# Print default functions
print(dir(MyClassObject))
# Output: All list

# Import a function from 'hello.py'
import hello
hello.say_hello()
# Output: hello

# Import a specific function
from hello import print_ciao
print_ciao()

# Modules can be aliased
import hello as hi
hi.say_hello()

# Modules can be stand-alone runnable script
if __name__ == '__main__':
    from hello import say_hello
    say_hello()
