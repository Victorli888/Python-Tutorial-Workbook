"""
https://www.youtube.com/watch?v=8mJ-OhcfpYg - Good Visual & Explanation on how Insertion sort wroks

Summary:
have a temp variable to store element in our given array, and compare whether temp is smaller, when our temp is larger
than the element to the next left OR if the end is reached INSERT temp at that position.
"""


def insertion_sort(nums):

    # idx represents the current pointer
    for idx in range(0, len(nums)):

        # hold current element for comparison
        temp = nums[idx]

        # if the left element is smaller than our current, we need to swap and shift the pointer.
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
