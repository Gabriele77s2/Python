# Make custom classes orderable
# min, max, and sorted all need the objects to be orderable
# To be properly orderable, the class needs to define all of
# the 6 methods __lt__, __gt__, __ge__, __le__, __ne__ and __eq__:
class IntegerContainer(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.value)

    def __lt__(self, other):
        print('{!r} - Test less than {!r}'.format(self, other))
        return self.value < other.value

    def __le__(self, other):
        print('{!r} - Test less than or equal to {!r}'.format(self, other))
        return self.value <= other.value

    def __gt__(self, other):
        print('{!r} - Test greater than {!r}'.format(self, other))
        return self.value > other.value

    def __ge__(self, other):
        print('{!r} - Test greater than or equal to {!r}'.format(self, other))
        return self.value >= other.value

    def __eq__(self, other):
        print('{!r} - Test equal to {!r}'.format(self, other))
        return self.value == other.value

    def __ne__(self, other):
        print('{!r} - Test not equal to {!r}'.format(self, other))
        return self.value != other.value

alist = [IntegerContainer(5), IntegerContainer(3),
         IntegerContainer(10), IntegerContainer(7)]
res = max(alist)
# Out: IntegerContainer(3) - Test greater than IntegerContainer(5)
# IntegerContainer(10) - Test greater than IntegerContainer(5)
# IntegerContainer(7) - Test greater than IntegerContainer(10)
print(res)
# Out: IntegerContainer(10)
res = min(alist)
# Out: IntegerContainer(3) - Test less than IntegerContainer(5)
# IntegerContainer(10) - Test less than IntegerContainer(3)
# IntegerContainer(7) - Test less than IntegerContainer(3)
print(res)
# Out: IntegerContainer(3)
res = sorted(alist)
# Out: IntegerContainer(3) - Test less than IntegerContainer(5)
# IntegerContainer(10) - Test less than IntegerContainer(3)
# IntegerContainer(10) - Test less than IntegerContainer(5)
# IntegerContainer(7) - Test less than IntegerContainer(5)
# IntegerContainer(7) - Test less than IntegerContainer(10)
print(res)
# Out: [IntegerContainer(3), IntegerContainer(5), IntegerContainer(7), IntegerContainer(10)]
res = sorted(alist, reverse=True)
# Out: IntegerContainer(10) - Test less than IntegerContainer(7)
# IntegerContainer(3) - Test less than IntegerContainer(10)
# IntegerContainer(3) - Test less than IntegerContainer(10)
# IntegerContainer(3) - Test less than IntegerContainer(7)
# IntegerContainer(5) - Test less than IntegerContainer(7)
# IntegerContainer(5) - Test less than IntegerContainer(3)
print(res)
# Out: [IntegerContainer(10), IntegerContainer(7), IntegerContainer(5), IntegerContainer(3)]

del IntegerContainer.__lt__ # The IntegerContainer no longer implements "less than"
res = min(alist)
# Out: IntegerContainer(5) - Test greater than IntegerContainer(3)
# IntegerContainer(3) - Test greater than IntegerContainer(10)
# IntegerContainer(3) - Test greater than IntegerContainer(7)
print(res)
# Out: IntegerContainer(3)

del IntegerContainer.__gt__ # The IntegerContainer no longer implements "greater then"
res = min(alist)
# TypeError: unorderable types: IntegerContainer() < IntegerContainer()

# functools
import functools

@functools.total_ordering
class IntegerContainer(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.value)

    def __lt__(self, other):
        print('{!r} - Test less than {!r}'.format(self, other))
        return self.value < other.value

    def __eq__(self, other):
        print('{!r} - Test equal to {!r}'.format(self, other))
        return self.value == other.value

    def __ne__(self, other):
        print('{!r} - Test not equal to {!r}'.format(self, other))
        return self.value != other.value

IntegerContainer(5) > IntegerContainer(6)
# Output: IntegerContainer(5) - Test less than IntegerContainer(6)
# Returns: False
IntegerContainer(6) > IntegerContainer(5)
# Output: IntegerContainer(6) - Test less than IntegerContainer(5)
# Output: IntegerContainer(6) - Test equal to IntegerContainer(5)
# Returns True

# Special case: dictionaries
adict = {'a': 3, 'b': 5, 'c': 1}
min(adict)
# Output: 'a'
max(adict)
# Output: 'c'
sorted(adict)
# Output: ['a', 'b', 'c']

# To keep the dictionary structure, you have to iterate over the .items():
min(adict.items())
# Output: ('a', 3)
max(adict.items())
# Output: ('c', 1)
sorted(adict.items())
# Output: [('a', 3), ('b', 5), ('c', 1)]

# For sorted, you could create an OrderedDict to keep the sorting while having a dict-like structure:
from collections import OrderedDict
OrderedDict(sorted(adict.items()))
# Output: OrderedDict([('a', 3), ('b', 5), ('c', 1)])
res = OrderedDict(sorted(adict.items()))
res['a']
# Output: 3

# By value
Again this is possible using the key argument:
min(adict.items(), key=lambda x: x[1])
# Output: ('c', 1)
max(adict.items(), key=operator.itemgetter(1))
# Output: ('b', 5)
sorted(adict.items(), key=operator.itemgetter(1), reverse=True)
# Output: [('b', 5), ('a', 3), ('c', 1)]

# Using the key argument
list_of_tuples = [(0, 10), (1, 15), (2, 8)]
min(list_of_tuples)
# Output: (0, 10)

# but if you want to sort by a specific element in each sequence use the key-argument:
min(list_of_tuples, key=lambda x: x[0]) # Sorting by first element
# Output: (0, 10)
min(list_of_tuples, key=lambda x: x[1]) # Sorting by second element
# Output: (2, 8)
sorted(list_of_tuples, key=lambda x: x[0]) # Sorting by first element (increasing)
# Output: [(0, 10), (1, 15), (2, 8)]
sorted(list_of_tuples, key=lambda x: x[1]) # Sorting by first element
# Output: [(2, 8), (0, 10), (1, 15)]

import operator
# The operator module contains efficient alternatives to the lambda function
max(list_of_tuples, key=operator.itemgetter(0)) # Sorting by first element
# Output: (2, 8)
max(list_of_tuples, key=operator.itemgetter(1)) # Sorting by second element
# Output: (1, 15)
sorted(list_of_tuples, key=operator.itemgetter(0), reverse=True) # Reversed (decreasing)
# Output: [(2, 8), (1, 15), (0, 10)]
sorted(list_of_tuples, key=operator.itemgetter(1), reverse=True) # Reversed(decreasing)
# Output: [(1, 15), (0, 10), (2, 8)]

# Getting a sorted sequence
sorted((7, 2, 1, 5)) # tuple
# Output: [1, 2, 5, 7]
sorted(['c', 'A', 'b']) # list
# Output: ['A', 'b', 'c']
sorted({11, 8, 1}) # set
# Output: [1, 8, 11]
sorted({'11': 5, '3': 2, '10': 15}) # dict
# Output: ['10', '11', '3'] # only iterates over the keys
sorted('bdca') # string
# Output: ['a','b','c','d']

# Extracting N largest or N smallest items from an iterable
import heapq
# get 5 largest items from the range
heapq.nlargest(5, range(10))
# Output: [9, 8, 7, 6, 5]
heapq.nsmallest(5, range(10))
# Output: [0, 1, 2, 3, 4]

# Getting the minimum or maximum of several values
min(7,2,1,5)
# Output: 1
max(7,2,1,5)
# Output: 7

# Minimum and Maximum of a sequence
min([2, 7, 5])
# Output: 2
sorted([2, 7, 5])[0]
# Output: 2
max([2, 7, 5])
# Output: 7
sorted([2, 7, 5])[-1]
# Output: 7

# But if there are multiple elements that are evaluated as having the maximum value:
class MyClass(object):
    def __init__(self, value, name):
        self.value = value
        self.name = name

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return str(self.name)

sorted([MyClass(4, 'first'), MyClass(1, 'second'), MyClass(4, 'third')])
# Output: [second, first, third]
max([MyClass(4, 'first'), MyClass(1, 'second'), MyClass(4, 'third')])
# Output: first
