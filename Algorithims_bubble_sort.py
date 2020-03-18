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
