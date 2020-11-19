import datetime
today = datetime.datetime.now()
print(str(today))
# Output: 2016-09-15 06:58:46.915000
print(repr(today))
# Output: datetime.datetime(2016, 9, 15, 6, 58, 46, 915000)

# When writing a class, you can override these methods to do whatever you want
class Represent(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return "Represent(x={},y=\"{}\")".format(self.x, self.y)
    def __str__(self):
        return "Representing x as {} and y as {}".format(self.x, self.y)

r = Represent(1, "Hopper")
print(r)
# Output: Representing x as 1 and y as Hopper
print(r.__repr__)
# Output: <bound method Represent.__repr__ of Represent(x=1,y="Hopper")>

# Sets the execution of __repr__ to a new variable
rep = r.__repr__()
print(rep)
# Output: Represent(x=1,y="Hopper")
r2 = eval(rep)      # evaluates rep
print(r2)           # prints __str__ from new object
# Output: Representing x as 1 and y as Hopper
print(r2 == r)      # prints 'False' because they are different objects
