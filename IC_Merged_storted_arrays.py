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

lisa = [3,4,6,10,11,15]
alice = [1,5,8,12,14,19]

new_list = merge_lists(lisa, alice)
print(new_list)
