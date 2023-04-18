"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

def easyWay(s,t):
    """
    Python has in-built methods to sort strings, after sorting if the strings are equal then they are anagrams.
    :param s: string one
    :param t: string two
    :return:
    """
    return sorted(s) == sorted(t)


"""
Analysis: Obvious Answer, but it doesn't test any programming knowledge. How might you do this without using sorted()
Time: O(Nlog(N))
Space: O(1)
"""


def hardWay(s, t):
    """
    Using a hashmap we store each unique character as a key, and the frequency as the value, and return the bool
    comparison for each hashmap.
    Best Case O(1) when we have two strings of a different size.
    :param s:
    :param t:
    :return:
    """

    if len(s) != len(t):
        return False

    sTable, tTable = {}, {}

    for i in range(len(s)):
        sTable[s[i]] = 1 + sTable.get(s[i], 0)
        tTable[t[i]] = 1 + tTable.get(t[i], 0)
    return sTable == tTable

"""
Analysis:
Time: O(N)
Space: O(2N) ... O(N)
"""

def harderWay(s,t):
    """
    How might you solve this without using the get()? Well get simply uses a default value incase the key doesn't exist
    in the hashmap. This can be replicated with an if & else statement.
    :param s:
    :param t:
    :return: True, if Anagram
    """
    if len(s) != len(t):
        return False

    sTable, tTable = {}, {}

    for i in range(len(s)):
        if s[i] in sTable:
            sTable[s[i]] += 1
        else:
            sTable[s[i]] = 1

        if t[i] in tTable:
            tTable[t[i]] += 1
        else:
            tTable[t[i]] = 1

    return sTable == tTable

"""
Analysis:
time: O(N)
Space: O(N)
"""
