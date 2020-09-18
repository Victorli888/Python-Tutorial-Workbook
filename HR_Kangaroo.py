"""
HackerRank Question Link: https://www.hackerrank.com/challenges/kangaroo/problem
x1 - starting distance for Kangaroo 1
v1 - jumping speed for Kangaroo 1
x2 - starting distance for Kangaroo 2
v2 - jumping speed for Kangaroo 2
Find: whether or not both kangaroos eventually jump to the same spot
Time Complexity: O(1)  Space Complexity: O(1)
Worse case for time is O(10000) best case is O(1)
"""

def kangaroo(x1, v1, x2, v2):
    j1 = 0
    j2 = 0  # number of jumps by kangaroo 1 & 2
    while True:
        total1 = x1 + v1*j1
        total2 = x2 + v2*j2
        if total1 == total2 and j1 == j2:
            return "YES"
        elif j1 >= 10000:
            return "NO"
        j1 += 1
        j2 += 1

# To test this solution use kangaroo_test.py found in this directory
#i.e from terminal while in this directory run <python3 kangaroo_test.py>
