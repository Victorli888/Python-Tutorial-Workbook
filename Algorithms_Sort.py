import sys
print("Example 1: Merge sort")


def merge_sort(A):  # When this method is called on, A represents A
    merge_sort2(A, 0, len(A)-1)  # A = List;  0 = starting index; len(A)-1 = Ending index


def merge_sort2(A, first, last):  # List A, First and last indices
    if first < last:  # This means if there's more than one item in the list break it down by....
        middle = (first + last)//2  # break it in half
        merge_sort2(A, first, middle)  # merge sort the first half
        merge_sort2(A, middle+1, last)  # merge sort the 2nd half of the list
        merge(A, first, middle, last)  # combine the two sorted lists


def merge(A, first, middle, last):  # list A, First, Middle, and Last index
    L = A[first:middle+1]   # create a variable for the first half
    R = A[middle+1:last+1]  # creating  a variable for the 2nd half.
    L.append(sys.maxsize)  # use these both these numbers...
    R.append(sys.maxsize)  # ...to know when you've reached the end of the list
    i = j = 0  # i for the right j for the left halves of the sort
    #  k will represent the list where merge sort will place elements. ( basically list A's index)
    for k in range(first, last+1):  # for the full range of elements in the list
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
# If the left element is smaller add it to where index [k] is in list A and increment the right index (i) over  by 1

        else:
            A[k] = R[j]
            j += 1
# else if the right element is smaller add it to where index [k] is in List A and increment the left index (j) over by 1


list = [5,9,1,2,10,4,8,6,3,7]

print(f"Your current list looks like this: {list}")
merge_sort(list)
print(f"Your sorted list looks like this: {list}")


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

print("\n\n\nExample 2: Quick Sort")
# Quick sort is Recursive Dive and Conquer algorithm that is very efficient for large data sets.

# SELECT A PIVOT NUMBER: We do this using the Median of three( By selecting a median number and picking the middle of
# of the three.
# From there we pick a Pivot point and put all the elements that are smaller to the left of the Pivot element.
# and all the elements larger than the pivot number to the right of the pivot element.

def quick_sort(A):
    quick_sort2(A, 0, len(A) - 1)


def quick_sort2(A, low, hi):
    if low < hi:
        p = partition(A, low, hi)
        quick_sort2(A, low, p - 1)
        quick_sort2(A, p + 1, hi)


def get_pivot(A, low, hi):
    mid = (hi + low) // 2
    s = sorted([A[low], A[mid], A[hi]])
    if s[1] == A[low]:
        return low
    elif s[1] == A[mid]:
        return mid
    return hi


def partition(A, low, hi):
    pivotIndex = get_pivot(A, low, hi)
    pivotValue = A[pivotIndex]
    A[pivotIndex], A[low] = A[low], A[pivotIndex]
    border = low

    for i in range(low, hi + 1):
        if A[i] < pivotValue:
            border += 1
            A[i], A[border] = A[border], A[i]
    A[low], A[border] = A[border], A[low]

    return (border)


def quick_selection(x, first, last):
    for i in range(first, last):
        minIndex = i
        for j in range(i + 1, last + 1):
            if x[j] < x[minIndex]:
                minIndex = j
        if minIndex != i:
            x[i], x[minIndex] = x[minIndex], x[i]

list = [5,9,1,2,4,8,6,3,7,10]
print(f"Your current list looks like this: {list}")
quick_sort(list)
print(f"Your sorted list looks like this: {list}")