# In Programming, introspection is the ability to determine the type of an object at runtime.
# This is one of Python's greatest strengths, Everything in python is an object and we can
# examine those objects with built-in python functions and modules.

print("Example 1: dir")
list_1 = [1, 2, 3, 4, 5]
print(dir(list_1))  # this will tell us all the methods we can use on a list
print("You can use this whenever you forget a method name.")

print("\n\nExample 2: type & id")
# type() returns the type of an object and id returns the unique id for various objects
def type_(object):
    print(type(object))

type_("I love you")
type_(143)
type_([])
type_({})
type_(dict)

print(id("I Love You"))

print("\n\nExample 3: Inspect Module")
import inspect
def in_spect(obj):
    print(inspect.getmembers(obj))

print("Use this to check the members of an object")

in_spect(str)
in_spect(int)
in_spect(list_1)
