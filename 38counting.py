from collections import Counter
c = Counter(["a", "b", "c", "d", "a", "b", "a", "c", "d"])
print(c)
# Out: Counter({'a': 3, 'b': 2, 'c': 2, 'd': 2})
c["a"]
# Out: 3
c[7] # not in the list (7 occurred 0 times!)
# Out: 0

Counter({"e": 2})
# Out: Counter({"e": 2})
Counter({"e": "e"}) # warning Counter does not verify the values are int
# Out: Counter({"e": "e"})

# Getting the most common value(-s): collections.Counter.most_common()
adict = {'a': 5, 'b': 3, 'c': 5, 'd': 2, 'e':2, 'q': 5}
Counter(adict.values())
# Out: Counter({2: 2, 3: 1, 5: 3})

# Sorting them from most-common to least-common value:
Counter(adict.values()).most_common()
# Out: [(5, 3), (2, 2), (3, 1)]
# Getting the most common value
Counter(adict.values()).most_common(1)
# Out: [(5, 3)]
# Getting the two most common values
Counter(adict.values()).most_common(2)
# Out: [(5, 3), (2, 2)]

# Counting the occurrences of one item in a sequence: list.count() and tuple.count()
alist = [1, 2, 3, 4, 1, 2, 1, 3, 4]
alist.count(1)
# Out: 3
atuple = ('bear', 'weasel', 'bear', 'frog')
atuple.count('bear')
# Out: 2
atuple.count('fox')
# Out: 0

# Counting the occurrences of a substring in a string: str.count()
astring = 'thisisashorttext'
astring.count('t')
# Out: 4
astring.count('th')
# Out: 1
astring.count('is')
# Out: 2
astring.count('text')
# Out: 1
Counter(astring)
# Out: Counter({'a': 1, 'e': 1, 'h': 2, 'i': 2, 'o': 1, 'r': 1, 's': 3, 't': 4, 'x': 1})

# Counting occurrences in numpy array
import numpy as np
a = np.array([0,3,4,3,5,4,7])
print(np.sum(a==3))
# 2

unique,counts=np.unique(a,return_counts=True)
print(unique,counts) # counts[i] is equal to occurrences of unique[i] in a
# [0 3 4 5 7] [1 2 2 1 1]

bin_count=np.bincount(a)
print(bin_count) # bin_count[i] is equal to occurrences of i in a
# [1 0 0 2 2 1 0 1]
