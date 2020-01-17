# Encapsulation is the act of containing the methods and data of an object to its self.
# restricting access to this prevents accidental modifications from other object. (Like a Class)

print("Example 1: Protected Members")  # protected members


class Espresso:
    def __init__(self):
        self._a = "espresso"  # with the _ (underscore) I've created a protected member


class Latte(Espresso):
    def __init__(self):
        Espresso.__init__(self)
        print(f"Calling upon the Protected member: ", self._a)


espresso = Espresso()
# Calling the protected member outside the class will result in an AttributeError
# print(espresso.a) # This will fail, but if you comment this line out. code will work.
# but as long as you call it wit the _ symbol then error will not occur
print(espresso._a)
latte = Latte()

print("\nExample 2: Private members")
class Parent:
    def __init__(self):
        self.a = "Public"
        self.__b = "Private"

class Child(Parent):
    def __init__(self):
        # calling on the constructor/Initializer/__init__ for Base class
        Parent.__init__(self)
        print("Calling Private Member of the parent class")
        print(self.__b)

# Driver code

papa = Parent()
print(papa.a)
# print(papa.__b) Attribute Error
# son = Child() Attribute Error
# print(papa.b) Attribute Error

# THE DIFFERENCE?
# Private can only be accessed through the class. End of Story
# Protected can be accessed aslong as you add the _ underscore along side the variable
print("\n Example 3: Magneto wants to trick Professor X by thinking the oppisite of his intentions ")
class Magneto:
    def __init__(self):
        self.say = "Hello Charles"
        # self.__Athink = "I'm going to stab you in the back"  # Attribute Error
        self._Bthink = "I'll fight with you"


class Xavier(Magneto):
    def __init__(self):
        print("This is what Xavier mind reads:")
        Magneto.__init__(self)
        print(self.say)
        print(self._Bthink)
        # print(self.__Athink)  # Attribute Error (Xavier can't read it)

magneto = Magneto()
xavier = Xavier()

print("\nThis is what Magneto is thinking and saying")
print(magneto.say)
print(magneto._Bthink)

print("\nThis is what Xavier says he mind read.")
print(xavier.say)
print(xavier._Bthink)

print("\n Example 4: Private Member application")
# By using private members I can do math in a class and make sure that nothing else in the code
# will mess with it in the future.


class Mental_Math:
    def __init__(self):
        self.__food = 5.00 + 1.79 + .79
        self.__tips = self.__food *.15
        self.total_cost = self.__food + self.__tips


class show(Mental_Math):
    def __init__(self):
        Mental_Math.__init__(self)
        print("The total bill costs:", self.total_cost, "USD")


do_math = show()
