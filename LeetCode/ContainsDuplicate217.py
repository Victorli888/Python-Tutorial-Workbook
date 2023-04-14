"""
https://leetcode.com/problems/contains-duplicate/
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.
"""

"""
Analysis of the problem:
As long as we find a Duplicate it's not necessary to iterate through the entire array.
"""

def bruteForce(nums):
    """
        Compare the first item of the array with the rest, and then repeat for all other items in the array. Implement a
    double for loop to iterate through.
    :param nums: some array containing integers
    :return: True if Duplicate is found, False if not
    """
    n = len(nums)

    # Edge Case for Arrays with a length smaller than 2
    if n<2:
        return False

    for i in range(n):
        for j in range(i):
            if nums[i] == nums[j]:
                return True
    return False
'''
Brute Force Analysis:
Time Complexity: O(n^2) - A Nested For Loop is used to iterate & compare each pair in the array O(n) * O(n)
Space Complexity: O(1) - We do not create our own array

range() will create a sequence of numbers up to n (but not including n)
i will be the leading pointer and j will follow the pointers are assigned to the position of each element in the array. 
When i reaches the end and j has followed up with all the elements in its range then the for loop ends and return false 
because there were no duplicates found, other wise the for loop terminates and returns true during the comparison check.
'''

def sortAndCompare(nums):
    sortedArr = sorted(nums)

    if len(sortedArr) < 2:
        return False

    for i in range(len(sortedArr) - 1):
        if sortedArr[i] == sortedArr[i + 1]:
            return True
    return False


'''
SortAndCompare Analysis:
Time Complexity: Create a sorted array, and iterate through it ----  nlog(n) + n so, TC is nlog(n)
Space Complexity: O(n), If allowed to mutate the original array, then we can do this in O(1) with nums.sort()

Maintains the same strategy to compare two pointers. Following pointer = i, and Leading Pointer = i+1  but we leverage 
the fact that our Array is sorted and any duplicates will be right next to each other. So we iterate he array only once
to compare all adjacent items

Notes for me: 
---- length = len(nums) 
I initially wrote this for the sake of clarity, but it's unnecessary since the built-in method is plenty readable
you could argue that it is more readable, but in the end, its trivial.

---- range(len(sortedArr) vs range(len(sortedArr)-1)
As we compare our pointers when our following pointer points to the last item in the array or leading pointer will point
outside of the array (IndexError). So we need code in place to end the for loop before that

Solution 1: use a break statement
   if i == size-1:
            break
Check for when our following pointer has reached the end of our array an break. (Ugly Solution IMO)

Solution 2: Reduce the range of the for loop
We know that our leading pointer will cover the 1 index ahead of our following pointer so reduce the range of our for
loop such that our following pointer only iterates to to the 2nd to last item --> len(nums)-1. 
'''


def hashSet(nums):
    uniqueNums = set()  # I suggest Reviewing Hashset vs Hashmap data structures

    for i in nums:
        if i in uniqueNums:
            return True
        uniqueNums.add(i)
    return False

"""
HashTable Solution Analysis:
Time Complexity: O(n), The Look up time and appending time for a hash set is O(1) and so doing these operations across
our array will yield a TC of O(n)
Space Complexity: O(n) we need to take up memory for hashset in order to do this.

As we iterate through our array we determine if the element exists in our hashset, we have a duplicate thus return True
Otherwise, append it to our hashset. If the for loop completes then there is no duplicates, thus return False.
"""