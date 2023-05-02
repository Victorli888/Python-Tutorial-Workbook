#https://leetcode.com/problems/longest-consecutive-sequence/

def find_max_sequence_count(nums):
    """
    implementing a set, we can use the O(1) look up time to check if sequences exists in given nums
    Time: O(n)
    Space: O(n)
    :param nums: given list of numbers
    :return: the longest sequence possible from given list
    """
    num_set = set(nums)
    longest = 0

    for num in nums:
        # when n-1 doesn't exist, n must be the start of a sequence
        if (num-1) not in num_set:
            curr_len = 0
            while (num + curr_len) in num_set:
                curr_len += 1
            longest = max(curr_len, longest)
    return longest

