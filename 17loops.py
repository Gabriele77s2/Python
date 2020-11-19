# Break in while
i = 0
while i < 7:
    print(i)
    if i == 4:
        print("Breaking from loop")
        break
    i += 1
# 0
# 1
# 2
# 3
# 4
# Breaking from loop

# Break in for
for i in (0, 1, 2, 3, 4):
    print(i)
    if i == 2:
        break
# 0
# 1
# 2

# Continue
for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i)
# 0
# 1
# 3
# 5

# Nested
while True:
    for i in range(1,5):
        if i == 2:
            break # Will only break out of the inner loop!



# Return
def break_loop():
    for i in range(1, 5):
        if (i == 2):
            return(i)
        print(i)
    return(5)


def break_all():
    for j in range(1, 5):
        for i in range(1, 4):
            if i*j == 6:
                return(i)
            print(i*j)
1 # 1*1
2 # 1*2
3 # 1*3
4 # 1*4
2 # 2*1
4 # 2*2
# return because 2*3 = 6, the remaining iterations of both loops are not executed

# Two same for loops
for i in [0, 1, 2, 3, 4]:
    print(i)
# 0
# 1
# 2
# 3
# 4

# Iterating over lists
for i in range(5):
 print(i)

for x in ['one', 'two', 'three', 'four']:
 print(x)
# one
# two
# three
# four

# Range
for x in range(1, 6):
    print(x)
# 1
# 2
# 3
# 4
# 5

# Enumerate
for index, item in enumerate(['one', 'two', 'three', 'four']):
    print(index, ':', item)
# (0, ':', 'one')
# (1, ':', 'two')
# (2, ':', 'three')
# (3, ':', 'four')

# Two same loops with else
for i in range(3):
    print(i)
else:
    print('done')

i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('done')
# 0
# 1
# 2
# done

# With else and break
for i in range(2):
    print(i)
    if i == 1:
        break
else:
    print('done')
# 0
# 1

a = [1, 2, 3, 4]
for i in a:
    if type(i) is not int:
        print(i)
        break
else:
    print("no exception")
# no exception

# Iterating over dictionaries
d = {"a": 1, "b": 2, "c": 3}
for key in d.keys():
    print(key)
# a
# b
# c
for value in d.values():
    print(value)
# 1
# 2
# 3
for key, value in d.items():
    print(key, ":", value)
# a : 1
# b : 2
# c : 3

# Half loop
a = 10
while True:
    a = a - 1
    print(a)
    if a < 7:
        break
print('Done')
# 9
# 8
# 7
# 6
# Done

# Iterating different portion of a list
lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']
for s in lst:
    print s[:1] # print the first letter
# a
# b
# c
# d
# e

for idx, s in enumerate(lst):
    print("%s has an index of %d" % (s, idx))
# alpha has an index of 0
# bravo has an index of 1
# charlie has an index of 2
# delta has an index of 3
# echo has an index of 4

for s in lst[1::2]:
    print(s)
# bravo
# delta
