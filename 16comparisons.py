# a == b compares the value of a and b
# a is b will compare the identities of a and b
a = 'Python is fun!'
b = 'Python is fun!'
a == b  # returns True
a is b  # returns False

a = [1, 2, 3, 4, 5]
b = a   # b references a
a == b  # True
a is b  # True
b = a[:]    # b now references a copy of a
a == b  # True
a is b  # False [!!]

# Longer strings and larger integers will be stored separately
a = 'short'
b = 'short'
c = 5
d = 5
a is b # True
c is d # True

a = 'not so short'
b = 'not so short'
c = 1000
d = 1000
a is b # False
c is d # False

# Operations
12 > 4
# True
12 < 4
# False
1 < 4
# True

12 != 1
# True
12 != '12'
# True
'12' != '12'
# False

12 == 12
# True
12 == 1
# False
'12' == '12'
# True
'spam' == 'spam'
# True
'spam' == 'spam '
# False
'12' == 12
# False

# Comparing Objects
class Foo(object):
    def __init__(self, item):
        self.my_item = item
    def __eq__(self, other):
        return self.my_item == other.my_item

a = Foo(5)
b = Foo(5)
a == b # True
a != b # False
a is b # False
