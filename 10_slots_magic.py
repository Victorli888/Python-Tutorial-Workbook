# By default Python uses a dictionary to store and Object's instance attributes
# Python can't allocate a static amount of memory at object creation to store all attributes SO it uses a-lot of RAM
# if you create a-lot of objects (thousands and millions), There is a way to circumvent this issue.

print("Example 1: Typical way to create a Class")


class Soda(object):
    def __init__(self, name, carbonation, flavor):
        self.name = name
        self.carbonation = carbonation
        self.flavor = flavor
        self.setup()


print("\n Example 2: If instead we used __slots__")


class Soda_2(object):
    __slots__ = ['name', 'carbonation', 'flavor']

    def __init__(self, name, carbonation, flavor):
        self.name = name
        self.carbonation = carbonation
        self.flavor = flavor
        self.setup()

# By using the __slots__ method we can reduce the burden on the RAM  by 40% to 50%. This is done by telling
# Python to not use a dict, and allocate space for a fixed set of attributes, Instead of of allocating all of it.
