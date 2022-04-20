# Hacker Rank Question Link: https://www.hackerrank.com/challenges/diagonal-difference/problem
"""
Assumption: input is a 3x3 array
"""

# Brute force Method  Time O(n) Space: O(1)


def diag_diff(arr):

    lrd = 0  # left to right diagonal
    rld = 0  # right to left diagonal
    j = 0
    i = 0

    for item in arr:
        lrd += arr[i][j]
        i += 1
        j += 1

    j = 0
    i = len(arr) - 1

    for item in arr:
        rld += arr[i][j]
        j += 1
        i -= 1
    print(f"lrd={lrd}")
    print(f"rld={rld}")

    return abs(lrd-rld)


test_1 = [[-1, 2, 3],
         [4, -5, 6],
         [7, 8, -9]]  # abs(-15 - 5b) = 0

test_2 = [[10, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]  # abs(24-15) = 9

print(diag_diff(test_1))
print(diag_diff(test_2))

print(len(test_1))