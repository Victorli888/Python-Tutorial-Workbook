"""Write an efficient function that checks whether any permutation of an input string is a palindrome

Assume: input strings are lowercase letters
Example:
    > Civic should return True
    > ivicc should return True
    > civil should return False
    > livci should return False

Biggest hint of your life, All Palindromes share one unique trait. the word will have 1 or less characters that don't
share a pair.  toot  0  civic = 1 racecar = rraacc e = 1. in other words there's no need to deal with pointers. just
use a set

"""
def Palindrome(a_string):
    list = set()  # store characters here
    print(f"The word \"{a_string}\" and its permutations are palindromes")
    for char in a_string:  # operation that runs through each character in the string
        if char in list:  # if the char is in my list remove it
            list.remove(char)
        else:  # if the character isn't there add it to the list
            list.add(char)
    if len(list) <= 1:  # if there are characters in my list then that means there isn't a pair to go with it
        #  if it exceeds 1 that means it isn't a palindrome, because palindromes "mirror" each other.
        return True
    return False

word = "racer"

print(Palindrome(word))
