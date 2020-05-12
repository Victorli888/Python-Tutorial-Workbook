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

# inputs for 3 sides
a = int(input("Enter Side 1: "))
b = int(input("Enter Side 2: "))
c = int(input("Enter Side 3: "))


# Results = value of a is equal to pythagoras Math theorem
a_as_hyp = a == ((b**2) + (c**2)) ** .5
b_as_hyp = b == ((a**2) + (c**2)) ** .5
c_as_hyp = c == ((a**2) + (b**2)) ** .5

if a_as_hyp or b_as_hyp or c_as_hyp:  # Print if all result conditions are true
    print("These sides form a Right Triangle!")
else:
    print("This does not form a right triangle.")
# Check if a is the hypotnuse

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
    try:  # can this string be converted from string to int?
        number = int(input())
        if number % 3 == 0 and number % 5 == 0:
            print("fizz-buzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)
        fizzbuzz_game()
    except ValueError:  # Edge case for when string can't be converted to int
        print("That is not a valid choice! please input a number")
        input("Tap [Enter] to continue")
        fizzbuzz_game()




# For a List
alist = [1, 14, 3, 10, 15, 20, 30, 3, 12]
ans = fizzbuz(alist)
print(ans)


# For a single input
fizzbuzz_game()

# Question 3:

# Create input variables
print("Please input x,y coordinates and the radius of circle one. ")
x1 = int(input("x1: "))
y1 = int(input("y1: "))
r1 = int(input("r1: "))
input("Thank you. Press [Enter to continue]")
print("Please input x,y coordinates and the radius of circle two. ")
x2 = int(input("x2: "))
y2 = int(input("y2: "))
r2 = int(input("r2: "))

# Calculate
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # Distance Formula
total_radius = r1 + r2

# If the distance between two circles is greater than the or equal to the total radius then the circles overlap
if distance >= total_radius:
    print("These circles don't Overlap.")
else:
    print("These circles overlap.")

