"""
Hacker Rank Question Link: https://www.hackerrank.com/challenges/plus-minus/problem


My solution: Space Complexity: O(1)  Time Complexity: O(n)
"""


def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    total_nums = len(arr)

    for i in arr:
        if i == 0:
            zero += 1
        if i > 0:
            pos += 1
        if i < 0:
            neg += 1

    pos = pos / total_nums
    neg = neg / total_nums
    zero = zero / total_nums

    print('{:2.6f}'.format(pos))
    print('{:2.6f}'.format(neg))
    print('{:2.6f}'.format(zero))


test1 = [-4, 3, -9, 0, 4, 1]
"""
Expected: 
0.500000
0.333333
0.166667
"""

plusMinus(test1)