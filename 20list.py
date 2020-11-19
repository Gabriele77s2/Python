a = [1, 2, 3, 4, 5]
# Append values 6, 7, and 7 to the list
a.append(6)
a.append(7)
a.append(7)
# a: [1, 2, 3, 4, 5, 6, 7, 7]

# Append another list
b = [8, 9, 10]
a.append(b)
# a: [1, 2, 3, 4, 5, 6, 7, 7, [8, 9, 10]]
a[8]
# Returns: [8,9,10]

# Append an element of a different type, as list elements do not need to have the same type
my_string = "hello world"
a.append(my_string)
# a: [1, 2, 3, 4, 5, 6, 7, 7, [8, 9], "hello world"]

# Extend list by appending all elements from b
a.extend(b)
# a: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]

# Extend list with elements from a non-list enumerable:
a.extend(range(3))
# a: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 0, 1, 2]

# Concatenate
a = [1, 2, 3, 4, 5, 6] + [7, 7] + b
# a: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]

# Index
a.index(7)
# Returns: 6
a.index(49)     # ValueError, because 49 is not in a.
a.index(7, 7)
# Returns: 7
a.index(7, 8)   # ValueError, because there is no 7 starting at index 8
a.insert(0, 0)  # insert 0 at position 0
a.insert(2, 5)  # insert 5 at position 2
# a: [0, 1, 5, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]

# Pop
a.pop(2)
# Returns: 5
# a: [0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
a.pop(8)
# Returns: 7
# a: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# With no argument:
a.pop()
# Returns: 10
# a: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Remove
a.remove(0)
a.remove(9)
# a: [1, 2, 3, 4, 5, 6, 7, 8]
a.remove(10)
# ValueError, because 10 is not in a

# Reverse
a.reverse()
# a: [8, 7, 6, 5, 4, 3, 2, 1]

# Count
a.count(7)
# Returns: 2

# Clear
a.clear()
# a = []

# Sort
a.sort()
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# Sorts the list in numerical order

a.sort(reverse = True)
# a = [8, 7, 6, 5, 4, 3, 2, 1]

# Better way to sort using attrgetter and itemgetter
from operator import itemgetter, attrgetter
people = [{'name':'chandan','age':20,'salary':2000},
          {'name':'chetan','age':18,'salary':5000},
          {'name':'guru','age':30,'salary':3000}]

by_age = itemgetter('age')
by_salary = itemgetter('salary')

people.sort(key=by_age) #in-place sorting by age
people.sort(key=by_salary) #in-place sorting by salary

list_of_tuples = [(1,2), (3,4), (5,0)]
list_of_tuples.sort(key=itemgetter(1))
print(list_of_tuples) #[(5, 0), (1, 2), (3, 4)]

persons = [Person("John Cena", datetime.date(1992, 9, 12), 175),
           Person("Chuck Norris", datetime.date(1990, 8, 28), 180),
           Person("Jon Skeet", datetime.date(1991, 7, 6), 185)]

person.sort(key=attrgetter('name'))     #sort by name
by_birthday = attrgetter('birthday')
person.sort(key=by_birthday)    #sort by birthday

# Replication
b = ["blah"] * 3
# b = ["blah", "blah", "blah"]

b = [1, 3, 5] * 5
# [1, 3, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5]

# Delete
a = list(range(10))
del a[::2]
# a = [1, 3, 5, 7, 9]
del a[-1]
# a = [1, 3, 5, 7]
del a[:]
# a = []

# Copying
b = a
a.append(6)
# b: [1, 2, 3, 4, 5, 6]

# Accessing
lst = [1, 2, 3, 4]
lst[0] # 1
lst[1] # 2

lst[4]  # IndexError: list index out of range
lst[-1] # 4
lst[-2] # 3
lst[-5] # IndexError: list index out of range
lst[len(lst)-1] # 4

lst[1:] # [2, 3, 4]
lst[:3] # [1, 2, 3]
lst[::2] # [1, 3]
lst[::-1] # [4, 3, 2, 1]
lst[-1:0:-1] # [4, 3, 2]
lst[5:8] # [] since starting index is greater than length of lst, returns empty list
lst[1:10] # [2, 3, 4] same as omitting ending index
lst[::-1] # [4, 3, 2, 1]
lst[3:1:-1] # [4, 3]
reversed(lst)[0:2] # 0 = 1 -1
 # 2 = 3 -1

# Slicing
data = 'chandan purohit    22 2000' #assuming data fields of fixed length
name_slice = slice(0,19)
age_slice = slice(19,21)
salary_slice = slice(22,None)

#now we can have more readable slices
print(data[name_slice]) #chandan purohit
print(data[age_slice]) #'22'
print(data[salary_slice]) #'2000'

# Checking if list is empty
lst = []
if not lst:
 print("list is empty")
# Output: list is empty

# Iterating over a list
my_list = ['foo', 'bar', 'baz']
for item in my_list:
    print(item)
# Output: foo
# Output: bar
# Output: baz

for (index, item) in enumerate(my_list):
    print('The item in position {} is: {}'.format(index, item))
# Output: The item in position 0 is: foo
# Output: The item in position 1 is: bar
# Output: The item in position 2 is: baz

for i in range(0,len(my_list)):
    print(my_list[i])
# Output: foo
# Output: bar
# Output: baz

for item in my_list:
    if item == 'foo':
        del my_list[0]
    print(item)
# Output: foo
# Output: baz

# Checking if an item is in a list
lst = ['test', 'twest', 'tweast', 'treast']
'test' in lst
# Out: True
'toast' in lst
# Out: False

# Any and all
nums = [1, 1, 0, 1]
all(nums)
# False

chars = ['a', 'b', 'c', 'd']
all(chars)
# True

nums = [1, 1, 0, 1]
any(nums)
# True

vals = [None, None, None, False]
any(vals)
# False

vals = [1, 2, 3, 4]
any(val > 12 for val in vals)
# False
any((val * 2) > 6 for val in vals)
# True

# Concatenate and merge
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
    print(a, b)
# Output:
# a1 b1
# a2 b2
# a3 b3

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3', 'b4']
for a, b in zip(alist, blist):
    print(a, b)
# Output:
# a1 b1
# a2 b2
# a3 b3

alist = ['a1', 'a2', 'a3']
blist = ['b1']
clist = ['c1', 'c2', 'c3', 'c4']
for a, b, c in itertools.zip_longest(alist, blist, clist):
    print(a, b, c)
# Output:
# a1 b1 c1
# a2 None c2
# a3 None c3
# None None c4

# Insert to a specific index values
alist = [123, 'xyz', 'zara', 'abc']
alist.insert(3, [2009])
print("Final List :", alist)
# Output: Final List : [123, 'xyz', 'zara', 2009, 'abc']

# Lenght
len(['one', 'two']) # returns 2
len(['one', [2, 3], 'four']) # returns 3, not 4

# Remove duplicate values
names = ["aixk", "duke", "edik", "tofp", "duke"]
list(set(names))
# Out: ['duke', 'tofp', 'aixk', 'edik']

# Comparison
[1, 10, 100] < [2, 10, 100]
# True, because 1 < 2
[1, 10, 100] < [1, 10, 100]
# False, because the lists are equal
[1, 10, 100] <= [1, 10, 100]
# True, because the lists are equal
[1, 10, 100] < [1, 10, 101]
# True, because 100 < 101
[1, 10, 100] < [0, 10, 100]
# False, because 1 > 0
[1, 10] < [1, 10, 100]
# True

# Accessing values in nested list
x = [1, 2, [3, 4, 5], 6, 7] # this is nested list
print x[2]
# Output: [3, 4, 5]
print x[2][1]
# Output: 4

alist = [[[1,2],[3,4]], [[5,6,7],[8,9,10],[12, 13, 14]]]
print(alist[0][0][1])
# 2
# Accesses second element in the first list

print(alist[1][1][2])
# 10
# Accesses the third element in the second list

alist[0][0].append(11)
print(alist[0][0][2])
# 11
# Appends 11 to the end of the first list

for row in alist: #One way to loop through nested lists
    for col in row:
        print(col)
# [1, 2, 11]
# [3, 4]
# [5, 6, 7]
# [8, 9, 10]
# [12, 13, 14]

[col for row in alist for col in row]
#[[1, 2, 11], [3, 4], [5, 6, 7], [8, 9, 10], [12, 13, 14]]

alist[1].insert(2, 15)
#Inserts 15 into the third position in the second list

print(alist[1][1:])
# [[8, 9, 10], 15, [12, 13, 14]]
# Slices still work

print(alist)
# [[[1, 2, 11], [3, 4]], [[5, 6, 7], [8, 9, 10], 15, [12, 13, 14]]]

# Initializing a list to a fixed number of elements
# For immutable elements (None, string literals, etc.)
my_list = [None] * 10
my_list = ['test'] * 10

# For mutable
my_list=[{1}] * 10
print(my_list)
# [{1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}]

my_list=[{1} for _ in range(10)]
print(my_list)
# [{1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}]

my_list[0].add(2)
print(my_list)
# [{1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}]

squares = [x * x for x in (1, 2, 3, 4)]
# squares: [1, 4, 9, 16]

squares = []
for x in (1, 2, 3, 4):
    squares.append(x * x)
# squares: [1, 4, 9, 16]

# Get a list of uppercase characters from a string
[s.upper() for s in "Hello World"]
# ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']

# Strip off any commas from the end of strings in a list
[w.strip(',') for w in ['these,', 'words,,', 'mostly', 'have,commas,']]
# ['these', 'words', 'mostly', 'have,commas']

# Organize letters in words more reasonably - in an alphabetical order
sentence = "Beautiful is better than ugly"
["".join(sorted(word, key = lambda x: x.lower())) for word in sentence.split()]
# ['aBefiltuu', 'is', 'beertt', 'ahnt', 'gluy']

# Create a list of characters in apple, replacing non vowels with '*'
# Example - 'apple' --> ['a', '*', '*', '*' ,'e']
[x for x in 'apple' if x in 'aeiou' else '*']
#SyntaxError: invalid syntax
# When using if/else together use them before the loop
[x if x in 'aeiou' else '*' for x in 'apple']
#['a', '*', '*', '*', 'e']

# Sort in-place mutation
[x.sort() for x in [[2, 1], [4, 3], [0, 1]]]
# [None, None, None]
[sorted(x) for x in [[2, 1], [4, 3], [0, 1]]]
# [[1, 2], [3, 4], [0, 1]]

# Random range
from random import randrange
[randrange(1, 7) for _ in range(10)]
# [2, 3, 2, 1, 1, 5, 2, 4, 3, 5]

# Two same conditional list comprehensions
[x for x in range(10) if x % 2 == 0]
# Out: [0, 2, 4, 6, 8]

even_numbers = []
for x in range(10):
    if x % 2 == 0:
        even_numbers.append(x)
print(even_numbers)
# Out: [0, 2, 4, 6, 8]

# Another same example
[2 * (x if x % 2 == 0 else -1) + 1 for x in xrange(10)]
# Out: [1, -1, 5, -1, 9, -1, 13, -1, 17, -1]

numbers = []
for x in range(10):
    if x % 2 == 0:
        temp = x
    else:
        temp = -1
    numbers.append(2 * temp + 1)
print(numbers)
# Out: [1, -1, 5, -1, 9, -1, 13, -1, 17, -1]

# Another example
[x if x > 2 else '*' for x in range(10) if x % 2 == 0]
# Out: ['*', '*', 4, 6, 8]

[x if (x > 2 and x % 2 == 0) else '*' for x in range(10)]
# Out:['*', '*', '*', '*', 4, '*', 6, '*', 8, '*']

# Two same comprehensions with nested loops
data = [[1, 2], [3, 4], [5, 6]]
output = []
for each_list in data:
    for element in each_list:
        output.append(element)
print(output)
# Out: [1, 2, 3, 4, 5, 6]

data = [[1, 2], [3, 4], [5, 6]]
output = [element for each_list in data for element in each_list]
print(output)
# Out: [1, 2, 3, 4, 5, 6]

# Generator expressions
[x**2 for x in range(10)]
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Set comprehensions
# A set containing every value in range(5):
{x for x in range(5)}
# Out: {0, 1, 2, 3, 4}

set(x for x in range(5))
# Out: {0, 1, 2, 3, 4}

# A set of even numbers between 1 and 10:
{x for x in range(1, 11) if x % 2 == 0}
# Out: {2, 4, 6, 8, 10}

# Unique alphabetic characters in a string of text:
text = "When in the Course of human events it becomes necessary for one people..."
{ch.lower() for ch in text if ch.isalpha()}
# Out: set(['a', 'c', 'b', 'e', 'f', 'i', 'h', 'm', 'l', 'o',
#           'n', 'p', 's', 'r', 'u', 't', 'w', 'v', 'y'])

# Comprehensions involving tuples
[x + y for x, y in [(1, 2), (3, 4), (5, 6)]]
# Out: [3, 7, 11]

[x + y for x, y in zip([1, 3, 5], [2, 4, 6])]
# Out: [3, 7, 11]

for x, y in [(1,2), (3,4), (5,6)]:
    print(x+y)
# 3
# 7
# 11

[(x, y) for x, y in [(1, 2), (3, 4), (5, 6)]]
# Out: [(1, 2), (3, 4), (5, 6)]

# Changing types
# Convert a list of strings to integers.
items = ["1","2","3","4"]
[int(item) for item in items]
# Out: [1, 2, 3, 4]
# Convert a list of strings to float.
items = ["1","2","3","4"]
map(float, items)
# Out:[1.0, 2.0, 3.0, 4.0]

# Nested list comprehensions
#List Comprehension with nested loop
[x + y for x in [1, 2, 3] for y in [3, 4, 5]]
#Out: [4, 5, 6, 5, 6, 7, 6, 7, 8]
#Nested List Comprehension
[[x + y for x in [1, 2, 3]] for y in [3, 4, 5]]
#Out: [[4, 5, 6], [5, 6, 7], [6, 7, 8]]

# Example with matrix transpose
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
[[row[i] for row in matrix] for i in range(len(matrix))]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Iterate two or list list simultaneously within list comprehensions
list_1 = [1, 2, 3 , 4]
list_2 = ['a', 'b', 'c', 'd']
list_3 = ['6', '7', '8', '9']
# Two lists
[(i, j) for i, j in zip(list_1, list_2)]
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# Three lists
[(i, j, k) for i, j, k in zip(list_1, list_2, list_3)]
# [(1, 'a', '6'), (2, 'b', '7'), (3, 'c', '8'), (4, 'd', '9')]

# List slicing (selecting parts of lists)
# Using the third "step" argument
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
lst[::2]
# Output: ['a', 'c', 'e', 'g']
lst[::3]
# Output: ['a', 'd', 'g']

# Selecting a sublist from a list
lst = ['a', 'b', 'c', 'd', 'e']
lst[2:4]
# Output: ['c', 'd']
lst[2:]
# Output: ['c', 'd', 'e']
lst[:4]
# Output: ['a', 'b', 'c', 'd']

# Reversing a list with slicing
a = [1, 2, 3, 4, 5]
# steps through the list backwards (step=-1)
b = a[::-1]
# built-in list method to reverse 'a'
a.reverse()
if a = b:
 print(True)
print(b)
# Output:
# True
# [5, 4, 3, 2, 1]
