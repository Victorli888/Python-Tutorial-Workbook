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

    i=0
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

ws_rm("    This    is a   string       with  lots  of whitespace  ")
