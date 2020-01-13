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

