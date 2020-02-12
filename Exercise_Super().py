# This will be quick exercise with the Super() class function.
# Using super() in Single Inheritance


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return self.length * 2 + self.width * 2


rectangle = Rectangle(3, 2)
print(f'The area of rectangle is: {rectangle.area()}')
print(f'The Perimeter of rectangle is: {rectangle.perimeter()}')


class Square(Rectangle):
    # using the super() we declare that Square inherits from Rectangle Class.
    def __init__(self, length):
        super().__init__(length, length)


square = Square(3)
print(f'The area of square is: {square.area()}')
print(f'The perimeter of square is: {square.perimeter()}')

# Understanding the mechanics of super() - super(P1,P2)
# P1 - subclass P2 - object that is an instance of that subclass
# for example we can use the super() that refers to square --- We'll call it cube


class Cube(Square):

    def surface_area(self):
        face_area = super(Square, self).area()
        return face_area * 6
#  A simple breakdown: Face area of a cube is inherited from the area of Square which is inherited from the area of
#  Rectangle... l*w = rectangle area, square area ; w = l, 6 * square area = surface area.

    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length

# The volume of a square is l*l*l, l*l = face, so face * l = volume


cube = Cube(3)
print(f'The surface area of a cube is: {cube.surface_area()}')
print(f'The volume of a cube is: {cube.volume()}')

print("\n\n\n\nExample2: Super() with Animals")

class Animal:
    def __init__(self, Animal):
        print(Animal, "are a type of animal")

class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'are a warm-blooded animal.')
        super().__init__(mammalName)

class WinglessMammal(Mammal):
    def __init__(self, WinglessMammal):
        print(WinglessMammal,"cannot fly")
        super().__init__(WinglessMammal)

class gilllessMammal(Mammal):
    def __init__(self, gilllessMammal):
        print(gilllessMammal, "cannot breath in water")
        super().__init__(gilllessMammal)

class Horse(WinglessMammal, gilllessMammal):
    def __init__(self):
        print('Horses have hooves')
        super().__init__('horses')

horse = Horse()
print("")
bat = gilllessMammal("bats")




