"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any
order.

https://leetcode.com/problems/top-k-frequent-elements/
"""
def list_frequent_elements(nums, k):
    """
    Uses a list of buckets to return the k of the most frequent numbers from given list of numbers num.
    :param nums: given array of numbers
    :param k: Number of frequent Elements, ie 2 shows the two most frequent numbers in a list
    :return: []
    """
    count = {}
    # freq is a list of buckets that will hold number from least to most frequent.
    # The index of the bucket describes the frequency and the element is the number from the given list

    # freq[0] would be hold the bucket numbers that don't occur, technically that should always be empty.
    # the range of len(nums) would then mean freq wouldn't be able to hold the maximum number of occurrences
    # i.e nums = [1], range(1) would create a bucket ONLY for index 0. For index 1,  len(nums)+1 would be needed
    freq = [[] for num in range(len(nums)+1)]

    # iterate and populate count hashmap
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    # count hashmap contains {number, total_count}, populate the buckets in our frequency list
    for n, c in count.items():
        freq[c].append(n)

    ans = []
    # freq is ordered from least to most frequent, thus we should start at the end & iterate backwards
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            ans.append(n)
            if len(ans) == k:
                return ans




