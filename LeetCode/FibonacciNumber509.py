# https://leetcode.com/problems/fibonacci-number/
# Find the Fibonacci Number at Nth term
# 0,1,1,2,3,5,8,13,21
# need first two terms in order to calculate Fib sequence
def findfib(n):
    """
    O(n) Time
    O(1) Space
    :param n: Nth number in fib sequence
    :return: Number at Nth position
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    term_1 = 0 # n-2
    term_2 = 1  # n-1

    for _ in range(2, n+1):
        next_number = term_1 + term_2
        term_1 = term_2
        term_2 = next_number
    return next_number

