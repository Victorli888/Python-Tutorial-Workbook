"""
Question 1: Create a word finder that finds words in a list with a length greater or equal to a given number

EXAMPLE INPUT
"elephant cat dog mouse bear wolf lion horse"
5
EXAMPLE OUTPUT
elephant
mouse
horse
"""


def word_seek(a_list, num):
    my_words = a_list.split()
    i = 0
    while i < len(my_words):
        if len(my_words[i]) >= num:
            print(my_words[i])
        i += 1


# example_list = "elephant cat dog mouse bear wolf lion horse"
# word_seek(example_list, 5)

"""
Question 2: Suffix Finder, Find the words from a given list with the same given suffix

# EXAMPLE INPUT
"apples oranges pears grapes lemons melons"
suffix = "es"
# EXAMPLE OUTPUT
apples
oranges
grapes
"""


def suffix_finder(a_list, suffix):
    my_words = a_list.split()
    i = 0

    while i < len(my_words):
        if my_words[i][-len(suffix):] == suffix:
            print(my_words[i])
        i += 1


# example_list = "apples oranges pears grapes lemons melons"
# example_suffix = "es"
# suffix_finder(example_list, example_suffix)

"""
Question 3, Simply wants to emphasize that all digits are truthy except 0.
create a program that echos the number of a user-input and stops echoing when 0 is the input
"""


def echo():
    ans = int(input("What Number would you like me to Echo?: "))

    while ans:
        print(f"That is the number {ans}")
        echo()
    print(f"I'm sorry I don't want to Echo the number {ans}")


# echo()

"Question 4: Element swap of a list"


def element_swap(a_list, index_1, index_2):
    temp = a_list[index_1]
    a_list[index_1] = a_list[index_2]
    a_list[index_2] = temp

    print(a_list)


# example_list = [1, 2, 3, 4, 5]
# element_swap(example_list, 0, 1)

"""
Question 5: find the smallest number in a given list.
"""


def min_swap(a_list):
    # Keep track of the position of the smallest number
    smallest_index = 0

    i = 1
    while i < len(a_list):
        if a_list[i] < a_list[smallest_index]:
            smallest_index = i
        i += 1

    temp = a_list[0]
    a_list[0] = a_list[smallest_index]
    a_list[smallest_index] = temp
    print(a_list)


# example_list = [2, 3, 4, 5, 1]
# min_swap(example_list)

"""
Question 6: Merge Two Sorted lists
"""


def not_mergesort(list1, list2):
    list3 = []
    x = 0
    y = 0
    while x < len(list1) and y < len(list2):
        if list1[x] < list2[y]:
            list3.append(list1[x])
            x += 1
        else:
            list3.append(list2[y])
            y += 1

# Handle case for when one list is longer than the other
    if x < len(list1):
        while x < len(list1):
            list3.append(list1[x])
            x += 1
    else:
        while y < len(list2):
            list3.append(list2[y])
            y += 1

    print(list3)


a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]

not_mergesort(a, b)
