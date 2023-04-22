from collections import defaultdict

def brute_force(strs):
    """
    Find anagrams and group them in list within a list. Do this by checking the length and sorting the characters
    :param strs: List of strings
    :return: List containing list of strings that are anagrams
    """
    groups = []
    for s in strs:  # loop through all strings inside or given list of strings
        is_anagram = False

        for group in range(len(groups)):
            if len(s) == len(groups[group][0]) and sorted(s) == sorted(groups[group][0]):
                # This is an anagram for the current group, append it to this group
                groups[group].append(s)
                is_anagram = True
                break

        if is_anagram == False:
            # current s is not an anagram of current group make a new group within groups
            groups.append([s])
    return groups

"""
Time Complexity: O(NMNLog(N)) ---> O(mn^2log(n))
n - for each string in given list
m- for each char in string
nlog(n) for sorting algo used in code
Space Complexity: O(N)
"""

def HashMap(strs):
    """
    Hashmap solution that maps a count list for each string in the given list. That count list acts as a key in our
    hashmap, if it exists already append it to the
    :param strs:
    :return:
    """
    # Dictionary containing an array count of chars as the key & a list of anagrams with those chars
    ans = defaultdict(list)

    for string in strs:
        # alphabet count as we iterate through a string
        count = [0] * 26
        for char in string:
            # using ord() we can find the ordinal position within unicode and increment the index
            # represented in our count array
            count[ord(char) - ord("a")] += 1

        ans[tuple(count)].append(string)  # lists not usable as key, cast to tuple
    return ans.values()
"""
Time Complexity: O(nm)
Space Complexity: O(n)
"""


def WithoutDefaultDict(strs):
    """
    Demonstrate how defaultdict can save us lines of code.
    simplifies the steps for how we implement our hashmap by removing the need to explicitly check for when a key in
    our array is empty.

    This is important in this circumstance because we need to know when to append a string to our list, or to create a
    list.
    :param strs:
    :return:
    """
    # dictionary {char_count_array: list_of_strings}
    ans = {}

    for string in strs:
        count = [0] * 26
        for char in string:
            count[ord(char) - ord("a")] += 1
        count = tuple(count)
        if count in ans:
            ans[count].append(string)
        else:
            ans[count] = [string]
    return ans.values()

"""
Time Complexity: Two variables to consider in regards to time complexity is m & n 
n - represents the number strings in the list we need to iterate through
m - represents the length of string in that list

It's more accurate to denote these as separate variables instead of n^2, because the elements our for loops operate on 
are different. For example the length of m is dependent on the total characters in a string, and n is dependent on the 
total elements in our string array

Space Complexity: O(NK)
for the same reason

"""
