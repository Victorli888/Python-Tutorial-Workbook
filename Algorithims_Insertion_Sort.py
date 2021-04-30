# A list is only sorted if it is in ascending order. A descending order is considered the worst unsorted case.

# For Insertion Sort you need to consider two parts of a list, an unsorted portion and a sorted portion
# the sorted portion must stay sorted at all times, The first element is to be in the sorted portion and must be
# compared to all the elements in the unsorted portion. Then INSERT  each unsorted element to its correct place.

# Follow these rules

# 1. Start with the first element and add it to the sorted portion of your list
# 2. Compare the next element, If its bigger simply add it to the list and do nothing, else insert it to the left
# 3. Restart
# 4. Compare the next element, with the most recent element in the sorted list if bigger add it else move to the next
# smallest element in the sorted list and repeat.
# 5. Repeat until done.


def insertionSort(alist):

    for i in range(0, len(alist)):

        # element to be compared
        current = alist[i]

        # compare the current element with the sorted portion and swapping
        while i > 0 and alist[i-1] > current:
            alist[i] = alist[i-1]
            i = i-1
            alist[i] = current

        #print(alist)  # uncomment this part to see how the list actually gets sorted.
    return alist

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






list = [2,5,8,0,4,7,9,12,3,5,7]
print(recursive(list, 0))
