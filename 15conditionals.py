def my_function():      # This is a function definition. Note the colon (:)
    a = 2               # This line belongs to the function because it's indented
    return a            # This line also belongs to the same function
print(my_function())    # This line is OUTSIDE the function block

if a > b:       # If block starts here
    print(a)    # This is part of the if block
else:           # else must be at the same level as if
    print(b)    # This line is part of the else block

if a > b: print(a)
else: print(b)

if x > y: y = x
    print(y)                    # IndentationError: unexpected indent
if x > y: while y != z: y -= 1  # SyntaxError: invalid syntax

def will_be_implemented_later():    #An empty block causes an IndentationError . Use pass when you have a block with no content
    pass

# If, elif, else
n = 5
print("Greater than 2" if n > 2 else "Smaller than or equal to 2")
# Out: Greater than 2
print("Hello" if n > 10 else "Goodbye" if n > 5 else "Good day")
# Output: Good day

number = 5
if number > 2:
    print("Number is bigger than 2.")
elif number < 2:
    print("Number is smaller than 2.")
else:
    print("Number is 2.")
# Output: Number is bigger than 2.

a = 1
b = 6
if a and b > 2:     # if one of them is true, then it is true
    print('yes')
else:
    print('no')
# Output: yes

if a > 2 and b > 2:
    print('yes')
else:
    print('no')
# Output: no

a = 1
if a == 3 or a == 4 or a == 6:  # each comparison must be made separetely, if a == 4 or 6 or 8 is not valide
    print('yes')
else:
    print('no')
# Output: no

if a in (3, 4, 6):
    print('yes')
else:
    print('no')
# Output: no

if True:
    print("It is true!")
else:
    print("This won't get printed..")
# Output: It is true!

if False:
    print("This won't get printed..")
else:
    print("It is false!")
# Output: It is false!

if 2 + 2 == 4:
    print("I know math!")
# Output: I know math!
