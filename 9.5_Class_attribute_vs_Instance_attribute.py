# In object oriented programing Python provides two scopes for attributes: Class and Instance
# instance attribute is Python variable belonging to one and only one object.
# Class attribute belongs to the class rather than a particular object. It is shared with the objects in the class

# instance attributes--- defined inside the constructor function, __init__(self, ...) of the class.
# Class attributes -- will be defined outside of the constructor function of the class.
print("Instance vs Class Attributes\n")
class ExampleClass(object):
    class_attr = "I am the class Attribute" # this is accessible property of the Class and any object in the class

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr  # this is only accessible from the scope of the object


if __name__ == '__main__':  # if this is the " main file script", Basically a check to see if it is being import script
    foo = ExampleClass(1)
    bar = ExampleClass(2)

print(foo.instance_attr)  # output: 1
print(bar.instance_attr)  # output: 2
print(ExampleClass.class_attr)  # output: "I am the class Attribute"
print(bar.class_attr)  # output: "I am the class Attribute"
print(foo.class_attr)  # output: "I am the class Attribute"

# print(ExampleClass.instance_attr)  # Running this will fail saying "ExampleClass has no attribute instance_attr"
#  which makes sense because the class it self doesn't actually have an instance attribute.

print("\n Bonus Example: __name__ = '__main__'")
# Take for example if I write this code,
print("If I were to run the following code in this module then You'll see that it would say:")  # Run Directly

if __name__ == '__main__':
    print("Run Directly")
else:
    print("Run from Import")

# If I were to run import this to a different Python file it would run the else statement.
# This is because by default the native python file sets a variable __name__ to '__main__' by default.

