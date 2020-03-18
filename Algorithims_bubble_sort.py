# In Bubble Sort, it sorts by comparing each element to its right side, and whichever element is the smaller will  be
# shifted to the left, repeat this until you get to the end of the list. (The largest number will be at the end)
# A new round beings and you repeat the process untill everything is sorted.

print("Example 0: lets understand how to swap")
a = 5
b = 10
print(f"Initially, a = {a} and b = {b} ")
# lets swap them so a = 10 and b = 5
temp = a
a = b
b = temp
print(f"Now, a = {a} and b = {b}")
print("\n\nWe can also do this by creating a swap method")
def swap(a,b):
    temp = a
    a = b
    b = temp
    return [a, b]
A = 5
B = 10
print([A, B])
print("now let's swap them.")
print(swap(A,B))

print("\n\nExample 1: Bubble sort")
def bubbleSort(list):
    # Setting the range for comparison ( 1st round n, 2nd round n-1, etc.
    for i in range(len(list)-1,0,-1):
        # Compare within the set range
        for j in range(i):
            # compare elements with it's right side neighbor
            if list[j] > list[j+1]:
                #swap
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

print(bubbleSort([5,1,4,3,6,8,9,0,2,7]))


print("\n\nNotes: range(len(list)-1,0,-1)")
# if we used len(list) it would put us outside the range of our list because our list starts at 0 take for example:
# we have list with 10 elements,
g = [5,1,4,3,6,8,9,0,2,7]
print(f"If we were to take len(g) we would get {len(g)}")
# but say we're trying to point to the last element in our list, Since python start referencing at 0 and not 1 for lists
# the last element is in the 9th position not the 10th.
# this means if we call on g[10] we will get an error because it is outside of the range of g

# in other words, to simplfy range(len(list)-1,0,-1) we are simply saying:
# range(last_element, First_element, go_backwards by 1)
