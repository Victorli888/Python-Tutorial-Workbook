# argv
def print_two(*args): # the asterisk tells python to take all arguments and put them in a list under "args"
    arg1, arg2 = args  # this is the arguments I want to put in that "args" list
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):  
    # in this we cut out the middle man and put that list directly in where "args" would be
    print(f"arg1: {arg1}, arg2: {arg2}")

# this takes only one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# This one will take none
def print_none():
    print("I got nothing.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
