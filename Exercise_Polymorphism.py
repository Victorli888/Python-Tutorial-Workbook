# Polymorphism (to Have many forms) to a programmer it means to have a function with the same name but
# is used for different types

print("Example 1 : len() (in-built function)")
# len() on a string
print(len("Polymorphism"))

# len() on a list
print(len([10, 20, 30]))

# Both share the same function but len() is used on two different data types.

print("\nExample 2: User defined functions")


def add(x, y, z = 0):
    return x + y + z


print(add(2, 5))
print(add(2, 3, 4))

print('\nExample 3: Class method Polymorphism')  # Class based Polymorphism


class China():

    def name(self):
        return "CHINA"

    def capital(self):
        print("Bejing")

    def language(self):
        print("Mandarin")

    def continent(self):
        print("Asia")


class USA():

    def name(self):
        return ("USA")

    def capital(self):
        print('Washington D.C.')

    def language(self):
        print("English")

    def continent(self):
        print('North America')


usa = USA()
china = China()

for country in (usa, china):
    print(f'\nHere are some keywords for {country.name()}')
    country.capital()
    country.language()
    country.continent()

print("\n Example 3.5: Polymorphism with Functions & Objects")
# You could same thing but instead of a for loop at the end you can call on each of objects with a function


def func(obj):
    print(f'\nHere are som e keywords for {obj.name()}')
    obj.capital()
    obj.language()
    obj.continent()


func(usa)
func(china)


print("\n Example 4: Polymorphism with inheritance")  # Method Overriding


class Fighting():
    def intro(self):
        print("There are several fight styles that utilize kicks")

    def kicks(self):
        print("Many forms of martial arts utilize kicks but not all of them.")


class Boxing(Fighting):
    def kicks(self):
        print("Boxing does not utilize kicks")

class Kickboxing(Fighting):
    def kicks(self):
        print("Kick-Boxing Utilizes kicks")

fighting = Fighting()
boxing = Boxing()
kick_boxing = Kickboxing()
print("\n")
fighting.intro()
fighting.kicks()
print("\n")
boxing.intro()
boxing.kicks()
print("\n")
kick_boxing.intro()
kick_boxing.kicks()
