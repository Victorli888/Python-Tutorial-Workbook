"""
Practice Problems from the Slither into Python Tutorial Workbook

Question 1: Assume a population of rabbits doubles every 3 months. Further assume the current population is
11 rabbits i.e. number_of_rabbits = 11
>> Write a Python program to calculate the rabbit population after 2 years and print the result to the terminal.

Question 2: Extend the above program to allow the user to input the number of rabbits and the time period after which
you want to know the rabbit population e.g. 4 years

Question 3: Assume the user is going to input 2 numbers, x and y for example. Write a Python program that will swap the
numbers stored in these variables e.g.
# Assume the user has input these
x = 3
y = 11
# Your code to swap here
# After, the variables should be:
# x = 11
# y = 3

Question 4: The goal of this task is to derive a single assignment statement for the following sequences such that,
if the variable x has the first value in a sequence, then x will have the next value in the sequence after the
assignment statement is executed. And if the assignment statement were executed repeatedly, then x would cycle through
all of the values in the sequence.

# EXAMPLE
# Sequence:
# 0 1 2 3 4 5 6 7 ...
#SOLUTION
x = x + 1

Sequence 1:
0 2 4 6 8 10 12 ...

Sequence 2:
0 -1 -2 -3 -4 -5 -6 ...

Sequence 3:
6 -6 6 -6 6 -6.....

Sequence 4 (Difficult):
-6 -3 0 -6 -3 0 -6 -3 0 -6 -3 0.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# Question 1
# Rabbits double every 3 months # Start: 11 rabbits # Find Population after 24 months


def rabbit_calc(num_of_rabbits, num_months):
    time_factor = num_months//3
    double_variable = 2 ** time_factor  # doubling_variable is the number of times the rabbits double.
    new_total = num_of_rabbits * double_variable
    return new_total

# print(rabbit_calc(11, 24))

# Question 2: Extend the above program to allow the user to input the number of rabbits and the time period
# I don't think it's neccessary to convert from years to months but I did it in Question 2 to show that it can easily
# be done


def input_rabbit_calc():
    num_of_rabbits = int(input("How many rabbits is there to start? "))
    years = int(input("How many years occurred? "))
    years_to_months = years * 12  # Years to Months
    time_factor = years_to_months//3
    double_variable = 2 ** time_factor  # doubling_variable is the number of times the rabbits double.
    new_total = num_of_rabbits * double_variable
    return new_total


# ans = input_rabbit_calc()
# print(ans)

# Question 3: Create a swap algorithm


def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y


def swap_diag(x, y):
    print(f"x is {x}\ny is {y}\nLet's swap them!")
    x, y = swap(x, y)
    print(f"\nNow are answer looks like this!\nx is {x}\ny is {y}\n")


swap_diag(3, 8)

# Question 4: Mental Math

# Sequence 1
x = 0  # First value of the sequence
x = x + 2  # Single assignment Statement

# Sequence 2
x = 0
x = x - 1

# Sequence 3
x = 6
x = x * -1

# Sequence 4
x = 0
x = x % 9 - 6
