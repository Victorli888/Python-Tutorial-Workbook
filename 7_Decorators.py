# Decorators are... functions which modify the functionality of other functions, Making them shorter and more pythonic
# The following examples are used to help make your code alot more concise

print("Example 1: Understanding functions in python")


def hi(name="Mario"):
    return "it's a me " + name


print(hi())  # outputs: 'hi Mario'
# we can assign functions to a variable
greet = hi
# We don't need to add the (parentheses) because we're not calling on the function, just setting it to a variable

print(greet())  # if we don't add the (parentheses) here we out put: <function hi at 0x02CFA2B0>
del hi
# print(hi()) # if we delete the function hi we output a NameError: name 'hi' is not defined

# BUT, we're able to still call on greet(), this is because the def hi is already commited to the memory of greet()

print(greet("Wario"))

print("\nExample 2: Defining Functions with....Functions")


def hey(name="Luigi"):
    print("its a me" + name + " *Sad Luigi Noises* ")

    def greet_2():
        return "now you are in greet() function"

    def welcome_2():
        return "now you are in the welcome() function"

    print(greet_2())
    print(welcome_2())
    print("now you are back in the hi() function")


hey()

# as you can tell if you call on hey() then, greet() and welcome() are also called. but calling greet() and welcome()
# are not available outside the hi() function

# greet_2()  # this will output: NameError: name 'greet' is not defined
