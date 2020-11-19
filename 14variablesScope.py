# Nonlocal variables
def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer

c = counter()
print(c())
# = 1
print(c())
# = 2
print(c())
# = 3

# Local variables
x = 'Hi'

def change_local_x():
    x = 'Bye'
    print(x)

change_local_x()
# = Bye
print(x)
# = Hi

# Global variables
x = 'Hi'

def change_global_x():
    global x
    x = 'Bye'
    print(x)

change_global_x()
# = Bye
print(x)
# = Bye

# Difference between two local variables
def foo():
    if True:
        a = 5
    print(a) # ok

b = 3
def bar():
    if False:
        b = 5
    print(b) # UnboundLocalError: local variable 'b' referenced before assignment

# del
x = 5
print(x)
# = 5
del x       # delete the variable's scope
#print(x)    # NameError: name 'f' is not defined

class A:
    pass

a = A()
a.x = 7
print(a.x)
# = 7
del a.x
#print(a.x)      # error: AttributeError: 'A' object has no attribute 'x'

x = {'a': 1, 'b': 2}
del x['a']
print(x)
# = {'b': 2}
#print(x['a'])   # error: KeyError: 'a'

x = [0, 1, 2, 3, 4]
del x[1:3]
print(x)
# = [0, 3, 4]

# Global vs Local
foo = 1         # global
def func():
    bar = 2     # local
    print(foo)  # prints variable foo from global scope
    print(bar)  # prints variable bar from local scope
    print(globals().keys())     # prints all variable names in global scope
    print(locals().values())    # prints all variable names in local scope
print(func())
# = 1
#   2
#   dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'counter', 'c', 'change_local_x', 'change_global_x', 'foo', 'b', 'bar', 'A', 'a', 'x', 'func'])
#   dict_keys(['bar'])
#   None

foo = 1
def func():
    foo = 2     # creates a new variable foo in local scope, global foo is not affected
    print(foo)  # prints 2
    # global variable foo still exists, unchanged:
    print(globals()['foo']) # prints 1
    print(locals()['foo'])  # prints 2
print(func())
# = 2
#   1
#   2
#   None

foo = 1     # global
def func():
    print(foo)  # raises UnboundLocalError, because global foo is initialized but local foo no
    foo = 7     # local
    print(foo)

foo = 1
def func():
    foo = 7     # global foo is modified
    print(foo)  # 7
    print(globals()['foo']) # 1
print(func())
# = 7
#   1
#   None

foo = 1
def f1():
    bar = 1
    def f2():
        roc = 2
        # here, foo is a global variable, roc is a local variable
        # bar is not in either scope
        print(locals().keys())      # ['roc']
        print('bar' in locals())    # False
        print('bar' in globals())   # False
    def f3():
        roc = 3
        print(bar)  # bar from f1 is referenced so it enters local scope of f3 (closure)
        print(locals().keys())      # ['bar', 'roc']
        print('bar' in locals())    # True
        print('bar' in globals())   # False
    def f4():
        bar = 4     # a new local bar which hides bar from local scope of f1
        roc = 4
        print(bar)
        print(locals().keys())      # ['bar', 'roc']
        print('bar' in locals())    # True
        print('bar' in globals())   # False

# Global vs Nonlocal
foo = 0     # global foo
def f1():
    foo = 1     # a new foo local in f1

    def f2():
        foo = 2     # a new foo local in f2

        def f3():
            foo = 3     # a new foo local in f3
            print(foo)  # 3
            foo = 30    # modifies local foo in f3 only

        def f4():
            global foo
            print(foo)  # 0
            foo = 100   # modifies global foo

def f1():

    def f2():
        foo = 2     # a new foo local in f2

        def f3():
            nonlocal foo    # foo from f2, which is the nearest enclosing scope
            print(foo)      # 2
            foo = 20        # modifies foo from f2!
