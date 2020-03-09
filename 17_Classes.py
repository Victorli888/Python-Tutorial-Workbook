print("Example 1: Instance & Class Variables")
# Instance variables for data which is unique to every object
# Class variables for data shared between different instances of a class


class Calculate_area():
    # Pi is a class variable
    pi = 3.142

    def __init__(self, radius):
        # self.radius is an instance variable
        self.radius = radius

    def area_circle(self):
        return self.pi * (self.radius ** 2)



a = Calculate_area(3)  # Calculate the area
ans = (a.area_circle())
print(f"The area of a circle with a radius of 32 is {ans}")
print(a.pi)  # output: 3.142; We can call upon the specific class variable in Calculate_area module
a.pi = 0  # output: 0; we can also set the class variable to a different value.
print(a.pi)

print("\nThe incorrect usage of Instance & Class variables.")


class SuperHero(object):
    superpowers = []

    def __init__(self, name):
        self.name = name

    def add_superpower(self, power):
        self.superpowers.append(power)


foo = SuperHero('foo')
bar = SuperHero('bar')

print(f"1.{foo.name}\n2.{bar.name}")
foo.add_superpower('fly')
print(f"1.{foo.superpowers}\n2.{bar.superpowers}")
# As you can see foo.superpowers & bar.superpowers share the same list. So when you mutate the class you change the
# variables to all variables related to that module.

print(""""\n\n\nMagic Methods" __init__ & __getitem__\n""")
# the __init__ function is a class initializer which means when that instance of the class is created then the __init__
# method is called too.

# We'll have two examples one two show case __init__ and one two show you can pass arguments into it as well.

class Init_1(object):
    def __init__(self):
        print("Hello! I generate every time the Class is called")

    def another_method(self):
        print("I am another method that isn't automatically called")


class Init_2(object):  # this one will have the argument in the __init__ method
    def __init__(self, donut_type, quantity):
        print(f"Suprise! You get {quantity} {donut_type} donuts today.")

    def another_method(self):
        print("I am the donut that isn't automatically called")

Init_1()
Init_1.another_method("print")
print("------------------------------")
Init_2("chocolate", 3)
Init_2.another_method("print me")
print("\nLets move onto getitem\n")
# using getitem in a class allows its instances to use the [] (indexer) operator


class Getitem(object):
    def __init__(self):
        self.info = {
            'name': 'Victor',
            'country': 'USA',
            'ID': 8000403143
        }

    def __getitem__(self, item):
        return self.info[item]

foo = Getitem()

print(f"Hello I am {foo['name']}, I am from the {foo['country']} and my badge number is {foo['ID']}")

# without the __getitem__ "Magic Method" we would run into this issue:

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'GetTest' object has no attribute '__getitem__'
