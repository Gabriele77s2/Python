from enum import Enum
class Color(Enum):
    red = 1
    green = 2
    blue = 3

print(Color.red)
# Output: Color.red
print(Color(1))
# Output: Color.red
print(Color['red'])
# Output: Color.red

# Enums are iterable
print([c for c in Color])
# Output: [<Color.red: 1>, <Color.green: 2>, <Color.blue: 3>]
