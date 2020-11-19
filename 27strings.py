# Formatting
foo = 1
bar = 'bar'
baz = 3.14

print('{}, {} and {}'.format(foo, bar, baz))
# Out: "1, bar and 3.14"
print('{0}, {1}, {2}, and {1}'.format(foo, bar, baz))
# Out: "1, bar, 3.14, and bar"
print('{0}, {1}, {2}, and {3}'.format(foo, bar, baz))
# Out: index out of range error
print("X value is: {x_val}. Y value is: {y_val}.".format(x_val=2, y_val=3))
# Out: "X value is: 2. Y value is: 3."

class AssignValue(object):
    def __init__(self, value):
        self.value = value

my_value = AssignValue(6)
print('My value is: {0.value}'.format(my_value)) # "0" is optional
# Out: "My value is: 6"

my_dict = {'key': 6, 'other_key': 7}
print("My other key is: {0[other_key]}".format(my_dict)) # "0" is optional
# Out: "My other key is: 7"

my_list = ['zero', 'one', 'two']
print("2nd element is: {0[2]}".format(my_list)) # "0" is optional
# Out: "2nd element is: two"

t = (12, 45, 22222, 103, 6)
print '{0} {2} {1} {2} {3} {2} {4} {2}'.format(*t)
# Out: 12 22222 45 22222 103 22222 6 22222

number_list = [12,45,78]
print map('the number is {}'.format, number_list)
# Out: ['the number is 12', 'the number is 45', 'the number is 78']

from datetime import datetime,timedelta
once_upon_a_time = datetime(2010, 7, 1, 12, 0, 0)
delta = timedelta(days=13, hours=8, minutes=20)
gen = (once_upon_a_time + x * delta for x in xrange(5))

print '\n'.join(map('{:%Y-%m-%d %H:%M:%S}'.format, gen))
# Out: 2010-07-01 12:00:00
#      2010-07-14 20:20:00
#      2010-07-28 04:40:00
#      2010-08-10 13:00:00
#      2010-08-23 21:20:00

# Methods
"This is a 'string'.".upper()
# "THIS IS A 'STRING'."
"This IS a 'string'.".lower()
# "this is a 'string'."
"this Is A 'String'.".capitalize() # Capitalizes the first character and lowercases all others
# "This is a 'string'."
"this Is a 'String'".title()
# "This Is A 'String'"
"this iS A STRiNG".swapcase() #Swaps case of each character
# "THIS Is a strIng"
str.upper("This is a 'string'")
# "THIS IS A 'STRING'"
map(str.upper,["These","are","some","'strings'"])
# ['THESE', 'ARE', 'SOME', "'STRINGS'"]

# Translating
translation_table = str.maketrans("aeiou", "12345")
my_string = "This is a string!"
translated = my_string.translate(translation_table)
# Th3s 3s 1 str3ng!

'this syntax is very useful'.translate(None, 'aeiou')
# ths syntx s vry sfl

# Format values into a string
i = 10
f = 1.5
s = "foo"
l = ['a', 1, 2]
d = {'a': 1, 2: 'foo'}
# The following statements are all equivalent
"{} {} {} {} {}".format(i, f, s, l, d)
str.format("{} {} {} {} {}", i, f, s, l, d)
"{0} {1} {2} {3} {4}".format(i, f, s, l, d)
# 10 1.5 foo ['a', 1, 2] {'a': 1, 2: 'foo'}

"I am from Australia. I love cupcakes from Australia!"
"I am from {}. I love cupcakes from {}!".format("Australia", "Australia")
"I am from {0}. I love cupcakes from {0}!".format("Australia")

# Reversing
[char for char in reversed('hello')]
# ['o', 'l', 'l', 'e', 'h']

''.join(reversed('hello'))
# 'olleh'

# Split
"This is a sentence.".split()
# ['This', 'is', 'a', 'sentence.']
" This is a sentence. ".split()
# ['This', 'is', 'a', 'sentence.']
"This is a sentence.".split(' ')
# ['This', 'is', 'a', 'sentence.']
"Earth,Stars,Sun,Moon".split(',')
# ['Earth', 'Stars', 'Sun', 'Moon']
" This is a sentence. ".split(' ')
# ['', 'This', 'is', '', '', '', 'a', 'sentence.', '', '']
"This is a sentence.".split('e')
# ['This is a s', 'nt', 'nc', '.']
"This is a sentence.".split('en')
# ['This is a s', 't', 'ce.']
"This is a sentence.".split('e', maxsplit=0)
# ['This is a sentence.']
"This is a sentence.".split('e', maxsplit=1)
# ['This is a s', 'ntence.']
"This is a sentence.".split('e', maxsplit=2)
# ['This is a s', 'nt', 'nce.']
"This is a sentence.".split('e', maxsplit=-1)
# ['This is a s', 'nt', 'nc', '.']

"This is a sentence.".rsplit('e', maxsplit=1)
# ['This is a sentenc', '.']
"This is a sentence.".rsplit('e', maxsplit=2)
# ['This is a sent', 'nc', '.']

# Replace
"Make sure to foo your sentence.".replace('foo', 'spam')
# "Make sure to spam your sentence."
"It can foo multiple examples of foo if you want.".replace('foo', 'spam')
# "It can spam multiple examples of spam if you want."
"""It can foo multiple examples of foo if you want, \
... or you can limit the foo with the third argument.""".replace('foo', 'spam', 1)
# 'It can spam multiple examples of foo if you want, or you can limit the foo with the third argument.'

# Testing
"Hello World".isalpha() # contains a space
# False
"Hello2World".isalpha() # contains a number
# False
"HelloWorld!".isalpha() # contains punctuation
# False
"HelloWorld".isalpha()
# True

"HeLLO WORLD".isupper()
# False
"HELLO WORLD".isupper()
# True
"".isupper()
# False

"Hello world".islower()
# False
"hello world".islower()
# True
"".islower()
# False

# Every word begins with an uppercase character
"hello world".istitle()
# False
"Hello world".istitle()
# False
"Hello World".istitle()
# True
"".istitle()
#False

# String contains
"foo" in "foo.baz.bar"
# True

# Join
" ".join(["once","upon","a","time"])
# "once upon a time"
"---".join(["once", "upon", "a", "time"])
# "once---upon---a---time"

# Counting number of times a substring appears in a string
s = "She sells seashells by the seashore."
s.count("sh")
# 2
s.count("se")
# 3
s.count("sea")
# 2
s.count("seashells")
# 1

# Test the starting and ending character
s = "This is a test string"
s.startswith("T")
# True
s.startswith("Thi")
# True
s.startswith("thi")
# False
s.startswith("is", 2)
# True
s.startswith(('This', 'That'))
# True
s.startswith(('ab', 'bc'))
# False

s = "this ends in a full stop."
s.endswith('.')
# True
s.endswith('!')
# False
s.endswith('stop.')
# True
s.endswith('Stop.')
# False
s.endswith(('.', 'something'))
# True
s.endswith(('ab', 'bc'))
# False
