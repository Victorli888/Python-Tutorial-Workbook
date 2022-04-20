"""
Going bottom up as an alternative to Recursion can reduce memory cost on the call stack

Example: using Recursion create a function that multipies all the numbers in range of 1 to n. (for whole integers only)
"""


def recursive_mult(n):
    return n * recursive_mult(n-1) if n > 1 else 1
# time O(n) space complexity is O(n)


anz = recursive_mult(3)
print(anz)

"""
This method O(n) for the size and can lead to a stack overflow on our call stack, by using a bottom up method we can 
optimize space to O(1)
"""


def bottom_up(n):
    result = 1
    for num in range(1, n+1):
        result *= num
    return result
# time is O(n) space is O(1)


ans = bottom_up(3)
print(ans)
