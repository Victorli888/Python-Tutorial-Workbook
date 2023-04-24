"""
https://www.youtube.com/watch?v=8mJ-OhcfpYg - Good Visual & Explanation on how Insertion sort wroks

Summary:
have a temp variable to store element in our given array, and compare whether temp is smaller, when our temp is larger
than the element to the next left OR if the end is reached INSERT temp at that position.
"""


def insertion_sort(nums):
    """
    Notes: we follow our element through the list until we find the appropriate spot before moving onto the next idx
    Time: Average Case:O(n^2) --- Best case: O(n) (when nums is already sorted we don't have to use while loop logic.)
    Space: O(1) - Sorts in place.
    :param nums: Given array of integers
    :return:
    """
    # starts at 0, but after looking closely at the nested while loop, logic doesn't apply until idx = 2
    for idx in range(0, len(nums)):

        # hold current element for comparison
        temp = nums[idx]

        # if the left element is smaller than our current temp, swap and decrement our pointer to follow current temp
        while idx > 0 and nums[idx - 1] > temp:
            nums[idx] = nums[idx - 1]
            idx -= 1
            nums[idx] = temp

    return nums


def recursive(arr, n):
    if n > len(arr):
        return

    recursive(arr, n+1)
    curr = arr[n+1]
    while curr > 0 and arr[n+2] > curr:
        arr[n+1] = arr[n+2]
        curr -= 1
    n += 1
    return arr
