"""
A function: is code that takes input, performs some computation and produces an output.
"""

# Default mutable argument trap


def add_to_list(word, word_list=[]):  # PyCharm IDE will flag this as "default argument is mutable"
    word_list.append(word)
    return word_list


def main():
    word = "apple"
    tlist = add_to_list(word)
    print(tlist)
    word = "orange"
    tlist = add_to_list(word, ['pear'])
    print(tlist)
    word = "banana"
    tlist = add_to_list(word)
    print(tlist)

"""
We expect:
$ py trap.py
['apple']
['pear', 'orange']
['banana']

But instead our actual is: 
$ py trap.py
['apple']
['pear', 'orange']
['apple', 'banana']

This is because in memory python initiates our empty word_list arg ONLY ONCE, and so the list has memory and anything
added to it will remain there.
if we use instead 

def add_to_list(word, word_list = None):
    if word_list is None:        
        word_list = []
    word_list.append(word)
    return word_list
    
"""


def add_to_list2(word, word_list=None):
    if word_list is None:
        word_list = []
    word_list.append(word)
    return word_list


"""
None is a special value that indicates [no value] and is immutable
"""

"""
 If "if __name__ == '__main__'"
 
 Every Module in python has a special Attribute called __name__. value of __name__ is set to __main__ when the module 
 is run as the main program. Otherwise, the value of __name__ is set to contain the name of the module.
 
 Use this block of code:  __name__ == '__main__'
 to prevent certain code from being run while the module is being imported.
"""

# MODULE1 1: person.py


def creds():
    name = "Sarah"
    age = 26
    print("person details {}, {}".format(name, age))


print("top-level in person module")

if __name__ == "__main__":
    print("person mod is run directly")
else:
    print("person mod is imported into another module")

# MODULE 2:  utility.py
"""
import person
person.creds()
if __name__ == "__main__":
    print("utility mod is run directly")
else:
    print("utility mod is imported into another module")
"""

"""
From the Command line example 1:
python person.py
>>>
top-level in person module
person mod is run directly
"""

"""
From the Command line example 2:
python utility.py
>>>
top-level in person module
person mod is imported into another module
person details Sarah, 26
utility mod is run directly
"""

"""
Example Problem 1: Write a module named sorting.py that implements selection sort and insertion sort and returns 
those sorted values.

sorting.py module should be imported

please view Slither_ch12_sorting.py & Slither_ch12_test.py for answer and executable.
"""

"""
Write a module called arithmetic.py. This module should include the following functions:

add()
multiply()
divide()
subtract()
The add(), multiply() and subtract() functions should be able to handle an arbitrary number of arguments. divide() should only take 2 arguments. Your function should return the calculated values, not print them.

Your module should be imported and run as follows in another script called test.py

"""

# arithmetic.py


def add(*argv):
    total = 0
    for arg in argv:
        total += arg
    return total


def sub(*argv):
    total = argv[0]
    i = 1
    while i < len(argv):
        total -= argv[i]
        i += 1
    return total


def multiply(*argv):
    total = 1
    for arg in argv:
        total *= arg
    return total


def divide(arg1, arg2):
    if arg2 == 0:

        return "Cannot divide by zero"

    else:
        total = arg1 // arg2
        return total


if __name__ == "__main__":
    print("Running as main")
    ans = multiply(6, 6, 45, 4, 6, 4)
    print(ans)
    print(sub(5, 6, 8, 9))
    print(sub(6, 3))
else:
    print("script is being imported")

    # test.py
    from practice import *

    print("Addition:")
    print(add(4, 6, 7, 2, 3))
    print(add(3, 2))
    # print("")
    #
    # print("subtraction")
    print(sub(5, 6, 8, 9))
    print(sub(3, 2))
    # print("")
    #
    # print("Division")
    print(divide(6, 3))

    # print("")
    #
    # print("Multiplication")
    print(multiply(2, 3))
    print(multiply(2, 3, 3))

# test.py
from practice import *

print("Addition:")
print(add(4, 6, 7, 2, 3))
print(add(3, 2))
# print("")
#
# print("subtraction")
print(sub(5, 6, 8, 9))
print(sub(3, 2))
# print("")
#
# print("Division")
print(divide(6, 3))

# print("")
#
# print("Multiplication")
print(multiply(2, 3))
print(multiply(2, 3, 3))