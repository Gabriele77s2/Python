from array import *
my_array = array('i', [1,2,3,4,5])
print(my_array[1])
# 2
print(my_array[2])
# 3
print(my_array[0])
# 1

for i in my_array:
    print(i)
# 1
# 2
# 3
# 4
# 5

# Append
my_array = array('i', [1,2,3,4,5])
my_array.append(6)
# array('i', [1, 2, 3, 4, 5, 6])

# Insert
my_array = array('i', [1,2,3,4,5])
my_array.insert(0,0)
#array('i', [0, 1, 2, 3, 4, 5])

# Extend
my_array = array('i', [1,2,3,4,5])
my_extnd_array = array('i', [7,8,9,10])
my_array.extend(my_extnd_array)
# array('i', [1, 2, 3, 4, 5, 7, 8, 9, 10])

# Add items from list into array
my_array = array('i', [1,2,3,4,5])
c=[11,12,13]
my_array.fromlist(c)
# array('i', [1, 2, 3, 4, 5, 11, 12, 13])

# Remove
my_array = array('i', [1,2,3,4,5])
my_array.remove(4)
# array('i', [1, 2, 3, 5])

# Remove last
my_array = array('i', [1,2,3,4,5])
my_array.pop()
# array('i', [1, 2, 3, 4])

# Fetch any element through its index
my_array = array('i', [1,2,3,4,5])
print(my_array.index(5))
# 5
my_array = array('i', [1,2,3,3,5])
print(my_array.index(3))
# 3

# Reverse
my_array = array('i', [1,2,3,4,5])
my_array.reverse()
# array('i', [5, 4, 3, 2, 1])

# Check for number occurrences of an element
my_array = array('i', [1,2,3,3,5])
my_array.count(3)
# 2

# Convert array to string
my_char_array = array('c', ['g','e','e','k'])
# array('c', 'geek')
print(my_char_array.tostring())
# geek

# Convert array to list
my_array = array('i', [1,2,3,4,5])
c = my_array.tolist()
# [1, 2, 3, 4, 5]

# Append a string to char array
my_char_array = array('c', ['g','e','e','k'])
my_char_array.fromstring("stuff")
print(my_char_array)
#array('c', 'geekstuff')

# Multidimensional arrays
lst=[[1,2,3],[4,5,6],[7,8,9]]
print (lst[0])
#output: [1, 2, 3]
print (lst[1])
#output: [4, 5, 6]
print (lst[2])
#output: [7, 8, 9]
print (lst[0][0])
#output: 1
print (lst[0][1])
#output: 2

lst[0]=[10,11,12]
# [[10,11,12],[4,5,6],[7,8,9]]

lst[1][2]=15
# [[10,11,12],[4,5,15],[7,8,9]]

my_array = [[[111,112,113],[121,122,123],[131,132,133]],
            [[211,212,213],[221,222,223],[231,232,233]],
            [[311,312,313],[321,322,323],[331,332,333]]]
print(my_array)
