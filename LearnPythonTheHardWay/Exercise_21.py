def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b
# In essence we're creating a function that will do simple arithmetic, however doing so doesn't create a working value
# We use "return" so that a working value can be used. without it the output would return as nothing
def sub(a, b):
    print(f"subtracting {a} - {b}")
    return a - b


def mult(a, b):
    print(f"multiplying {a} * {b}")
    return a * b


def divide(a, b):
    print(f"dividing {a} / {b}")
    return a / b


print("Let's do some fast maths using functions")
# This is where we begin to use our functions
age = add(30, 5)  # each of these have variables are being used in place of a and b in each function
height = sub(78, 4)  # thanks to return, they all return a value associated with the variables value
weight = mult(90, 2)
iq = divide(100, 2)
#  printing all of our answers we can see that the math was done right.
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
#  if we ran the script again without return we would see the script displays "none"
# Bonus Puzzle

print("Here is a puzzle.")

what = add(age, sub(height, mult(weight, divide(iq, 2))))  # Work Inside-Out

print("That becomes: ", what, "Can you do it by hand?")
