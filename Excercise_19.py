def cheese_and_crackers (cheese_count, boxes_of_crackers):
    print(f"You wedges of cheese: {cheese_count}")
    print(f"You have {boxes_of_crackers}, boxes of crackers.")
    print("That could feed a village.")
    print(f"Get some wine.\n")  # \n - create a new line
#  "def" to create the mini-script "cheese_and_crackers" the functions name so we can call on it later
# ("(cheese_count, boxes_of_crackers)" the variables used in the function.
# The indented portion is the actual mini-script
print("We can just give function numbers directly:")
cheese_and_crackers(20,30)
# in the most direct and simplest way, we setting integers to input1 and input2 of our function

print("Or, We can use variables from our script:")
amount_of_crackers = 50
amount_of_cheese = 10
# this is the operation to set a value to a variable
cheese_and_crackers(amount_of_cheese,amount_of_crackers)
# we're setting the integer amount and setting it equal to a variable
# Then we use the variable instead of the integers to be used in our function (mini-script)
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
# before call on function (mini-script) were asking to the script to do math in input1 and input2 of our function.
# After the math is done, it becomes 1 input and it uses that input in the function we wrote
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# We have a variable in the script that was set to an integer and we're simply adding an integer to it.
# After adding these integers together we set it to input1 , input2 use them in our function (mini-script)

# When you run this you'll notice its printing the same dialogue over and over again but with different values.
# this is the idea behind this function
