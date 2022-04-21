# Linear Search - going through each and every element in a list.
# Binary Search - splitting the list in half and searching through the half before moving on

print("Example 1: Linear Search")
#  find if 0 is present in the list
list_a = [1,3,5,7,0,44,6,2,4]


def linear_search(list):
    for i in list:
        if i == 0:
            return "0 Found!"
    return "Nothing found"

print(linear_search(list_a))

print("Example 2: Binary Search")  # for a sorted list
# The idea is to keep comparing the element with the middle value. Thus, each search we eliminate one half of the list.
# 1. Two Pointers, First and Last (these increment or decrement to limit the part of list to be searched
# 2. Find the middle element = [length of list] / 2
# 3. compare the middle element with the value to be found
# 4. check if the middle element is lesser to the value to be found
#   - IF yes, element must lie on the second half of the list
#   - IF no, element must lie on the first half of the list.
print("Find whether 14 is present in the given list\n")
given = [2,3,4,5,6,7,8,9,14,54]

def binary_search(arr, target):  # search_for = What number we are searching for
    # Initialize Variables for binary search
    si = 0  # Starting Index
    ei = len(arr)-1  # Ending Index
    searching = True

    while searching:
        # Start in the middle
        mi = (si+ei)//2  # Middle Index

        # IF Value is found
        if arr[mi] == target:
            print(f"Found {target} at index {mi}")
            searching = False  # stop searching
            return mi  # Terminates the program


        elif si+1 == ei:  # If we searched the entire array and can't find the target
            print(f"{target} could not be found")
            searching = False

        # Else continue searching
        else:
            if arr[mi] > target:  # What we're searching for is a smaller number
                # Go left
                ei = mi  # Middle index is now the new Ending Index or Ceiling
            else:  # What we're searching for is a larger number
                # Go Right
                si = mi  # middle index is the new Starting index or Floor


binary_search(given, 7)  # Test  Value 7 should be found at index 5
