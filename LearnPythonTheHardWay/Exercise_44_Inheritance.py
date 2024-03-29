# Demonstrating Implicit Inheritance (Is-a) A house is-a Building
class Parent(object):

    def implicit(self):
        print("Parent implicit()")


class Child(Parent):
    pass  # An Empty Class?! What's going to happen if I call on it.

dad = Parent()
son = Child()

dad.implicit()
son.implicit() #  When called it instead calls upon its parent class.
print("\n")
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
print("\n")
# Demonstrate Altering before or after

class Parent2(object):

    def altered(self):
        print("Parent Altered()")


class Child2(Parent2):

    def altered(self):
        print("Child Before Parent altered()")
        super(Child2, self).altered()
        print("Child, After Parent altered()")


dad = Parent2()
son = Child2()

dad.altered()
son.altered()
print("\n")
# Demonstrate all 3 of these examples.

class Parent3(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("Parent implicit()")

    def altered(self):
        print("Parent altered()")

class Child3(Parent3):

    def override(self):
        print("Child override()")

    def altered(self):
        print("Child, Before Parent altered().")
        super(Child3, self).altered()
        print("Child, After Parent altered().")


dad = Parent3()
son = Child3()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
print("\n")

# We can do the all of the above with Composition as well. ( Has-a)
# Quick review of Has-a Is-a  .... A House Is-a Building .... A house has-a Room

class Other4(object):
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child4(object):

    def __init__(self):
        self.other = Other4()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
       print("CHILD, BEFORE OTHER altered()")
       self.other.altered()
       print("CHILD, AFTER OTHER altered")

son = Child4()

son.implicit()
son.override()
son.altered()