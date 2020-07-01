"""
Binary Search Review
Imagane a number line from 0 to 100 and in between it a magic number. Binary Search follows this procedure
FIND:   34
ASSUME:      0 = low; 100 = high; 50 = middle
PROCEDURE:
1. check if 34 => middle or 34 < middle [ 34 < 50 TRUE]
2. cut the number line accordingly! Number line is now 0 to 50
0 = low; 50 = high; middle = 25
3. check if 34 => middle or 34 < middle [ 34 => 25 TRUE]
4. cut the number line accordingly! Number line is now 25 to 50
etc

Textbook Example:
2  4  9  12  34  35  77
|_____________________|  # The number we were trying to guess is in here

2  4  9  12  34  35  77
| low                 | high
|_____________________|        # We will call these two position low and high

2  4  9  12  34  35  77
| low                 | high
|_____________________|        # The number is somewhere between low and high

2  4  9  12  34  35  77
| low                 | high   # We're also able to calculate the index for
|_____________________|        # the number in the middle of low and high

2  4  9  12  34  35  77
| low     | middle     | high   # We're also able to calculate the index for
|_________|____________|        # the number in the middle of low and high

#
# Assume the number we're searching for is 4
#

2  4  9  12  34  35  77
| low     | middle     | high   # We're also able to calculate the index for
|_________|____________|        # the number in the middle of low and high

2  4  9  12  34  35  77
| low     | middle     | high   # As the list is sorted we can check if the
|_________|____________|        # number at 'middle' is <= or > 4

2  4  9  12  34  35  77
| low     | middle     | high   # In this case 4 is < 12 so we don't need to
|_________|____________|        # bother searching anything above middle index

2  4  9  12
| low     | high                # So we cut that portion of the list out
|_________|                     # and make middle the new high

2  4  9  12
| low     | high                # Repeat the process,
|_________|                     # continuously halving the list until the condition
                                # that low < high fails i.e low == high
"""


def binary_search(arr, elem):
    low = 0                      # Define initial low value.
    high = len(arr)              # Define initial high value.

    while low < high:            # The condition that must hold true.
        mid = (low + high) // 2  # Calculate the mid index.

        if arr[mid] < elem:  # Check if the value is in first or second half.
            low = mid + 1    # Update low value if mid val < elem (in second half).
        else:
            high = mid      # Otherwise update high value (elem in first half).
    return low              # Return the position of the element we're searching for.
                            

ex = list(range(1, 101))
print(ex)
ans = binary_search(ex, 29)
print(ans)
