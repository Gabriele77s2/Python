def greet():
    print("Hello")
greet()
# Out: Hello

def greet_two(greeting):
    print(greeting)
greet_two("Howdy")
# Out: Howdy

def greet_two(greeting="Howdy"):
    print(greeting)
greet_two()
# Out: Howdy

def many_types(x):
    if x < 0:
        return "Hello!"
    else:
        return 0
print(many_types(1))
print(many_types(-1))
# Output:
# 0
# Hello!

def func(*args):
    # args will be a tuple containing all values that are passed in
    for i in args:
        print(i)

func(1, 2, 3) # Calling it with 3 arguments
# Out: 1
# 2
# 3

list_of_arg_values = [1, 2, 3]
func(*list_of_arg_values) # Calling it with list of values, * expands the list
# Out: 1
# 2
# 3
func() # Calling it without arguments
# No Output

def func(**kwargs):
    # kwargs will be a dictionary containing the names as keys and the values as values
    for name, value in kwargs.items():
        print(name, value)

func(value1=1, value2=2, value3=3) # Calling it with 3 arguments
# Out: value1 1
# value2 2
# value3 3
func() # Calling it without arguments
# No Out put
my_dict = {'foo': 1, 'bar': 2}
func(**my_dict) # Calling it with a dictionary
# Out: foo 1
# bar 2

def make(action='nothing'):
    return action

make("fun")
# Out: fun
make(action="sleep")
# Out: sleep
# The argument is optional so the function will use the default value if the argument is not passed in.
make()
# Out: nothing

def f(a, b=42, c=[]):
    pass
print(f.__defaults__)
# Out: (42, [])

# Immutable: Integers, strings, tuples, and so on. All operations make copies.
# Mutable: Lists, dictionaries, sets, and so on. Operations may or may not mutate.
x = [3, 1, 9]
y = x
x.append(5) # Mutates the list labelled by x and y, both x and y are bound to [3, 1, 9]
x.sort() # Mutates the list labelled by x and y (in-place sorting)
x = x + [4] # Does not mutate the list (makes a copy for x only, not y)
z = x # z is x ([1, 3, 9, 4])
x += [6] # Mutates the list labelled by both x and z (uses the extend function).
x = sorted(x) # Does not mutate the list (makes a copy for x only).
print(x)
# Out: [1, 3, 4, 5, 6, 9]
print(y)
# Out: [1, 3, 5, 9]
print(z)
# Out: [1, 3, 5, 9, 4, 6]

# Return values
def give_me_five():
    return 5

print(give_me_five()) # Print the returned value
# Out: 5
num = give_me_five()
print(num) # Print the saved returned value
# Out: 5
print(give_me_five() + 10)
# Out: 15

def give_me_another_five():
    return 5
    print('This statement will not be printed. Ever.')

print(give_me_another_five())
# Out: 5

def give_me_two_fives():
    return 5, 5 # Returns two 5

first, second = give_me_two_fives()
print(first)
# Out: 5
print(second)
# Out: 5

# Closure
def makeInc(x):
    def inc(y):
        # x is "attached" in the definition of inc
        return y + x
    return inc

incOne = makeInc(1)
incFive = makeInc(5)
incOne(5) # returns 6
incFive(5) # returns 10

# Nested
def fibonacci(n):
    def step(a,b):
        return b, a + b
    a, b = 0, 1
    for i in range(n):
        a, b = step(a, b)
    return a

def make_adder(n):
    def adder(x):
        return n + x
    return adder

add5 = make_adder(5)
add6 = make_adder(6)
add5(10)
#Out: 15
add6(10)
#Out: 16

def repeatedly_apply(func, n, x):
    for i in range(n):
        x = func(x)
    return x

repeatedly_apply(add5, 5, 1)
#Out: 26

# Recursive
def factorial(n):
    #n here should be an integer
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

factorial(0)
#out 1
factorial(1)
#out 1
factorial(2)
#out 2
factorial(3)
#out 6

# Defining a function with arguments
def divide(dividend, divisor): # The names of the function and its arguments
    # The arguments are available by name in the body of the function
    print(dividend / divisor)

divide(10, 2)
# output: 5
divide(divisor=2, dividend=10)
# output: 5

# Defining a function with multiple arguments
def func(value1, value2, optionalvalue=10):
    return '{0} {1} {2}'.format(value1, value2, optionalvalue1)

print(func(1, 'a', 100))
# Out: 1 a 100
print(func('abc', 14))
# abc 14 10
print(func('This', optionalvalue='StackOverflow Documentation', value2='is'))
# Out: This is StackOverflow Documentation

# Defining functions with list arguments
def func(myList):
    for item in myList:
        print(item)

func([1,2,3,5,7])
# 1
# 2
# 3
# 5
# 7

aList = ['a','b','c','d']
func(aList)
# a
# b
# c
# d
