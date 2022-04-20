# Hacker Rank Problem: Sales by Match
'''
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each
 sock, determine how many pairs of socks with matching colors there are.
'''
given_arr = [1,1,4,6,8,9,97,5,3,5,667,7,5,4,3,5,5,6,3,1,1,1,2,35,9,0]


def findPairs(arr):
    """
    We can use a Hashmap to store the type of sock & number of socks found. Since we only care about total pairs we
    should floor divide each value of each key and add it to our total pairs. Once all key-value pairs are accounted for
    we can return total number of socks.

    :param arr: Is our given array of integers to find pairs from
    :return: Total Number of pairs in our array
    """
    count = {}
    numOfPairs = 0

    for item in arr:
        count[item] = 0
    for item in arr:
        count[item] += 1

    for item in count:
        numOfPairs += int(count[item] // 2)
    return numOfPairs

pairs = findPairs(given_arr)
print(f"We have {pairs} pairs of socks")


""" Big O Analysis
Time Complexity: 3 * O(n) ~ O(n)
Space Complexity: O(n)
"""