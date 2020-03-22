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

def binary_search(list, data):
    first = 0
    last = len(list)-1
    done = False

    while first <= last and not done:
        mid = (first + last)//2
        if list[mid] == data:
            done = True
        else:
            if list[mid] > data:
                last = last-1
            else:
                first = first+1
    return done

print(binary_search(given,14))
