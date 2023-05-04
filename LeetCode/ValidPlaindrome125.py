#https://leetcode.com/problems/valid-palindrome/

def bruteForce(s):
    """
    This can be done in O(n) space and O(n)
    First remove all non alpha
    time by iterating backwards through our string a verifying the result with s
    :param s:
    :return:
    """
    # remove non-alphanumeric characters from s
    s = "".join(c for c in s if c.isalnum())
    # change to lower case
    s = s.lower()
    ans = ""

    for idx in range(len(s)-1, -1, -1):
        ans += s[idx]
    return ans == s

def brute_force2(s):
    """
    We can use a s[::-1] as a convenient way to reverse our string without the for loop
    GOTCHA: you may think since we've overwritten s, we have O(1) space. This is not technically true
    while the previous value is marked as inaccessible it is not immediately collected by the garbage collector
    Space is still O(n)
    :param s:
    :return:
    """
    # remove non-alphanumerics & convert to lowercase
    s = "".join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]

def is_alphanum(char):
    """
    Python has a built-in method that does this already (char.isalnum()), BUT it's possible to use your own as well
    A - Z; a - z; 0 - 9
    :param char: a single character, (99 is two characters)
    :return: True if alphanumeric
    """
    return ord("A") <= ord(char) <= ord("Z") or ord("a") <= ord(char) <= ord("z") or ord("0") <= ord(char) <= ord("9")

def two_pointer(s):
    """
    We can solve this problem by using two pointer that start from both sides and move to meet in the middle.
    O(n) Runtime
    O(1) Space

    :param s: some string
    :return:
    """
    # Pointers
    left, right = 0, len(s)-1

    while left < right:
        while left < right and not is_alphanum(s[left]):
            left += 1
        while left < right and not is_alphanum(s[right]):
            right -= 1
        if not s[left].lower() == s[right].lower():
            return False
        left += 1
        right -= 1
    return True



