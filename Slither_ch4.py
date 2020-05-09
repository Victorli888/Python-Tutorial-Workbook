"""
1)Write a program that takes three inputs, a, b and c and prints out whether or not those numbers form a right angled
triangle. The formula you'll need is

[Image] - please visit https://www.slitherintopython.com/book/chapter_4/chapter_4.html

2)Fizz buzz is a game in which the following rules apply:

any number which is divisible by 3 is replaced with fizz
any number which is divisible by 5 is replaced with buzz
any number which is divisible by both 3 and 5 is replaced with fizz-buzz
any other number is just the number itself

3) Write a program which takes in six numbers, x1, y1, r1 and x2, y2, r2 (which are the x and y coordinates of the
center of a circle and that circles radius) and print out whether or not the two circles overlap.

[Image] please visit https://www.slitherintopython.com/book/chapter_4/chapter_4.html

You're going to need the formula for the distance between two points to solve this which is:


"""

# Question 1.

# Question 2.

# For a list of numbers


def fizzbuz(num_list):
    listy = []
    for item in num_list:
        if item % 3 == 0 and item % 5 == 0:
            listy.append("fizz-buzz")
        elif item % 3 == 0:
            listy.append("fizz")
        elif item % 5 == 0:
            listy.append("buzz")
        else:
            listy.append(item)
    return listy


# For a single user input

def fizzbuzz_game():
    print("Lets play fizzbuzz! What number do you choose?")
    number = int(input())

    if number % 3 == 0 and number % 5 == 0:
        print("fizz-buzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)

# how to create edge case for string that can't be converted to integer

# For a List
alist = [1, 14, 3, 10, 15, 20, 30, 3, 12]
ans = fizzbuz(alist)
print(ans)


# For a single input
fizzbuzz_game()
