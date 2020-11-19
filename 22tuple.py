# Tuples are immutable
t = 'a', 'b', 'c', 'd', 'e'
t = ('a', 'b', 'c', 'd', 'e')

t0 = ()
type(t0) # <type 'tuple'>
t1 = 'a',
type(t1) # <type 'tuple'>
t2 = ('a')
type(t2) # <type 'str'>
t2 = ('a',)
type(t2) # <type 'tuple'>

t = tuple('lupins')
print(t) # ('l', 'u', 'p', 'i', 'n', 's')
t = tuple(range(3))
print(t) # (0, 1, 2)

t = (1, 2)
q = t
t += (3, 4)
print(t)
# (1, 2, 3, 4)
print(q)
# (1, 2)

a = 1   # a is the value 1
a = 1,  # a is the tuple (1,)
a = (1,) # a is the tuple (1,)
a = (1)  # a is the value 1 and not a tuple

x, y, z = (1, 2, 3)
# x == 1
# y == 2
# z == 3

a = 1, 2, 3, 4
_, x, y, _ = a
# x == 2
# y == 3

x, = 1, # x is the value 1
x = 1,  # x is the tuple (1,)

# Comparison
tuple1 = ('a', 'b', 'c', 'd', 'e')
tuple2 = ('1','2','3')
tuple3 = ('a', 'b', 'c', 'd', 'e')

cmp(tuple1, tuple2)
# Out: 1
cmp(tuple2, tuple1)
# Out: -1
cmp(tuple1, tuple3)
# Out: 0

len(tuple1)
# Out: 5

max(tuple1)
# Out: 'e'
max(tuple2)
# Out: '3'

min(tuple1)
# Out: 'a'
min(tuple2)
# Out: '1'

# Convert a list into tuple
list = [1,2,3,4,5]
tuple(list)
# Out: (1, 2, 3, 4, 5)

# Concatenation
tuple1 + tuple2
# Out: ('a', 'b', 'c', 'd', 'e', '1', '2', '3')

# Indexing
x = (1, 2, 3)
x[0] # 1
x[1] # 2
x[2] # 3
x[3] # IndexError: tuple index out of range
# Indexing with negative numbers will start from the last element as -1
x[-1] # 3
x[-2] # 2
x[-3] # 1
x[-4] # IndexError: tuple index out of range

print(x[:-1]) # (1, 2)
print(x[-1:]) # (3,)
print(x[1:3]) # (2, 3)

# Reversing
colors = "red", "green", "blue"
rev = colors[::-1]
# rev: ("blue", "green", "red")

rev = tuple(reversed(colors))
# rev: ("blue", "green", "red")
