# type() simply returns the type of object i.e ("blah blah") returns as <class 'str'>
# isinstance() checks if an object is a certain type i.e isinstance("blah blah", str) returns True
print("Example 1: Type vs isinstance")
print(type("Blah Blah"))
print(isinstance("blah", str))


print("\nExample 2: isinstance")# isinstance takes into consideration for Inheritance
class Animal():
    def walk(self):
        print("I'm moving")

    def eat(self):
        print("I'm eating")


class Dog(Animal):

    def bork(self):
        print("bork bork")


class Cat(Animal):

    def meow(self):
        print("meow meow")


dog = Dog()
cat = Cat()

if isinstance(cat, Dog):
    cat.meow()
else:
    print("cat is not an instance of Dog")
if isinstance(dog, Animal):
    dog.bork()
else:
    print("dog is not an instance of Animal")
# Type is only really used for debugging and checks
print("\nExample 3: why not to use type")
print("type(cat) = ", type(cat))
print("type(dog) = ", type(dog))
print("type(Animal) = ", type(Animal))

if type(cat) == Dog:
    cat.meow()
else:
    print("cat is not an instance of Dog")
if type(dog) == Animal:
    dog.bork()
else:
    print("dog is not an instance of Animal")

# As you can tell since type(Animal) and type(dog) do not return the same statement they both fail even
# though we're trying to test whether or not they are the "same type" of class.
