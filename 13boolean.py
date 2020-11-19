# Function
def true_func():
    print("true_func()")
    return True

def false_func():
    print("false_func()")
    return False

print(true_func() or false_func())
# = true_func()
#   True
print(false_func() or true_func())
# = false_func()
#   true_func()
#   True
print(true_func() and false_func())
# = true_func()
#   false_func()
#   False
print(false_func() and false_func())
# = false_func()
#   False

# And
x = True
y = True
z = x and y
print(z)
# = True

x = True
y = False
z = x and y
print(z)
# = False

x = False
y = True
z = x and y
print(z)
# = False

x = False
y = False
z = x and y
print(z)
# = False

# False is favorite on True

x = 1
y = 1
z = x and y
print(z)    # z = y, so z = 1
# = 1

x = 0
y = 1
z = x and y
print(z)    # z = x, so z = 0
# = 0

x = 1
y = 0
z = x and y
print(z)    # z = y, so z = 0
# = 0

x = 0
y = 0
z = x and y
print(z)    # z = x, so z = 0
# = 0

# Zero '0' is favorite on One '1'

# Or
x = True
y = True
z = x or y
print(z)
# = True

x = True
y = False
z = x or y
print(z)
# = True

x = False
y = True
z = x or y
print(z)
# = True

x = False
y = False
z = x and y
print(z)
# = False

# True is favorite on False

x = 1
y = 1
z = x or y
print(z)    # z = y, so z = 1
# = 1

x = 0
y = 1
z = x or y
print(z)    # z = y, so z = 1
# = 1

x = 1
y = 0
z = x or y
print(z)    # z = x, so z = 1
# = 1

x = 0
y = 0
z = x or y
print(z)    # z = x, so z = 0
# = 0

# One '1' is favorite on Zero '0'

# Not
x = True
y = not x
print(y)
# = False

x = False
y = not x
print(y)
# = True
