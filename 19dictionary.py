d = {}  # empty dict
d = {'key': 'value'}    # dict with initial values
d = dict()  # empty dict
d = dict(key='value')   # explicit keyword arguments
d = dict([('key', 'value')])    # passing in a list of key/value pairs

d['newkey'] = 42
d['new_list'] = [1, 2, 3]
d['new_dict'] = {'nested_dict': 1}

del d['newkey']

mydict = {}
print(mydict)
# {}
print(mydict.get("foo", "bar"))
# bar
print(mydict)
# {}
print(mydict.setdefault("foo", "bar"))
# bar
print(mydict)
# {'foo': 'bar'}

# Iterating over ad dictionary
d = {'a': 1, 'b': 2, 'c':3}
for key in d:
    print(key, d[key])
# c 3
# b 2
# a 1

print([key for key in d])
# ['c', 'b', 'a']

for key, value in d.items():
    print(key, value)
# c 3
# b 2
# a 1

# With default values
from collections import defaultdict
d = defaultdict(int)
d['key']    # 0
d['key'] = 5
d['key']     # 5
d = defaultdict(lambda: 'empty')
d['key']    # 'empty'
d['key'] = 'full'
d['key']    # 'full'

# Merge
fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
fishdog = {**fish, **dog}
print(fishdog)
# {'hands': 'paws', 'color': 'red', 'name': 'Clifford', 'special': 'gills'}

# Accessing keys and values
mydict = {'a':'1', 'b':'2'}
print(mydict.keys())
# dict_keys(['a', 'b'])
print(mydict.values())
# dict_values(['1', '2'])
print(mydict.items())
# dict_items([('a', '1'), ('b', '2')])

# Accessing values
dictionary = {"Hello": 1234, "World": 5678}
print(dictionary["Hello"])
# 1234

# Creating and populating it with values
stock = {'eggs': 5, 'milk': 2}
# Or creating an empty dictionary
dictionary = {}
# And populating it after
dictionary['eggs'] = 5
dictionary['milk'] = 2
# Values can also be lists
mydict = {'a': [1, 2, 3], 'b': ['one', 'two', 'three']}
# Use list.append() method to add new elements to the values list
mydict['a'].append(4)   # => {'a': [1, 2, 3, 4], 'b': ['one', 'two', 'three']}
mydict['b'].append('four')  # => {'a': [1, 2, 3, 4], 'b': ['one', 'two', 'three', 'four']}
# We can also create a dictionary using a list of two-items tuples
iterable = [('eggs', 5), ('milk', 2)]
dictionary = dict(iterables)
# Or using keyword argument:
dictionary = dict(eggs=5, milk=2)
# Another way will be to use the dict.fromkeys:
dictionary = dict.fromkeys((milk, eggs))    # => {'milk': None, 'eggs': None}
dictionary = dict.fromkeys((milk, eggs), (2, 5))    # => {'milk': 2, 'eggs': 5}

# Creating an ordered
from collections import OrderedDict
d = OrderedDict()
d['first'] = 1
d['second'] = 2
d['third'] = 3
d['last'] = 4
# Outputs "first 1", "second 2", "third 3", "last 4"
for key in d:
    print(key, d[key])

# The dict() constructor
dict(a=1, b=2, c=3)     # {'a': 1, 'b': 2, 'c': 3}
dict([('d', 4), ('e', 5), ('f', 6)])    # {'d': 4, 'e': 5, 'f': 6}
dict([('a', 1)], b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}
dict({'a' : 1, 'b' : 2}, c=3)   # {'a': 1, 'b': 2, 'c': 3}

# Example
car = {}
car["wheels"] = 4
car["color"] = "Red"
car["model"] = "Corvette"
print "Little " + car["color"] + " " + car["model"] + "!"
# Little Red Corvette!

car = {"wheels": 4, "color": "Red", "model": "Corvette"}
for key in car:
    print key + ": " + car[key]
# wheels: 4
# color: Red
# model: Corvette
