import collections
counts = collections.Counter([1,2,3])
# letter counter
collections.Counter('Happy Birthday')
# Counter({'a': 2, 'p': 2, 'y': 2, 'i': 1, 'r': 1, 'B': 1, ' ': 1, 'H': 1, 'd': 1, 'h': 1, 't': 1})

# world counter
collections.Counter('I am Sam Sam I am That Sam-I-am That Sam-I-am! I do not like that Sam-I-am'.split())
# Counter({'I': 3, 'Sam': 2, 'Sam-I-am': 2, 'That': 2, 'am': 2, 'do': 1, 'Sam-I-am!': 1, 'that': 1, 'not': 1, 'like': 1})

# recipes
c = collections.Counter({'a': 4, 'b': 2, 'c': -2, 'd': 0})

# Get count of individual element
c['a']
# 4

# Set count of individual element
c['c'] = -3
# Counter({'a': 4, 'b': 2, 'd': 0, 'c': -3})

# Get total number of elements in counter (4 + 2 + 0 - 3)
sum(c.itervalues()) # negative numbers are counted!
# 3

# Get elements (only those with positive counter are kept)
list(c.elements())
# ['a', 'a', 'a', 'a', 'b', 'b']

# Remove keys with 0 or negative value
c - collections.Counter()
# Counter({'a': 4, 'b': 2})

# Remove everything
c.clear()
# Counter()

# Add remove individual elements
c.update({'a': 3, 'b':3})
c.update({'a': 2, 'c':2}) # adds to existing, sets if they don't exist
# Counter({'a': 5, 'b': 3, 'c': 2})
c.subtract({'a': 3, 'b': 3, 'c': 3}) # subtracts (negative values are allowed)
# Counter({'a': 2, 'b': 0, 'c': -1})

# collections.OrderedDict
d = {'foo': 5, 'bar': 6}
print(d)
# {'foo': 5, 'bar': 6}

d['baz'] = 7
print(a)
# {'baz': 7, 'foo': 5, 'bar': 6}

d['foobar'] = 8
print(a)
# {'baz': 7, 'foo': 5, 'bar': 6, 'foobar': 8}

from collections import OrderedDict
d = OrderedDict([('foo', 5), ('bar', 6)])
print(d)
# OrderedDict([('foo', 5), ('bar', 6)])

d['baz'] = 7
print(d)
# OrderedDict([('foo', 5), ('bar', 6), ('baz', 7)])

d['foobar'] = 8
print(d)
# OrderedDict([('foo', 5), ('bar', 6), ('baz', 7), ('foobar', 8)])

# Or we can create an empty OrderedDict and then add items:
o = OrderedDict()
o['key1'] = "value1"
o['key2'] = "value2"
print(o)
# OrderedDict([('key1', 'value1'), ('key2', 'value2')])

# Iterating through an OrderedDict allows key access in the order they were added
d['foo'] = 4
print(d)
OrderedDict([('foo', 4), ('bar', 6), ('baz', 7), ('foobar', 8)])

# collections.defaultdict
# str
state_capitals = collections.defaultdict(str)
# defaultdict(<class 'str'>, {})
state_capitals['Alaska']
# ''
state_capitals
# defaultdict(<class 'str'>, {'Alaska': ''})

# int
fruit_counts = defaultdict(int)
fruit_counts['apple'] += 2 # No errors should occur
# default_dict(int, {'apple': 2})
fruit_counts['banana'] # No errors should occur
# 0
fruit_counts # A new key is created
# default_dict(int, {'apple': 2, 'banana': 0})

state_capitals['Alabama'] = 'Montgomery'
# defaultdict(<class 'str'>, {'Alabama': 'Montgomery', 'Alaska': ''})

# Using list as the default_factory will create a list for each new key.
s = [('NC', 'Raleigh'), ('VA', 'Richmond'), ('WA', 'Seattle'), ('NC', 'Asheville')]
dd = collections.defaultdict(list)
for k, v in s:
    dd[k].append(v)
print(dd)
# defaultdict(<class 'list'>,
# {'VA': ['Richmond'],
#  'NC': ['Raleigh', 'Asheville'],
#  'WA': ['Seattle']})

# collections.namedtuple
Person = namedtuple('Person', ['age', 'height', 'name'])
Person = namedtuple('Person', 'age, height, name')
Person = namedtuple('Person', 'age height name')

dave = Person(30, 178, 'Dave')
jack = Person(age=30, height=178, name='Jack S.')
print(jack.age) # 30
print(jack.name) # 'Jack S.'

Human = namedtuple('Person', 'age, height, name')
dave = Human(30, 178, 'Dave')
print(dave) # yields: Person(age=30, height=178, name='Dave')

# collections.deque
from collections import deque
d = deque('ghi') # make a new deque with three items
for elem in d: # iterate over the deque's elements
    print elem.upper()
# G
# H
# I

d.append('j') # add a new entry to the right side
d.appendleft('f') # add a new entry to the left side
# show the representation of the deque
# deque(['f', 'g', 'h', 'i', 'j'])

d.pop() # return and remove the rightmost item
# 'j'

d.popleft() # return and remove the leftmost item
# 'f'

list(d) # list the contents of the deque
# ['g', 'h', 'i']
d[0] # peek at leftmost item
# 'g'
d[-1] # peek at rightmost item
# 'i'

list(reversed(d)) # list the contents of a deque in reverse
# ['i', 'h', 'g']
'h' in d # search the deque
# True

d.extend('jkl') # add multiple elements at once
# deque(['g', 'h', 'i', 'j', 'k', 'l'])

d.rotate(1) # right rotation
# deque(['l', 'g', 'h', 'i', 'j', 'k'])

d.rotate(-1) # left rotation
#deque(['g', 'h', 'i', 'j', 'k', 'l'])

deque(reversed(d)) # make a new deque in reverse order
# deque(['l', 'k', 'j', 'i', 'h', 'g'])

d.clear() # empty the deque
d.pop() # cannot pop from an empty deque
# Traceback (most recent call last):
# File "<pyshell#6>", line 1, in -toplevel-
# d.pop()
# IndexError: pop from an empty deque

d.extendleft('abc') # extendleft() reverses the input order
# deque(['c', 'b', 'a'])

# collections.ChainMap
import collections
# define two dictionaries with at least some keys overlapping.
dict1 = {'apple': 1, 'banana': 2}
dict2 = {'coconut': 1, 'date': 1, 'apple': 3}

# create two ChainMaps with different ordering of those dicts.
combined_dict = collections.ChainMap(dict1, dict2)
reverse_ordered_dict = collections.ChainMap(dict2, dict1)

# Note the impact of order on which value is found first in the subsequent lookup
for k, v in combined_dict.items():
    print(k, v)
# date 1
# apple 1
# banana 2
# coconut 1

for k, v in reverse_ordered_dict.items():
    print(k, v)
# date 1
# apple 3
# banana 2
# coconut 1
