# *args & **kwargs only the [*] & [**] is necessary when using, Mainly used in FUNCTION DEFININTIONS.
# * & ** allow you to pass a variable number of arguments to a function

print("Example 1: *args")  # *args is used to send a NON-KEYWORDED variable length argument list to the function.


def test_var_args(f_argv, *argv):
    print("first normal arg:", f_argv)
    for arg in argv:
        print("Another arg through *argv:", arg)


test_var_args("I", "love", "u", ";^)")
# this loop will continue as long as there are arguments to iterate
print("\nExample 2: **Kwargs")  # use this when you want to make KEYWORDED variable length of arguments, [Named args]


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


greet_me(name1="Victor", name2="James", name3="Yash")

print("\nExample 3: Using *args & **kwargs to call a function")


def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

# With this, We're able to pass arguments to this little function using *args and *kwargs
args = ("two", 3, 5)
kwargs = {"arg3": 420, "arg1": 51, "arg2": 69}
test_args_kwargs(*args)
test_args_kwargs(**kwargs)
