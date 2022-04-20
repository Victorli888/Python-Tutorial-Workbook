"""
There is a string "s" of lowercase English letters that is repeated infinitely many times. Given an integer "n"
find and print the number of letter a's in the first  letters of the infinite string.
"""


def repeatedString(s, n):
    """:cvar
    s - our given string that will be infinitely repeated
    n - the number of indicies that we are checking starting from the first index of
    since we know that our string is repeated, we can find the total number of times that our whole string is repeated
    in the interval. that number of times is defined our variable "repeat", Now we need to find the total number of times
    "a" is found in our given string "s" and multiply it by our repeat.
    The only thing left to worry about is the remainder string that couldn't be divided evenly by our given s.
    itteriate through our remainder and calculate that into our total and we will have our answer
    """
    repeat = n // len(s)
    remainder = n % len(s)
    count = 0
    for i in range(0, len(s)):
        if s[i] == "a":
            count += 1
    count *= repeat
    for i in range(0, remainder):
        if s[i] == "a":
            count += 1

    return count

s = 'abababaaa'
n = 5

ans = repeatedString(s,n)
print(ans)  # Expected: 3



"""
Big O Analysis:
Time Complexity: 2 * O(n) >>>> O(n)
Space Complexity: this works inplace so O(1)
"""