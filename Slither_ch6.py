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

# Question 2: String Cutter


"""
Note:
string_cutter() & string_cutter_2 method doesn't accept negative answers and only cuts with positive whole integers
. For example to cut string[-11:-5] for string = Hello World would need different logic. Personally I would use a 
Try and Except Exception Handling
"""


def string_cutter():   # my solution
    a_string = input("Enter string to be cut: ")
    lower_index = int(input("Enter lower index to be cut from: "))
    upper_index = int(input("Enter upper index to be cut from: "))

    if upper_index >= lower_index:
        print(a_string[lower_index:upper_index])
    else:
        print("invalid try again")
        string_cutter()


def string_cutter_2():  # Book solution
    a_string = input("Enter string to be cut: ")
    lower_index = int(input("Enter lower index to be cut from: "))
    upper_index = int(input("Enter upper index to be cut from: "))

    if len(a_string) < lower_index or len(a_string) < upper_index:
        # We can't have an index larger than the total amount of indices in our string
        print("This string can't be cut from these these indices")
    else:
        print(a_string[lower_index:upper_index])

# Question 3: Password Security


"""
What determines password strength:
Weak:  Lower case only, or Upper Case Only
Fair: Mixture of Upper & Lower Case
Good:  Mixture of Upper & Lower Case + Numbers
Strong: Mixture of Upper & Lower Case + Numbers + Special Characters
"""

# Brute Force Method:


def split(word):
    return [char for char in word]


def score_checker(total_score):
    if total_score == 4:
        print("This is a strong password")
    elif total_score == 3:
        print("This is a good password")
    elif total_score == 2:
        print("This is a fair password")
    else:
        print("This is a weak password\n")
        input("Tap [Any Key] to continue")
        password()


def password():

    # items
    upper_case = ["A","B","C","D","E","F","G","H","I","J","K",'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y'
        ,'Z']
    lower_case = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y",
                  "z"]
    numbers = ["1",'2','3','4','5','6','7','8','9','0']

    special = ["!",'@','#','$','%','^','&','*','_','-','?']

    # Take a user input
    print("Please create a new password (Do not use these special characters ()\{}|+></~`)")
    print("Password should be at least 7 Characters")
    ans = input("Create a password: ")

    if len(ans) >= 7:
        pass
    else:
        password()

    i = 0  # current index for string from user input.

    # scores that will increase by 1, if they have a lowercase, upper, number, or special character
    lower_case_score = 0
    upper_case_score = 0
    number_score = 0
    special_score = 0

    split_up_string = split(ans)  # split up characters in array


# Run through the string array split_up_string and if true set password_trait_score to 1
    while i < len(split_up_string):

        if split_up_string[i] in lower_case:
            lower_case_score = 1
        elif split_up_string[i] in upper_case:
            upper_case_score = 1
        elif split_up_string[i] in numbers:
            number_score = 1
        elif split_up_string[i] in special:
            special_score = 1
        i += 1

    total_score = lower_case_score + upper_case_score + number_score + special_score
    score_checker(total_score)


#password()
