"""
Bucket Sort:
Steps:
1. Find the range of buckets needed for our input
2. Initialize those buckets
3. iterate through our input and distribute each item to their respective bucket
4. sort each item in bucket
5. concatenate our buckets together & return


Bucket sort implements some other sorting algorithm to sort

Why use it?
It seems counter-intuitive to use a sorting method in our sorting method, but there use cases like if the size of nums
is incredibly large and/or if the distribution is spread evenly across nums. This is where bucket sort could increase
efficiency.

"""


def sort(nums, num_buckets=10):
    # Find maximum, to determine the range of buckets
    max_val = max(nums)
    bucket_range = max_val+1/num_buckets

    # Init buckets
    buckets = [[] for _ in range(num_buckets)]

    # Distribute num in nums to their respective bucket
    for num in nums:
        bucket_idx = int(num // bucket_range)
        buckets[bucket_idx].append(num)

    for bucket in range(num_buckets):
        buckets[bucket] = sorted(buckets[bucket])

    # Concatenate or sorted buckets
    sorted_nums = []
    for bucket in buckets:
        for num in bucket:
            sorted_nums.append(num)
    return sorted_nums
    # Using list comprehension this could be one line.
    # [num for bucket in buckets for num in bucket]



