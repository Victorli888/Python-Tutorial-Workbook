"""
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def bruteForce(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return i, j

"""
Analysis: 
Time: O(N^2)
Space: O(1)
Two Pointer method, with the 1st pointer set to the first item in our list try all other numbers with the 2nd pointer
after the 2nd pointer iterates through all other items in nums, move our 1st pointer by one and repeat
"""

def hashMap(nums, target):
    """
    Find the indices of two numbers in a list that add up to a given target, using a hash map.

    :param nums: A list of integers to search for pairs.
    :param target: The target sum to find.
    :return: A tuple of two integers representing the indices of the two numbers that add up to the target sum.
    """
    prevNums = {}

    for idx, num in enumerate(nums):
        otherNum = target - num
        if otherNum in prevNums:
            return prevNums[otherNum], idx
        prevNums[num] = idx


"""
target = num1 + num2  --> num2 = target - num1
This function uses a hash map to store previously seen numbers and their indices, allowing for a single pass through
the list of numbers to find the desired pair. The function returns a tuple containing the indices of the two numbers
that add up to the target.

Runtime: O(n) - single pass
Space: O(n) - we create a hashmap and we iterate & append each item in nums
"""