# Template that defines the basic characteristics of a particular object
class Person(object):
    """A simple class."""   # docstring
    species = "Homo Sapiens" # class attribute

    def __init__(self, name):   # special method
        """This is the initializer. It's a special method (see below)"""
        self.name = name # instance attribute

    def __str__(self):  # special method
        """This method is run when Python tries
        to cast the object to a string. Return
        this string when using print(), etc."""
        return self.name

    def rename(self, renamed):  # regular method
        """Reassign and print the name attribute."""
        self.name = renamed
        print("Now my name is {}".format(self.name))

# Instances
kelly = Person("Kelly")
joseph = Person("Joseph")
john_doe = Person("John Doe")

# Attributes
kelly.species
'Homo Sapiens'
john_doe.species
'Homo Sapiens'
joseph.species
'Homo Sapiens'
kelly.name
'Kelly'
joseph.name
'Joseph'

# Methods
john_doe.__str__()
'John Doe'
print(john_doe)
'John Doe'
john_doe.rename("John")
'Now my name is John'

# Bound, unbound, static methods
class A(object):
    def f(self, x):
        return 2 * x
a = A()
A.f(a, 20)
# 40
a.f(2)
# 4

class D(object):
    multiplier = 2

    @classmethod
    def f(cls, x):
        return cls.multiplier * x

    @staticmethod
    def g(name):
        print("Hello, %s" % name)
D.f
# <bound method type.f of <class '__main__.D'>>
D.f(12)
# 24
D.g
# <function D.g at ...>
D.g("world")
# Hello, world

# Basic inheritance
class BaseClass(object):
    pass
class DerivedClass(BaseClass):
    pass

class Rectangle():
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

class Square(Rectangle):
    def __init__(self, s):
        # call parent constructor, w and h are both s
        super(Square, self).__init__(s, s)
        self.s = s
r.area()
# Output: 12
r.perimeter()
# Output: 14
s.area()
# Output: 4
s.perimeter()
# Output: 8

# issubclass(DerivedClass, BaseClass): returns True if DerivedClass is a subclass of the BaseClass
# isinstance(s, Class): returns True if s is an instance of Class or any of the derived classes of Class
# subclass check
issubclass(Square, Rectangle)
# Output: True

# instantiate
r = Rectangle(3, 4)
s = Square(2)
isinstance(r, Rectangle)
# Output: True
isinstance(r, Square)
# Output: False
# A rectangle is not a square
isinstance(s, Rectangle)
# Output: True
# A square is a rectangle
isinstance(s, Square)
# Output: True

# Monkey patching
class A(object):
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return A(self.num + other.num)

def get_num(self):
    return self.num

foo = A(42)
A.get_num = get_num
bar = A(6);
foo.get_num() # 42
bar.get_num() # 6

# New style
class MyClass:
    pass

my_inst = MyClass()
type(my_inst)
# <class '__main__.MyClass'>
my_inst.__class__
# <class '__main__.MyClass'>
issubclass(MyClass, object)
# True

# Class methods: alternate initializers
class Person(object):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name

    @classmethod
    def from_full_name(cls, name, age):
        if " " not in name:
            raise ValueError
        first_name, last_name = name.split(" ", 2)
        return cls(first_name, last_name, age)

    def greet(self):
        print("Hello, my name is " + self.full_name + ".")

bob = Person("Bob", "Bobberson", 42)
alice = Person.from_full_name("Alice Henderson", 31)
bob.greet()
# Hello, my name is Bob Bobberson.
alice.greet()
# Hello, my name is Alice Henderson.

# Multiple inheritance
class Foo(object):
    foo = 'attr foo of Foo'

class Bar(object):
    foo = 'attr foo of Bar' # we won't see this.
    bar = 'attr bar of Bar'

class FooBar(Foo, Bar):
    foobar = 'attr foobar of FooBar'

fb = FooBar()
fb.foo
# attr foo of Foo

class Foo(object):
    def foo_method(self):
        print("foo Method")

class Bar(object):
    def bar_method(self):
        print("bar Method")

class FooBar(Foo, Bar):
    def foo_method(self):
        super(FooBar, self).foo_method()

    class Foo(object):
        def __init__(self):
            print("foo init")

    class Bar(object):
        def __init__(self):
            print("bar init")

    class FooBar(Foo, Bar):
        def __init__(self):
            print("foobar init")
            super(FooBar, self).__init__()

    a = FooBar()
# foobar init
# foo init
print isinstance(a,FooBar)
print isinstance(a,Foo)
print isinstance(a,Bar)
# True
# True
# True

# Properties
class Character(object):
    def __init__(name, max_hp):
        self._name = name
        self._hp = max_hp
        self._max_hp = max_hp

    # Make hp read only by not providing a set method
    @property
    def hp(self):
        return self._hp

    # Make name read only by not providing a set method
    @property
    def name(self):
        return self.name

    def take_damage(self, damage):
        self.hp -= damage
        self.hp = 0 if self.hp <0 else self.hp

    @property
    def is_alive(self):
        return self.hp != 0

    @property
    def is_wounded(self):
        return self.hp < self.max_hp if self.hp > 0 else False

    @property
    def is_dead(self):
        return not self.is_alive

bilbo = Character('Bilbo Baggins', 100)
bilbo.hp
# out : 100
bilbo.hp = 200
# out : AttributeError: can't set attribute
# hp attribute is read only.
bilbo.is_alive
# out : True
bilbo.is_wounded
# out : False
bilbo.is_dead
# out : False
bilbo.take_damage( 50 )
bilbo.hp
# out : 50
bilbo.is_alive
# out : True
bilbo.is_wounded
# out : True
bilbo.is_dead
# out : False
bilbo.take_damage( 50 )
bilbo.hp
# out : 0
bilbo.is_alive
# out : False
bilbo.is_wounded
# out : False
bilbo.is_dead
# out : True

# Default values for instance variables
class Rectangle(object):
    def __init__(self, width, height, color='blue'):
        self.width = width
        self.height = height
        self.color = color

    def area(self):
        return self.width * self.height

# Create some instances of the class
default_rectangle = Rectangle(2, 3)
print(default_rectangle.color) # blue
red_rectangle = Rectangle(2, 3, 'red')
print(red_rectangle.color) # red

class Rectangle2D(object):
    def __init__(self, width, height, pos=[0,0], color='blue'):
        self.width = width
        self.height = height
        self.pos = pos
        self.color = color

r1 = Rectangle2D(5,3)
r2 = Rectangle2D(7,8)
r1.pos[0] = 4
r1.pos # [4, 0]
r2.pos # [4, 0] r2's pos has changed as well

class Rectangle2D(object):
    def __init__(self, width, height, pos=None, color='blue'):
        self.width = width
        self.height = height
        self.pos = pos or [0, 0] # default value is [0, 0]
        self.color = color

r1 = Rectangle2D(5,3)
r2 = Rectangle2D(7,8)
r1.pos[0] = 4
r1.pos # [4, 0]
r2.pos # [0, 0] r2's pos hasn't changed

# Class and instance variables
class C:
    x = 2 # class variable
    def __init__(self, y):
        self.y = y # instance variable

C.x
# 2
C.y
# AttributeError: type object 'C' has no attribute 'y'
c1 = C(3)
c1.x
# 2
c1.y
# 3
c2 = C(4)
c2.x
# 2
c2.y
# 4
c2.x = 4
c2.x
# 4
C.x
# 2

class D:
    x = []
    def __init__(self, item):
        self.x.append(item) # note that this is not an assignment!

d1 = D(1)
d2 = D(2)
d1.x
# [1, 2]
d2.x
# [1, 2]
D.x
# [1, 2]

# Class composition
class Country(object):
    def __init__(self):
        self.cities=[]

    def addCity(self,city):
        self.cities.append(city)

class City(object):
    def __init__(self, numPeople):
        self.people = []
        self.numPeople = numPeople

    def addPerson(self, person):
        self.people.append(person)

    def join_country(self,country):
        self.country = country
        country.addCity(self)

        for i in range(self.numPeople):
            person(i).join_city(self)

class Person(object):
    def __init__(self, ID):
        self.ID=ID

    def join_city(self, city):
        self.city = city
        city.addPerson(self)

    def people_in_my_country(self):
        x = sum([len(c.people) for c in self.city.country.cities])
        return x

US=Country()
NYC=City(10).join_country(US)
SF=City(5).join_country(US)

print(US.cities[0].people[0].people_in_my_country())
# 15

# Singleton
@Singleton
class Single:
    def __init__(self):
        self.name=None
        self.val=0

    def getName(self):
        print(self.name)

x = Single.Instance()
y = Single.Instance()
x.name = 'I\'m single'
x.getName() # outputs I'm single
y.getName() # outputs I'm single

# Metaclasses
Dummy = type('OtherDummy', (), dict(x=1))
Dummy.__class__ # <type 'type'>
Dummy().__class__.__class__ # <type 'type'>

class mytype(type):
    def __init__(cls, name, bases, dict):
        # call the base initializer
        type.__init__(cls, name, bases, dict)
        # perform custom initialization...
        cls.__custom_attribute__ = 2

MyDummy = mytype('MyDummy', (), dict(x=2))
MyDummy.__class__ # <class '__main__.mytype'>
MyDummy().__class__.__class__ # <class '__main__.mytype'>
MyDummy.__custom_attribute__ # 2
