# Lists,  not hashable; mutable
# Hashable = An object is hashable if its value never changes during its lifetime
int_list = [1, 2, 3]
string_list = ['abc', 'defghi']

# Types of list
empty_list = []
mixed_list = [1, 'abc', True, 2.34, None]
nested_list = [['a', 'b', 'c'], [1, 2, 3]]

# Indexing
names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
print(names[0])
# Output: Alice
print(names[2])
# Output: Craig
print(names[-1])
# Output: Eric
print(names[-4])
# Output: Bob

names[0] = 'Ann'
print(names)
# Output: ['Ann', 'Bob', 'Craig', 'Diana', 'Eric']

# Operations
names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
names.append("Sia")
print(names)
# Output: ['Alice', 'Bob', 'Craig', 'Diana', 'Eric', 'Sia']

names.insert(1, "Nikki")
print(names)
# Output: ['Alice', 'Nikki', 'Bob', 'Craig', 'Diana', 'Eric', 'Sia']

names.remove("Bob")
print(names)
# Output: ['Alice', 'Nikki', 'Craig', 'Diana', 'Eric', 'Sia']

# Remove default to the last item
names.pop()
print(names)
# Output: 'Sia'

print(names.index("Alice"))
# Output: 0

print(len(names))
# Output: 6

a = [1, 1, 1, 2, 3, 4]
print(a.count(1))
# Output: 3

a.reverse()
print(a)
# Output: [4, 3, 2, 1, 1, 1]

# Can iterate over the list elements like below
for element in my_list:
    print (element)

# Tuples, supports indexing; immutable; hashable if all its members are hashable
# Same rules of the lists
ip_address = ('10.20.30.40', 8080)

# There is a comma after "member',)" because otherwise it would be a variable
one_member_tuple = ('Only member',)        # With brackets
one_member_tuple = 'Only member',          # No brackets
one_member_tuple = tuple(['Only member'])  # Tuple syntax

# Dictionaries, keys hashable
# key : value
state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanta'
}

ca_capital = state_capitals['California']
print(ca_capital)
# Output: Sacramento

# Can get all of the keys in a dictionary and then iterate over them:
for k in state_capitals.keys():
    print('{} is the capital of {}'.format(state_capitals[k], k))
# Output: Little Rock is the capital of Arkansas
#         Denver is the capital of Colorado
#         Sacramento is the capital of California
#         Atlanta is the capital of Georgia

# Set, hashable
# No repeats and no insertion order but sorted order
# It is used when it is only important that some things are grouped together
first_names = {'Adam', 'Beth', 'Charlie'}

# Can build a set using an existing list
my_list = [1,2,3]
my_set = set(my_list)

# Check membership of the set using 'in'
print('Adam' in first_names)
# Output: True

# No insertion order but sorted order
for i in first_names:
    print(i)

# Defaultdict
# Set a default value if the key does not exist
state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanta'
}

print(state_capitals['Alabama'])
# Output: Traceback (most recent call last):
#         File "<ipython-input-61-236329695e6f>", line 1, in <module>
#         state_capitals['Alabama']
#         KeyError: 'Alabama'

# Now I set a default value 'Boston' in case the key does not exist
from collections import defaultdict
state_capitals = defaultdict(lambda: 'Boston')

# Must rewriting them otherwise at 'Arkansas' will print 'Boston' instead of 'Little Rock'
state_capitals['Arkansas'] = 'Little Rock'
state_capitals['California'] = 'Sacramento'
state_capitals['Colorado'] = 'Denver'
state_capitals['Georgia'] = 'Atlanta'

print(state_capitals['Alabama'])
# Output: 'Boston'

print(state_capitals['Arkansas'])
# Output: 'Little Rock'
