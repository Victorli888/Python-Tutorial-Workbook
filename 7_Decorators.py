# Decorators are... functions which modify the functionality of other functions, Making them shorter and more pythonic
# The following examples are used to help make your code alot more concise
# We use decorators to execute code before and after a function

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
print("\nExample 3: Returning functions from within functions")


def hi3(name="superman"):
    def greet3():
        return "now you are in the greet3 function"

    def welcome3():
        return "now you are in the welcome3 function"

    if name == "superman":
        return greet3
    else:
        return welcome3  # we don't add the () at the ends of these because ()-- at the end executes the function
    # if we leave it off we're able to pass them around and assign them to other variables without executing them


a = hi3()  # by default, hi3() = hi3(name="superman") and thus it enters the hi3 function, but without another pair of
# (parenthesis) then the we're not able to execute the functions in the function
# by changing hi3() to hi3(name="regularman") then we return our else statement or welcome3

print(a)  # this will output  <function greet at 0x7f213c01500 --- This is why this "error" message displays
print(a())  # this will print the expected outcome


print("\nExample 4: Giving a function as an argument to another function:")
#  we can use the argument of a function to call on another function

def hi4():
    return "General Kenobi, YOU ARE A BOLD ONE."

def doSomethingBeforeHi(func):
    print("Why, Hello there (͡° ͜ʖ ͡°)")
    print(func)


doSomethingBeforeHi(hi4())

print("\nExample 5: writing a decorator")

def decorator4(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I'm now doing work after executing a_func()")
    return wrapTheFunction()


def a_function_requiring_decoration():
    print("I need a decoration")


a_function_requiring_decoration()  # Outputs: "I need a decoration"
print("Now let's wrap that string into decorator4 function\n")


a_function_requiring_decoration = decorator4(a_function_requiring_decoration)
# a_function_requiring_decoration is wrapped by WrapTheFunction()
# HOW DO I SET A FUNCTION WITH AN ARGUMENT FUNCTION TO A VARIABLE WITHOUT CALLING IT

a_function_requiring_decoration()  # I DON'T NEED THIS BUT I DON't KNOW WHY
# outputs: I am doing som boring work before executing a_func()
#          I am doing work after executing a_func()
#          I am doing some boring work after executing a_func()


# I need to figure out when I should use parenthesis when calling a function
# https://stackoverflow.com/questions/9768865/python-nonetype-object-is-not-callable-beginner