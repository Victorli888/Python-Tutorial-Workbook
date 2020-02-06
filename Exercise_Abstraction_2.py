# Another example on using the Abstract Class method. Think of this as the Default class that the
# Child class will reference

from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        print("I don't know how many sides I have")


class Triangle(Polygon):
    # This overrides abstract method
    def noofsides(self):
        print("I have 3 sides.")


class Pentagon(Polygon):
    def noofsides(self):
        # overrides abstract method
        print("I have 5 sides.")


class Squartangle(Polygon):
    def noofsides(self):
        # Defaults to abstract method
        super().noofsides()



triangle = Triangle()
triangle.noofsides()

pentagon = Pentagon()
pentagon.noofsides()

squartangle = Squartangle()
squartangle.noofsides()

# Post Exercise Reflection: The act of Abstraction is to reduce the complexity of your code
# for example, imagine creating attack, defence, and Health stats for an object. Realizing that
# its the same element over and over again, you abstract it by making all of them inherit from the same
# parent class that has attack, defence, and health.
