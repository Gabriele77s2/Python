# Duck Typing
class Duck:
    def quack(self):
        print("Quaaaaaack!")

    def feathers(self):
        print("The duck has white and gray feathers.")

class Person:
    def quack(self):
        print("The person imitates a duck.")

    def feathers(self):
        print("The person takes a feather from the ground and shows it.")

    def name(self):
        print("John Smith")

    def in_the_forest(obj):
        obj.quack()
        obj.feathers()

donald = Duck()
john = Person()
in_the_forest(donald)
in_the_forest(john)
# Quaaaaaack!
# The duck has white and gray feathers.
# The person imitates a duck.
# The person takes a feather from the ground and shows it.

# Basic Polymorphism
class Shape:
    # This is a parent class that is intended to be inherited by other classes
    def calculate_area(self):
    # This method is intended to be overridden in subclasses.
    # If a subclass doesn't implement it but it is called, NotImplemented will be raised.
    raise NotImplemented

class Square(Shape):
    # This is a subclass of the Shape class, and represents a square
    side_length = 2 # in this example, the sides are 2 units long
    def calculate_area(self):
        """
        This method overrides Shape.calculate_area(). When an object of type
        Square has its calculate_area() method called, this is the method that
        will be called, rather than the parent class' version.
        It performs the calculation necessary for this shape, a square, and
        returns the result.
        """
        return self.side_length * 2

class Triangle(Shape):
    # This is also a subclass of the Shape class, and it represents a triangle
    base_length = 4
    height = 3

    def calculate_area(self):
        """
        This method also overrides Shape.calculate_area() and performs the area
        calculation for a triangle, returning the result.
        """
        return 0.5 * self.base_length * self.height

    def get_area(input_obj):
        """
        This function accepts an input object, and will call that object's
        calculate_area() method. Note that the object type is not specified. It
        could be a Square, Triangle, or Shape object.
        """
        print(input_obj.calculate_area())

# Create one object of each class
shape_obj = Shape()
square_obj = Square()
triangle_obj = Triangle()
# Now pass each object, one at a time, to the get_area() function and see the result.
get_area(shape_obj)
get_area(square_obj)
get_area(triangle_obj)
# None
# 4

# What happens without polymorphism?
class Square:
    side_length = 2

    def calculate_square_area(self):
        return self.side_length ** 2

class Triangle:
    base_length = 4
    height = 3

    def calculate_triangle_area(self):
        return (0.5 * self.base_length) * self.height

    def get_area(input_obj):
        # Notice the type checks that are now necessary here. These type checks
        # could get very complicated for a more complex example, resulting in
        # duplicate and difficult to maintain code.
        if type(input_obj).__name__ == "Square":
            area = input_obj.calculate_square_area()
        elif type(input_obj).__name__ == "Triangle":
            area = input_obj.calculate_triangle_area()
        print(area)

# Create one object of each class
square_obj = Square()
triangle_obj = Triangle()
# Now pass each object, one at a time, to the get_area() function and see the
# result.
get_area(square_obj)
get_area(triangle_obj)
# 4
# 6.0

# Method Overriding
class Parent(object):
    def introduce(self):
        print("Hello!")

    def print_name(self):
        print("Parent")

class Child(Parent):
    def print_name(self):
        print("Child")

p = Parent()
c = Child()
p.introduce()
p.print_name()
c.introduce()
c.print_name()

$ python basic_override.py
# Hello!
# Parent
# Hello!
# Child
