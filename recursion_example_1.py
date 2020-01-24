# recursion is the process of defining something in terms of its self. (two parallel mirrors)

# example of a recursive function to find the factorial of a number.

def calc_factorial(x):
    """
    This is a recursive function that finds the factorial of an integer
    :param x:
    :return:
    """

    if x == 1:
        return 1

    else:
        return (x * calc_factorial(x-1))

num = 5

print(f"the factorial of {num} is {calc_factorial(num)}")

