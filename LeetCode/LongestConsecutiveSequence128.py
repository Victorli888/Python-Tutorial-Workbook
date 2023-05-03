#https://leetcode.com/problems/longest-consecutive-sequence/

def find_max_sequence_count(nums):
    """
    implementing a set, we can use the O(1) look up time to check if sequences exists in given nums
    Time: O(n)
    Space: O(n)

    Any logic that will sort the array will be n(log(n)) time
        1) convert nums to a hashset data structure
        2) check to see if num in num_set contains num-1, when num -1 doesn't exist then num is "starter" for a sequence
        3) iterate through the sequence by adding 1 and check if it exists, each iteration is counted as the curr_length
        4) when a sequence completes curr_length is compared to the current longest. where the max of the two is passed
        5) return the longest count
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

