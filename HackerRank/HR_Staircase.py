"""
Hacker Rank Question Link: https://www.hackerrank.com/challenges/staircase/problem


My solution: Space Complexity: O(1)  Time Complexity: O(n)
"""


def staircase(n):  # Where n is the number of staircases high
    m = 1  # m is the current count
    n -= 1  # including the last index will make the value be n+1 so n-1 is needed to make it n

    while n >= 0:
        spaces = n*" "
        pound = m*"#"
        print(spaces + pound)
        m += 1
        n -= 1


staircase(6)  # Test
