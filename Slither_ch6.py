"""
~~~Question 1: Write a program that takes as input, a single integer from the user which will specify how many decimal
places the number e should be formatted to. Take e to be 2.7182818284590452353602874713527
EXAMPLE INPUT
4
EXAMPLE OUTPUT
2.7183

~~~Question 2: Write a program that will take as input, a string and two integers. The two integers will represent
indices.If the string can be sliced using the two indices then print the sliced string. If either or both of the
integers are outside the strings index range then print that the string cannot be sliced at those integers.
EXAMPLE INPUT
"This is my string"
2
9
EXAMPLE OUTPUT
'is is m'
EXAMPLE INPUT
"This is a string"
10
22
EXAMPLE OUTPUT
'Cannot slice string using those indices'

~~~Question 3: When you sign up for accounts on website or apps, you may be told your password strength when entering it
for the first time. In this exercise, you are to write a program that takes in as input, a string that will represent
a password.

Assume: digits, Lower-case, Upper-case, and special characters eg, !@#$ can be used
Grade strength: too weak, weak , good, and very strong. Only "good" and "very strong" passwords are valid. Everything
else should display not valid and ask for another input.

~~~Question 4: Write a program that takes 3 floating point numbers as input from the user: a starting radius, radius
increment and an ending radius. Based on these three numbers, your program should output a table with a spheres
corresponding surface area and volume.
EXAMPLE INPUT
1
1
10
EXAMPLE OUTPUT
    Radius            Area          Volume
----------      ----------    ------------
       1.0           12.57            4.19
       2.0           50.27           33.51
       3.0          113.10          113.10
       4.0          201.06          268.08
       5.0          314.16          523.60
       6.0          452.39          904.78
       7.0          615.75         1436.76
       8.0          804.25         2144.66
       9.0         1017.88         3053.63
      10.0         1256.64         4188.79
"""

# Question 1: How many decimals are in e? syntax: "{}".format(x)
def decimals_of_e():
    e = 2.7182818284590452353602874713527
    print(" e is 2.7182818284590452353602874713527, to how many decimals would you like to reduce this to?")
    print("For example, if You say 2 e will look like: {:.2f}".format(e))
    amount_of_decimals = input("> ")
    print("{:.{}f}".format(e, amount_of_decimals))  # follows {[: <align> <minimum width> <.precision> <type>]}


def decimals_of_pi():
    pi = 3.14159265359
    print(" pi is 3.14159265359 to how many decimals would you like to reduce this to?")
    amount_of_decimals = input("> ")
    ans = "{:.{}f}".format(pi, amount_of_decimals)
    print(f"Tada! we now have {ans}")

# decimals_of_e()
# decimals_of_pi()




