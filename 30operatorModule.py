# Itemgetter
from itertools import groupby
from operator import itemgetter

adict = {'a': 1, 'b': 5, 'c': 1}
dict((i, dict(v)) for i, v in groupby(adict.items(), itemgetter(1)))
# Output: {1: {'a': 1, 'c': 1}, 5: {'b': 5}}

alist_of_tuples = [(5,2), (1,3), (2,2)]
sorted(alist_of_tuples, key=itemgetter(1,0))
# Output: [(2, 2), (5, 2), (1, 3)]

# Operators as alternative to an infix operator
1 + 1
# Output: 2
from operator import add
add(1, 1)
# Output: 2

from operator import mul
mul('a', 10)
# Output: 'aaaaaaaaaa'
mul([3], 3)
# Output: [3, 3, 3]

# Methodcaller
alist = ['wolf', 'sheep', 'duck']
list(filter(lambda x: x.startswith('d'), alist)) # Keep only elements that start with 'd'
# Output: ['duck']

from operator import methodcaller
list(filter(methodcaller('startswith', 'd'), alist)) # Does the same but is faster.
# Output: ['duck']
