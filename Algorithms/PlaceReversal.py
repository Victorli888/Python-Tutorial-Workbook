# Instead of reading a list backwards, we will change an exisiting list and put it in the reverse order.

# 2 Pointers, one at the first index and another at the last index. We will swap these elements at these pointers and
# move to next indices.

# The terminating condition would be when left equals to or has crossed over to the right pointer

# ALGORITHM
# 1. left pointer points to the first index, & right pointer points to the last index

# 2. Swap the elements with of the left and right pointer.

# 3. increment the left pointer by 1 & decrement the right pointer by 1

# 4. check if left >= right.
#   a. if yes, end (reversal complete)
#   b. if no, repeat 2-4
print("Example 1: Place Reversal")
def Reversal(alist):
    # initialize pointers

    left = 0
    right = len(alist)-1  # since the order starts a 0  the last element is actually (n-1)

    # condition for termination
    while right > left:

        # swapping
        temp = alist[left]
        alist[left] = alist[right]
        alist[right] = temp

        # increment and decrement pointers
        left += 1
        right -= 1

    return alist

list = [10,9,8,7,6,5,4,3,2,1]
print(Reversal(list))

# s = string
# print(s[::-1]) will reverse the string

# Let's talk about efficiency, why not just create a new list and append each element starting from the end?
print("\nExample 2: Inefficient method")
def inefficient(a_list):
    b_list = []
    for element in a_list[::-1]:
        b_list.append(element)
    return b_list

another_list = [10,9,8,7,6,5,4,3,2,1]
print(inefficient(another_list))

# This is inefficient because,
# A) We need to use additional memory to store our 2nd list (b_list)
# B) We need to go through the entire list of elements at-least once

print("\n\nPractice #1: Reverse the string 'Hello World'")

string1 = "Hello World"

# def split(phrase):
#     return [character for character in phrase]


def P1_Reverse(phrase):
    # Start with list comprehension list  (leaf for leaf in tree)
    list = [character for character in phrase]  # breaks up each char in the string and puts it in a list
    Reversal(list) # Reverse the order
    new = "".join(list)  #string.join(iterable); iterable - any object where all the returned value are strings
    return new


print(P1_Reverse(string1))

print("\n\nExample 2: Reverse the phrase I Love You to You Love I ")


def P2_Reverse(string):
    list2 = string.split()  # by default split() will split the string by each space and puts it in a LIST
    reversed_list = Reversal(list2)
    new = " ".join(reversed_list)
    return new

string2 = "I Love You"
print(P2_Reverse(string2))

print("\n\nExample 3: check whether or not words are a palindrome or not")
def P3_Palidrome_Check(string):
    value1 = string
    print(f"Lets check if {value1} is a palindrome.")
    value2 = P1_Reverse(string)
    print(f"{value1} backwards is {value2}")
    if value1 == value2:
        print(f"{value1} is a palindrome\n\n")
    else:
        print(f"{value1} is not a palindrome\n\n")

P3_Palidrome_Check("madam")
P3_Palidrome_Check(("mouse"))

# This will not properly check palindromes that are sentences But the code could be altered to only check the characters
# in a string and that will check whether or not a palindrome is a true palindrome.

def remove_spaces(string):
    return string.replace(" ", "")
