# Intersection
{1, 2, 3, 4, 5}.intersection({3, 4, 5, 6})
# Output: {3, 4, 5}
{1, 2, 3, 4, 5} & {3, 4, 5, 6}
# Output: {3, 4, 5}

# Union
{1, 2, 3, 4, 5}.union({3, 4, 5, 6})
# Output: {1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5} | {3, 4, 5, 6}
# Output: {1, 2, 3, 4, 5, 6}

# Difference
{1, 2, 3, 4}.difference({2, 3, 5})
# Output: {1, 4}
{1, 2, 3, 4} - {2, 3, 5}
# Output: {1, 4}

# Symmetric difference with
{1, 2, 3, 4}.symmetric_difference({2, 3, 5})
# Output: {1, 4, 5}
{1, 2, 3, 4} ^ {2, 3, 5}
# Output: {1, 4, 5}

# Superset check
{1, 2}.issuperset({1, 2, 3})
# Output: False
{1, 2} >= {1, 2, 3}
# Output: False

# Subset check
{1, 2}.issubset({1, 2, 3})
# Output: True
{1, 2} <= {1, 2, 3}
# Output: True

# Disjoint check
{1, 2}.isdisjoint({3, 4})
# Output: True
{1, 2}.isdisjoint({1, 4})
# Output: False

# Existence check
2 in {1,2,3}
# Output: True
4 in {1,2,3}
# Output: False
4 not in {1,2,3}
# Output: True

# Add and Remove
s = {1,2,3}
s.add(4)
# Output: s == {1,2,3,4}
s.discard(3)
# Output: s == {1,2,4}
s.discard(5)
# Output: s == {1,2,4}
s.remove(2)
# Output: s == {1,4}
s.remove(2)
# Output: KeyError!

s = {1, 2}
s.update({3, 4})
# Output: s == {1, 2, 3, 4}

restaurants = ["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]
unique_restaurants = set(restaurants)
print(unique_restaurants)
# Output: {'Chicken Chicken', "McDonald's", 'Burger King'}

list(unique_restaurants)
# Output: ['Chicken Chicken', "McDonald's", 'Burger King']

# Removes all duplicates and returns another list
list(set(restaurants))

# Set of Sets
print({frozenset({1, 2}), frozenset({3, 4})})

a = {1, 2, 2, 3, 4}
b = {3, 3, 4, 4, 5}

a.intersection(b)
# Output: {3, 4}
a.union(b)
# Output: {1, 2, 3, 4, 5}
a.difference(b)
# Output: {1, 2}
b.difference(a)
# Output: {5}

# a.symmetric_difference(b) == b.symmetric_difference(a)
a.symmetric_difference(b)
# Output: {1, 2, 5}
b.symmetric_difference(a)
# Output: {1, 2, 5}

c = {1, 2}
c.issubset(a)
# Output: True
a.issuperset(c)
# Output: True

d = {5, 6}
a.isdisjoint(b) # {2, 3, 4} are in both sets
# Output: False
a.isdisjoint(d)
# Output: True

# This is an equivalent check, but less efficient
len(a & d) == 0
# Output: True

# This is even less efficient
a & d == set()
# Output: True

1 in a
# Output: True
6 in a
# Output: False

len(a)
# Output: 4
len(b)
# Output: 3

setA = {'a','b','b','c'}
print(setA)
# Output: set(['a', 'c', 'b'])

listA = ['a','b','b','c']
print(listA)
# Output: ['a', 'b', 'b', 'c']

from collections import Counter
counterA = Counter(['a','b','b','c'])
print(counterA)
# Output: Counter({'b': 2, 'a': 1, 'c': 1})
