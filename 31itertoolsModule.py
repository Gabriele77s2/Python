# combinations
import itertools
a = [1,2,3,4,5]
b = list(itertools.combinations(a, 2))
print(b)
# [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]

b = list(itertools.combinations(a, 3))
print(b)
# [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4),
#  (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5),
#  (2, 4, 5), (3, 4, 5)]

# dropwhile
def is_even(x):
    return x % 2 == 0

lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44]
result = list(itertools.dropwhile(is_even, lst))
print(result)
# [13, 14, 22, 23, 44]

# zip_longest
from itertools import zip_longest
a = [i for i in range(5)] # Length is 5
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] # Length is 7

for i in zip_longest(a, b):
    x, y = i # Note that zip longest returns the values as a tuple
    print(x, y)
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e
# None f
# None g

# Grouping items from an iterable object using a function
lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 2, 6)]

def testGroupBy(lst):
    groups = itertools.groupby(lst, key=lambda x: x[1])
    for key, group in groups:
        print(key, list(group))
testGroupBy(lst)
# 5 [('a', 5, 6)]
# 2 [('b', 2, 4), ('a', 2, 5), ('c', 2, 6)]

lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 5, 6)]
testGroupBy(lst)
# 5 [('a', 5, 6)]
# 2 [('b', 2, 4), ('a', 2, 5)]
# 5 [('c', 5, 6)]

lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 2, 6)]
groups = itertools.groupby(lst, key=lambda x: x[1])

for key, group in sorted(groups):
    print(key, list(group))
# 2 [('c', 2, 6)]
# 5 []

groups = itertools.groupby(lst, key=lambda x: x[1])
for key, group in sorted((key, list(group)) for key, group in groups):
    print(key, list(group))
# 2 [('b', 2, 4), ('a', 2, 5), ('c', 2, 6)]
# 5 [('a', 5, 6)]

# takewhile
def is_even(x):
    return x % 2 == 0

lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44]
result = list(itertools.takewhile(is_even, lst))
print(result)
# [0, 2, 4, 12, 18]

# permutations
a = [1,2,3]
list(itertools.permutations(a))
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
list(itertools.permutations(a, 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

a = [1,2,1]
list(itertools.permutations(a))
# [(1, 2, 1), (1, 1, 2), (2, 1, 1), (2, 1, 1), (1, 1, 2), (1, 2, 1)]
set(itertools.permutations(a))
# {(1, 1, 2), (1, 2, 1), (2, 1, 1)}

# repeat
import itertools
for i in itertools.repeat('over-and-over', 3):
    print(i)
# over-and-over
# over-and-over
# over-and-over

# Get an accumulated sum of numbers in an iterable
import itertools as it
import operator

list(it.accumulate([1,2,3,4,5]))
# [1, 3, 6, 10, 15]
list(it.accumulate([1,2,3,4,5], func=operator.mul))
# [1, 2, 6, 24, 120]

# Cycle through elements in an iterator
import itertools as it
it.cycle('ABCD')
# A B C D A B C D A B C D ...

# Iterate over each element in cycle for a fixed range
cycle_iterator = it.cycle('abc123')
[next(cycle_iterator) for i in range(0, 10)]
# ['a', 'b', 'c', '1', '2', '3', 'a', 'b', 'c', '1']

# count
for number in itertools.count():
    if number > 20:
        break
    print(number)
# 0
# 1
# 2
# 3
# ...

for number in itertools.count(start=10, step=4):
    print(number)
    if number > 20:
        break
# 10
# 14
# 18
# 22

# Chaining multiple iterators together
from itertools import chain
a = (x for x in ['1', '2', '3', '4'])
b = (x for x in ['x', 'y', 'z'])
' '.join(chain(a, b))
# '1 2 3 4 x y z'
