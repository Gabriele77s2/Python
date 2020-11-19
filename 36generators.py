# List
alist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
5 in alist # True
10 in alist # False

# Tuple
atuple = ('0', '1', '2', '3', '4')
4 in atuple # False
'4' in atuple # True

# String
astring = 'i am a string'
'a' in astring # True
'am' in astring # True
'I' in astring # False

# Set
aset = {(10, 10), (20, 20), (30, 30)}
(10, 10) in aset # True
10 in aset # False

# Dict
adict = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
1 in adict # True - implicitly searches in keys
'a' in adict # False
2 in adict.keys() # True - explicitly searches in keys
'a' in adict.values() # True - explicitly searches in values
(0, 'a') in adict.items() # True - explicitly searches key/value pairs

# Getting the index for strings: str.index(), str.rindex() and str.find(), str.rfind()
astring = 'Hello on StackOverflow'
astring.index('o') # 4
astring.rindex('o') # 20

astring.find('o') # 4
astring.rfind('o') # 20
astring.index('q') # ValueError: substring not found
astring.find('q') # -1

astring.index('o', 5) # 6
astring.index('o', 6) # 6 - start is inclusive
astring.index('o', 5, 7) # 6
astring.index('o', 5, 6) # - end is not inclusive
# ValueError: substring not found

astring.rindex('o', 20) # 20
astring.rindex('o', 19) # 20 - still from left to right
astring.rindex('o', 4, 7) # 6

# Getting the index list and tuples: list.index(), tuple.index()
alist = [10, 16, 26, 5, 2, 19, 105, 26]
# search for 16 in the list
alist.index(16) # 1
alist[1] # 16
alist.index(15)
# ValueError: 15 is not in list

atuple = (10, 16, 26, 5, 2, 19, 105, 26)
atuple.index(26) # 2
atuple[2] # 26
atuple[7] # 26 - is also 26!

# Searching key(s) for a value in dict
def getKeysForValue(dictionary, value):
    foundkeys = []
    for keys in dictionary:
        if dictionary[key] == value:
            foundkeys.append(key)
    return foundkeys

# Same above function
def getKeysForValueComp(dictionary, value):
    return [key for key in dictionary if dictionary[key] == value]

# If you only care about one found key:
def getOneKeyForValue(dictionary, value):
 return next(key for key in dictionary if dictionary[key] == value)

adict = {'a': 10, 'b': 20, 'c': 10}
getKeysForValue(adict, 10) # ['c', 'a'] - order is random could as well be ['a', 'c']
getKeysForValueComp(adict, 10) # ['c', 'a'] - dito
getKeysForValueComp(adict, 20) # ['b']
getKeysForValueComp(adict, 25) # []
# The other one will only return one key
getOneKeyForValue(adict, 10) # 'c' - depending on the circumstances this could also be 'a'
getOneKeyForValue(adict, 20) # 'b'
getOneKeyForValue(adict, 25) # StopIteration
