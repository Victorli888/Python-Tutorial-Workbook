"""
Example 1 : Find W in Hello World!
A While loop will loop until False
i < len(a_string) in layman's terms means run through the entire string/list
"""


def find_w(a_string):
    i = 0  # index of the string in question
    while i < len(a_string) and a_string[i] != "W":
        i += 1
    if i < len(a_string):
        print(f"I've found {a_string[i]}!")
    else:
        print("I was not able to find W.")


"""
Example 2: Leading Whitespace Remover
In other words, This method removes white space found at the beginning of strings.

Input: "     hello!"
Output: "hello!"

String indexing review:
b = "0123456789"

print(f"This is the first index of a string {b[0]} ")
print(f"This is also the first index of a string {b[-10]}")
print(f"This is the first 5 indices of a string {b[:5]}")
print(f"This is the last 5 indices of a string {b[5:]}")
print(f"This is 12345: {b[1:6]}")

"""


def leading_ws_rm(a_string):
    i = 0  # current index of the char of the string in question
    while i < len(a_string) and a_string[i] == " ":
        i += 1
    if i < len(a_string):
        print(a_string[i:])
    else:
        print("No alpha-numeric characters exist in this string")


"""
This time we're going to design an all-purpose white space remover.
INPUT:
"    This    is a   string       with  lots  of whitespace  "
OUTPUT:
"This is a string with lots of whitespace"
"""


def ws_rm(a_string):
    output = ""

    i = 0
    while i < len(a_string):
        # Find a non whitespace character (start of a word)
        while i < len(a_string) and a_string[i] == " ":
            i += 1

        j = i

        if i < len(a_string):
            # Find the end of that word
            while j < len(a_string) and a_string[j] != " ":
                j += 1

            # Build up a string from the original without excess whitespace
            output += " " + a_string[i:j]

        i = j + 1

    # Print output of the final string
    print(output[1:])


# ws_rm("    This    is a   string       with  lots  of whitespace  ")

"""
Question 1 : Write a program that takes a string from the user and prints the first number encountered along with it's 
position. You can assume the number is a single digit

EXAMPLE INPUT
"This is chapter 7 of the book"
EXAMPLE OUTPUT
"7 16"


EXAMPLE INPUT
"There are no digits here"
EXAMPLE OUTPUT
"No digits in string"
"""


def num_finder(a_string):  # for a single digit
    i = 0
    while i < len(a_string) and not a_string[i].isdigit():
        i += 1

    if i < len(a_string):
        print(f"Number: {a_string[i]}\nLocation: {i}")
    else:
        print("There is no number in this string.")


# num_finder("Under Armor has one mission : to make you better")

""" 
Question 2: Upgrade num_finder so that outputs a number larger than a single digit 
"""


def num_finder_2(a_string):  # for multiple digits in a number
    i = 0

    # Find the index of the starting digit
    while i < len(a_string) and not a_string[i].isdigit():
        i += 1
    # Find the index of the ending digit
    if i < len(a_string):
        j = i
        while j < len(a_string) and a_string[j].isdigit():
            j += 1

    # cut the string based on that index
    digit = a_string[i:j]

    if i < len(a_string):
        print(f"Number: {digit}\nLocation: {i}")
    else:
        print("There is no number in this string.")


# num_finder_2("I have 3323 beans in this jar.")


"""
Question 3: Find the first Rep-digit 

# EXAMPLE INPUT
"34 74 86 34576 47093 3 349852 777 9082"
# EXAMPLE OUTPUT
"777"


# EXAMPLE INPUT
"98 3462 245 87658"
# EXAMPLE OUTPUT
"No repdigit in string"
"""


def repdigit(a_string):

    repdigit_found = False
    i = 0

    while i < len(a_string) and not repdigit_found:
        j = i + 1  # "Just keep going until you find it"
        while j < len(a_string) and not a_string[i] == a_string[j]:
            i += 1
            j += 1

        if j < len(a_string):

            while j < len(a_string) and a_string[i] == a_string[j]:
                j += 1

            if a_string[i] == a_string[j-1]:
                repdigit_found = True
                ans = a_string[i:j]
                print(f"Repdigit: {ans}")
        else:
            ans = "N/A"
            print(f"Repdigit: {ans}")
            break


# repdigit("34 74 86 34576 47093 3 349852 77 9082")

"""
Question 4: Write a program that mimics the behavior of a Browser's Find feature
"""


def ctrl_find(string):
    find = input("Search: ")

    occurences = 0

    i = 0
    while i < len(string):
        j = i
        # Find the first letter index in find
        while j < len(string) and not find[0]:
            j += 1

        if j < len(string) and string[j:j+len(find)] == find:
            occurences += 1

        i = j + 1

    print(f"After searching for: \"{find}\", I found {occurences} occurrences")


txt = """Your dog begs every time you cook with onions, garlic, or bake chocolate desserts. It breaks your heart a 
little every time you tell him no, but dogs can’t eat those. He knows those foods are bad but thinks they’re poison to 
you too - and doesn’t want you to die alone."""

ctrl_find(txt)