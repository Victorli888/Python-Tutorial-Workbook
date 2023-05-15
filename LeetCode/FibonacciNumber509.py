# https://leetcode.com/problems/fibonacci-number/
# Find the Fibonacci Number at Nth term
# 0,1,1,2,3,5,8,13,21
# need first two terms in order to calculate Fib sequence
def find_next_number(n):
    """
    O(n) Time
    O(1) Space
    find_next_number(4) = 3
    :param n: next number after Nth number in fib sequence
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

def find_sequence(n):
    """
    Find Sequence for up to nth term
    :param n: determine how many numbers in the sequence should be produced
    :return: fibonacci sequence as a list
    """
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return[0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    return sequence

def find_next_recursively(n):
    if n == 0:
        return 0
    if n == 1:
         return 1

    return find_next_recursively(n-1) + find_next_recursively(n-2)

