"""
Question 1: Write a program that prints the first n numbers of the Fibonacci sequence.
The Fibonacci sequence is defined as the next number in the sequence is the sum of the previous two numbers
and the first two numbers in the sequence are 0 and 1. A part of the sequence is shown below:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Question 2: Write a program that prints a sequence such as the one shown below. The number of stars in the widest part
should be equal to the number a user inputs:
~~Input~~
7

~~Output~~
*
**
***
****
*****
******
*******
******
*****
****
***
**
*

Question 3: Write a Python program that reads in a single integer from the user. Then read in an unknown number of
integers, each time printing whether or not the number was higher or lower than the previous. You can assume that every
number is different and you can stop when the number entered is 0. Here is an example input and output:

"""


# Question 1: prints the numbers in fibonacci's sequence

def fibonacci(num_terms):
    n1 = 0
    n2 = 1
    if num_terms <= 0:
        print("please enter number higher than 0")
    elif num_terms == 1:
        print(f"fibonacci's sequence for one term is: {n1}")
    else:
        print(f"fibonacci's sequence for {num_terms} terms is:")
        count = 0
        while count < num_terms:
            print(n1)
            nxt_term = n1 + n2
            n1 = n2
            n2 = nxt_term
            count += 1


fibonacci(6)


# Question 2: create a stars problem


def stars(width_required):
    curr_width = 0
    while curr_width <= width_required:
        print("*" * curr_width)
        curr_width += 1

    while curr_width > 0:
        print("*" * curr_width)
        curr_width -= 1


stars(7)


# Question 3: Guess my Number game!
"""
The player doesn't know but the magic number is 5! the program will either say higher or lower until the magic number is
guessed.
"""

def magic_number_game():
    print("Hello! Try to guess the magic number!")
    guess = int(input("Your Guess?: "))
    magic_number = 5

    while guess != 5:
        if guess > magic_number:
            print("Lower!")
        elif guess < magic_number:
            print("higher!")
        guess = int(input("Try another number: "))

    if guess == 5:
        print("You Win!")


magic_number_game()