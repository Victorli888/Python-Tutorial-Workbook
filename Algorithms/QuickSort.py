# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

print("\n\n\nExample 1: Quick Sort")
# Quick sort is Recursive Dive and Conquer algorithm that is very efficient for large data sets.

# SELECT A PIVOT NUMBER: We do this using the Median of three( By selecting a median number and picking the middle of
# of the three.
# From there we pick a Pivot point and put all the elements that are smaller to the left of the Pivot element.
# and all the elements larger than the pivot number to the right of the pivot element.

def quick_sort(A):
    quick_sort2(A, 0, len(A) - 1) # the arguments will be passed as A, low, and hi in quicksort2

def quick_sort2(A, low, hi):
    if low < hi:  # Essentially saying If there is more than one index to be sorted then.... do the following
        p = partition(A, low, hi)  # the partition method will return our pivot
        quick_sort2(A, low, p - 1)  # recursive method for left of the pivot
        quick_sort2(A, p + 1, hi)  # recursive method for the right of the pivot


def get_pivot(A, low, hi): # this will be used in the partition method
    mid = (hi + low) // 2  # floor division the low and hi for the middle
    pivot = hi
    if A[low] < A[hi]:  # if index 0 < than index 9 then continue...
        if A[mid] < A[hi]:  # if Index 5 is < index 9 then Pivot should be index 5 or mid
            pivot = mid
    elif A[low] == A[hi]:  # else if index 0 is equal to index 9 then pivot should be index 0
        pivot = low
    return pivot


def partition(A, low, hi):
    pivotIndex = get_pivot(A, low, hi)
    pivotValue = A[pivotIndex]
    A[pivotIndex], A[low] = A[low], A[pivotIndex]
    border = low

    for i in range(low, hi + 1):
        if A[i] < pivotValue:  # all indices smaller than the pivot value
            border += 1 # add one to the border index
            A[i], A[border] = A[border], A[i]  # swap
    A[low], A[border] = A[border], A[low]  # swap

    return (border)


def quick_selection(x, first, last):  # not necessary but will help sort faster LOOK INTO THIS...
    for i in range(first, last):
        minIndex = i
        for j in range(i + 1, last + 1):
            if x[j] < x[minIndex]:
                minIndex = j
        if minIndex != i:
            x[i], x[minIndex] = x[minIndex], x[i]

list = [5,9,1,2,4,8,6,3,7,10]
list2 = sorted(list)
print(list2)
print(f"Your current list looks like this: {list}")
quick_sort(list)
print(f"Your sorted list looks like this: {list}")