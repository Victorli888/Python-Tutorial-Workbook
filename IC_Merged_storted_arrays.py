"""In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies
orders and enter as one unit.

Each order is represented by an "order id" (an integer).

We have our lists of orders sorted numerically already, in lists.
Write a function to merge our lists of orders into one sorted list.

~~~BONUS~~~
What if we wanted to merge several sorted lists? Write a function that takes as an input a list of sorted lists and
outputs a single sorted list with all the items from each list.

Do we absolutely have to allocate a new list to use for the merged output? Where else could we store our merged list?
How would our function need to change?

 """
import time

def list_merger(lista, listb):
    # merge into one list
    for items in lista:
        listb.append(items)
    # list b has all values now we need to sort the values.
    return sorted(listb)

"""
space complexity: O(n)
time complexity: O(n)
"""

# Interview Cake solution
def merge_lists(lisas_list, alices_list):
    # Set up our merged_list
    merged_list_size = len(lisas_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_lisa = 0
    current_index_merged = 0
    while current_index_merged < merged_list_size:
        is_lisas_list_exhausted = current_index_lisa >= len(lisas_list)
        is_alices_list_exhausted = current_index_alices >= len(alices_list)
        if (not is_lisas_list_exhausted and
                (is_alices_list_exhausted or
                 lisas_list[current_index_lisa] < alices_list[current_index_alices])):
            # Case: next comes from my list
            # Lisa's must not be exhausted, and EITHER:
            # 1) Alice's list IS exhausted, or
            # 2) the current element in my list is less
            #    than the current element in Alice's list
            merged_list[current_index_merged] = lisas_list[current_index_lisa]
            current_index_lisa += 1
        else:
            # Case: next comes from Alice's list
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list


# Victor's Solution
"""
Deeper explanation for the "Two cases in order to adding index_A to listC
1. IF A is exhausted, then the end of the list has been reached. We cannot append any more items into the list
2a. IF B is exhausted, then the end of B's list has been reached. We should append index_A
2b. OR listB[index_B] >= listA[index_A], We intend to keep this sorted from smallest to largest. If B is larger we want
to append A instead. 
IF all these conditions fail then we want to append index_B to listC


Deeper explanation to why exhaustedA and exhaustedB values need to be in the while loop, when you keep it just outside
of the loop with the other variables. When we call the method we do one check to see if A is exhausted, it returns 
false and we move onto to our while loop. in our while loop, when we call on the value of exhaustedA it will always 
return false NO MATTER WHAT because the value itself is false and we never call on it again to check it with our 
new pointer values.

"""
def merge_lists2(listA, listB):

    # init variables, Array size, Merged Array
    array_size = len(listA) + len(listB)
    listC = [None] * array_size  # this cannot be left as []  REVIEW

    index_A = 0
    index_B = 0
    index_C = 0

    # Start Merge, I will create check merge conditions for A
    while index_C < array_size:
        exhaustedA = len(listA) <= index_A  # these must be in the while loop  REVIEW
        exhaustedB = len(listB) <= index_B
        if not exhaustedA and (exhaustedB or listB[index_B] >= listA[index_A]):  # REVIEW for practice
            # Two cases in order to add index_A to listC
            # 1. A is NOT exhausted (exhaustedA = false) AND,
            # 2. either B IS exhausted OR curr_index of b is >= curr_index of A
            # If both of these are True then we will proceed with the operation.

            listC[index_C] = listA[index_A]
            index_A += 1
        else:
            listC[index_C] = listB[index_B]
            index_B += 1
        index_C += 1
    return listC




lisa = [3,4,6,10,11,15]
alice = [1,5,8,12,14,19]

new_list = merge_lists2(lisa, alice)
print(new_list)
