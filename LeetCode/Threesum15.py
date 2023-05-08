#https://leetcode.com/problems/3sum/

"""
Notes:
    () Can't contain Duplicate Answers
    () The sum of all three numbers must be 0

"""


def find_zero_sum(nums):
    """
    Two pointer solution, that sorts the array and solves for zero-sum of three numbers
    :param nums: given list of numbers
    :return: Non-duplicate triplets of numbers summing to zero

    Time-Complexity: O(n)^2
    Space: O(n)
    """
    nums.sort()
    ans = []

    for index in range(len(nums)):
        # sum of zero is impossible if all three numbers are positive
        # Array is sorted, if the first element isn't negative then there is no negatives in the list
        if nums[index] > 0:
            break
        if index > 0 and nums[index] == nums[index - 1]:
            continue

        left = index + 1
        right = len(nums) - 1

        while left < right:
            sum_of_three = nums[left] + nums[right] + nums[index]
            if sum_of_three < 0:
                left += 1
            elif sum_of_three > 0:
                right -= 1
            else:
                # append our answer and inc/dec both sides to avoid duplicates
                ans.append([nums[index], nums[left], nums[right]])
                left += 1
                right -= 1
                # Avoid using duplicates
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return ans



