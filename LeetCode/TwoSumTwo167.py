#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Edge: unlike two-sum 1, the given array is already sorted from non-decreasing order
# Gotcha: it's expected that the index returned is 1-based

"""
Notes: There is exactly one solution, and the right side of the array has all the largest numbers and the left the smallest
We can use two pointers from both sides to determine whether we need to increase or decrease sum to find the target.
Doing so, the solution will eventually be found
"""

def left_right_approach(numbers, target):
    """
    left_num + right_num = total; if total > target, we need to reduce and vice-versa for the left
    [0,1,5,7,8]  target = 6; 0+8 is larger than the target, and incrementing left to 1+8 doesn't get us closer.
    :param numbers: Given Sorted array
    :param target: Target Number
    :return: 1-based indicies of numbers in numbers list
    """
    left_idx = 0
    right_idx = len(numbers) - 1

    while left_idx < right_idx:
        total = numbers[left_idx] + numbers[right_idx]
        if total == target:
            return left_idx + 1, right_idx + 1
        # Total is too big, Reduce
        if total > target:
            right_idx -= 1
        # Total is too small, Increase
        else:
            left_idx += 1
    raise Exception("No such value pair was found")

"""
Time Complexity: O(n)
space: O(1)
"""