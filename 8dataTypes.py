# Boolean
x or y  # if x is False then y otherwise x
x and y # if x is False then x otherwise y
not x   # if x is True then False, otherwise True

# A boolean is also an int . The bool type is a subclass of the int type and True and False are its only instances
issubclass(bool, int)   # True
isinstance(True, bool)  # True
isinstance(False, bool) # True

True + False == 1   # 1 + 0 == 1
True * True == 1    # 1 * 1 == 1

# Numbers
# Integers
a = 2
b = 100
c = 123456789
d = 38563846326424324

# Float
a = 2.0
b = 100.e0
c = 123456789.e1

# Complex
a = 2 + 1j
b = 100 + 10j

# Strings
# Reversed
a = reversed('hello')
# Output: <reversed object at 0x7f5df5348790>


# Tuples, supports indexing; immutable; hashable if all its members are hashable
# Hashable = An object is hashable if its value never changes during its lifetime
a = (1, 2, 3)
b = ('a', 1, 'python', (1, 2))
b[2] = 'something else' # returns a TypeError

# Lists, not hashable; mutable
a = [1, 2, 3]
b = ['a', 1, 'python', (1, 2), [1, 2]]
b[2] = 'something else'                 # Allowed

# Set, hashable
a = {1, 2, 'a'}

# Dictionaries, keys hashable
a = {1: 'one',
     2: 'two'}
b = {'a': [1, 2, 3],
     'b': 'a string'}

# Testing type of variables
a = '123'
print(type(a))
# Output: <class 'str'>

b = 123
print(type(b))
# Output: <class 'int'>

# In conditional statements it is possible to test the datatype with isinstance (not encouraged)
i = 7
if isinstance(i, int):
    i += 1
elif isinstance(i, str):
    i = int(i)
    i += 1

# NoneType
x = None
if x is None:
    print('Not a surprise, I just defined x as None.')

# Converting between datatypes
a = '123'
b = int(a)

a = '123.456'
b = float(a)
c = int(a)    # ValueError: invalid literal for int() with base 10: '123.456'
d = int(b)    # 123

a = 'hello'
list(a)   # ['h', 'e', 'l', 'l', 'o']
set(a)    # {'o', 'e', 'l', 'h'}
tuple(a)  # ('h', 'e', 'l', 'l', 'o')

# Mutable and Immutable Data Type
def f(m):
    m.append(3) # adds a number to the list. This is a mutation.
x = [1, 2]
f(x)
x == [1, 2] # False now, since an item was added to the list

def bar():
x = (1, 2)
g(x)
x == (1, 2) # Will always be True, since no function can change the object (1, 2)

# Examples of mutable Data Types:
# bytearray
# list
# set
# dict

# Examples of immutable Data Types:
# int , long , float , complex
# str
# bytes
# tuple
# frozenset

# String data type
a_str = 'Hello World'
print(a_str)
# Output: Hello World
print(a_str[0])
# Output: H
print(a_str[0:5])
# Output: Hello

# Set data types
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # duplicates will be removed
# Output: {'pear', 'apple', 'orange', 'banana'}

a = set('abracadabra')
print(a) # unique letters in a
# Output: {'a', 'r', 'b', 'c', 'd'}

a.add('z')
print(a)
# Output: {'a', 'c', 'r', 'b', 'z', 'd'}

# Numbers data type
int_num = 10
float_num = 10.2
complex_num = 3.14j
long_num = 1234567

# List data type
list = [123, 'abcd', 10.2, 'd']
list1 = ['hello', 'world']
print(list)
# Output: [123, 'abcd', 10.2, 'd']
print(list[0:2])
# Output: [123, 'abcd']
print(list1 * 2)
# Output: ['hello', 'world', 'hello', 'world']
print(list + list1)
# Output: [123, 'abcd', 10.2, 'd', 'hello', 'world']

# Dictionary data type
dic = {'name':'red', 'age':10}
print(dic)
# Output: {'name':'red', 'age':10}
print(dic['name'])
# Output: red
print(dic.values())
# Output: dict_values(['red',10])
print(dic.keys())
# Output: dict_keys(['name','age'])

# Tuple data type
tuple = (123, 'hello')
print(tuple)
# Output: (123, 'hello')
print(tuple[0])
# Output: 123
