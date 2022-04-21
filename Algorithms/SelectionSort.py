# Very similar to Insertion sort, where we have 2 portions of a list, sorted and unsorted.

# The first element is considered the minimum and is compared with the other elements. If a new minimum is founds then
# it is considered to be the new minimum. Once a full round is complete the smallest element is swapped with the first
# element. Repeat until all elements have been sorted.

# Consider [5,9,1,2,7,0], We will run through this entire list with 5 and determine whether the numbers to the right
# are smaller. 5>1 so 1 becomes the new minimum..... 1 > 0 so 0 becomes the new minimum. swap 5 with 0 and repeat.

# 1. Consider the first element in the list and compare it to the next one
# 2. if its larger than make it the new minimum else do nothing
# 3. continue the list until the the minimum after going through the entire list and swap it with the 1st position
# 4. repeat with the following integer

print("Example 1: Selection Sort")
def selectionSort(alist):

    for i in range(len(alist)):

        # find the minimum element in remaining
        minPosition = i

        for j in range(i+1, len(alist)):
            if alist[minPosition] > alist[j]:
                minPosition = j

        # Swap the minimum element with the minPosition
        temp = alist[i]
        alist[i] = alist[minPosition]
        alist[minPosition] = temp

    return alist


list = [5,9,1,2,7,0]
print(selectionSort(list))