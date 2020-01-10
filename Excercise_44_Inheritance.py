# Demonstrating Implicit Inheritance
class Parent(object):

    def implicit(self):
        print("Parent implicit()")


class Child(Parent):
    pass  # An Empty Class?! What's going to happen if I call on it.

dad = Parent()
son = Child()

dad.implicit()
son.implicit() #  When called it instead calls upon its parent class.

# Demonstrating Override Explicitly
class Parent1(object):

    def overide(self):
        print("Parent override()")
    def inher(self):
        print(" I don't have anything so I Inherited from Parent1")

class Child1(Parent1):
    def overide(self):
        print("Child override()")

class Child2(Parent1):
    pass

class Gchild(Child1):
    pass

dad = Parent1()
son = Child1()
daughter = Child2()
son_of_son = Gchild()

dad.overide()
son.overide()
son.inher()  # Inherit from Parent class
daughter.inher()  # Inherit from same parent class
son_of_son.inher() # Double inheritance?


