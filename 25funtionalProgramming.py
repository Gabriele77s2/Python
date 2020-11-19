# Lambda
s=lambda x:x*x
s(2) # 4

# Map
name_lengths = map(len, ["Mary", "Isla", "Sam"])
print(name_lengths) # [4, 4, 3]

# Reduce
total = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
print(total) # 10

# Filter
arr=[1,2,3,4,5,6]
[i for i in filter(lambda x:x>4,arr)] # outputs[5,6]

# Decorators @
# This simplest decorator does nothing to the function being decorated. Such
# minimal decorators can occasionally be used as a kind of code markers.
def super_secret_function(f):
    return f

@super_secret_function
def my_function():
    print("This is my secret function.")

def disabled(f):
    """
    This function returns nothing, and hence removes the decorated function
    from the local scope.
    """
    pass

@disabled
def my_function():
    print("This function can no longer be called...")

my_function()
# TypeError: 'NoneType' object is not callable

#This is the decorator
def print_args(func):
    def inner_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs) #Call the original function with its arguments.
    return inner_func

@print_args
def multiply(num_a, num_b):
    return num_a * num_b

print(multiply(3, 5))
#Output:
# (3,5) - This is actually the 'args' that the function receives.
# {} - This is the 'kwargs', empty because we didn't specify keyword arguments.
# 15 - The result of the function.

# Decorator class
class Decorator(object):
    """Simple decorator class."""
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print('Before the function call.')
        res = self.func(*args, **kwargs)
        print('After the function call.')
        return res

@Decorator
def testfunc():
    print('Inside the function.')

testfunc()
# Before the function call.
# Inside the function.
# After the function call.

# Class Decorators only produce one instance for a specific function so decorating a method with a
# class decorator will share the same decorator between all instances of that class:
from types import MethodType
class CountCallsDecorator(object):
    def __init__(self, func):
        self.func = func
        self.ncalls = 0 # Number of calls of this method
    def __call__(self, *args, **kwargs):
        self.ncalls += 1 # Increment the calls counter
        return self.func(*args, **kwargs)
    def __get__(self, instance, cls):
        return self if instance is None else MethodType(self, instance)

class Test(object):
    def __init__(self):
        pass

    @CountCallsDecorator
    def do_something(self):
        return 'something was done'

a = Test()
a.do_something()
a.do_something.ncalls # 1
b = Test()
b.do_something()
b.do_something.ncalls # 2

# Decorator with arguments
def decoratorfactory(message):
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            print('The decorator wants to tell you: {}'.format(message))
            return func(*args, **kwargs)
        return wrapped_func
    return decorator

@decoratorfactory('Hello World')
def test():
    pass

test()
# Hello World!

# Decorator classes
def decoratorfactory(*decorator_args, **decorator_kwargs):
    class Decorator(object):
        def __init__(self, func):
            self.func = func
        def __call__(self, *args, **kwargs):
            print('Inside the decorator with arguments {}'.format(decorator_args))
            return self.func(*args, **kwargs)
    return Decorator

@decoratorfactory(10)
def test():
    pass

test()
# 10
