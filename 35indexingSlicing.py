# basic slicing
a = "abcdef"
a # "abcdef"
  # Same as a[:] or a[::] since it uses the defaults for all three indices
a[-1] # "f"
a[:] # "abcdef"
a[::] # "abcdef"
a[3:] # "def" (from index 3, to end(defaults to size of iterable))
a[:4] # "abcd" (from beginning(default 0) to position 4 (excluded))
a[2:4] # "cd" (from position 2, to position 4 (excluded))
a[::2] # "ace" (every 2nd element)
a[1:4:2] # "bd" (from index 1, to index 4 (excluded), every 2nd element)
a[:-1] # "abcde" (from index 0 (default), to the second last element (last element - 1))
a[:-2] # "abcd" (from index 0 (default), to the third last element (last element -2))
a[-1:] # "f" (from the last element to the end (default len())
a[3:1:-1] # "dc" (from index 2 to None (default), in reverse order)
a[::-1] # "fedcba" (from last element (default len()-1), to first, in reverse order(-1))
a[5:None:-1] # "fedcba" (this is equivalent to a[::-1])
a[5:0:-1] # "fedcb" (from the last element (index 5) to second element (index 1)

# reversing an object
s = 'reverse me!'
s[::-1] # '!em esrever'

# slice assignment
lst = [1, 2, 3]
lst[1:3] = [4, 5]
print(lst) # Out: [1, 4, 5]

lst = [1, 2, 3, 4, 5]
lst[1:4] = [6]
print(lst) # Out: [1, 6, 5]

lst = [1, 2, 3]
lst[:] = [4, 5, 6]
print(lst) # Out: [4, 5, 6]

lst = [1, 2, 3]
lst[-2:] = [4, 5, 6]
print(lst) # Out: [1, 4, 5, 6]

# Making a shallow copy of an array
arr = ['a', 'b', 'c']
copy = arr[:]
arr.append('d')
print(arr) # ['a', 'b', 'c', 'd']
print(copy) # ['a', 'b', 'c']

# basic indexing
arr = ['a', 'b', 'c', 'd']
print(arr[0])
# 'a'
print(arr[1])
# 'b'
print(arr[2])
# 'c'
print(arr[-1])
# 'd'
print(arr[-2])
# 'c'
print arr[6]
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# IndexError: list index out of range
