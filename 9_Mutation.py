# to simply put it Mutable means able to change.
print("Example 1: Strings are not mutable")  # pass by value
cup1 = "This cup is Empty..."
print(cup1)
cup2 = cup1
cup2 += "...Let's fill this cup"
# I Only applied changes to cup 2
print(cup1)
# As you can see cup1 still has it's initial value.


print("\nExample 2: [Lists are mutable]")   # pass by reference
mug1 = ["This Mug is Empty..."]
print(mug1)
mug2 = mug1
mug2 += ["... Let's fill it with coffee"]
#  I only applied changes to Mug 2 Why did it change????
print(mug1)
# we put the string in a list and in Python Lists are mutable. and since mug 2 passes by reference changes to mug 2
# also creates changes for mug 1.


print("\nAnother Example involving functions and mutable data types.")
def add_to(num, target=[]):
    target.append(num)
    return target

print(add_to(1))   # outputs: [1]
print(add_to(2)) # outputs: [1,2]
print(add_to(3))  # outputs: [1,2,3]

# since you're calling the function with a new set of data points, You'd think that it would create a fresh list so
# Normally you would've expected something like this
# [1]
# [2]
# [3]
# BUT  due to mutability of lists, Python will evaluate arguments as soon as the functioned is defined not each
# time it's called. It's not a good idea to to define default arguments in a mutable data type.

print("\nOutput only the current argument")
def add_to_2(num, target = None):
    if target is None:
        target = []
    target.append(num)
    return target
print(add_to_2(1))
print(add_to_2(2))
print(add_to_2(3))