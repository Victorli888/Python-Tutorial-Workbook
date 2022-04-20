import sys


"""
Question 1: Write a program that multiplies an arbitrary number of command-line arguments together. 
The arguments will be numbers

your Program should run as follows:
$ python3 calc.py 8 8 9 3 2
3456

"""


# sys.argv is shorthand for argument vector, This is a list containing command line arguments passed to the script.
# The arguments passed for the script come after the name of the script. i.e $ python3 Slither_ch10.py arg1 arg 2 ...


def calc():

    total = 1

    i = 1
    while i < len(sys.argv):
        total *= int(sys.argv[i])
        i += 1

    print(total)


# calc()

"""
Question 2: write a program that reads in lines from standard input (no redirection) and outputs them to 
standard output. (No redirection)
"""
# standard input = stdin
# read() - Reads the entire contents of the file and entire contents will be assigned to a single string
# readlines() - stores each line as an element in a list
# readline() - reads only a single line from standard input, arguably the best because  it can save memory.


def reader():

    line = sys.stdin.readline()
    while line:
        print(line)
        line = sys.stdin.readline()


# reader()


"""
Question 3: Write a program that reads a text file and outputs how many words are contained within that file

"""


def word_count():
    file_name = sys.argv[1]

    with open(file_name, "r") as f:
        text = f.read()

    words = text.split()
    print(len(words))


# word_count()

"""
Question 4: Write a program that takes the contents of a file and determines whether or not a phrase is a palindrome.
Words that are Palindromes should return True, else false.Capitals and spaces should not effect the answer.

"""
# with statement clarifies code that would use try... finally blocks to ensure clean-up code is executed.
# with statement will handle closing the file for us


def palindrome():
    # take a standard input file
    file_name = sys.argv[1]

    # Open the file
    with open(file_name, "r") as f:
        # contents in opened file as usable variable "word"
        word = f.readline().strip()  # readline() - reads only a single line from standard input,
        while word:
            processed = word.replace(" ", "").lower()  # remove all spaces and change all to lowercase.
            if processed == processed[::-1]:  # [::-1] from start to finish but go backwards
                print(True)
            else:
                print(False)
            word = f.readline().strip()  # strip() removes the trailing and leading white space


# palindrome()

