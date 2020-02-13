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
