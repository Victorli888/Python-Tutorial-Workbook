

def mergesort(mylist):
    if len(mylist) > 1:
        mid = len(mylist) // 2  # floor division -- The entire
        left = mylist[:mid]  # x[x0,x1,x2,x3,x4,x5....]
        right = mylist[mid:]  # "slice assignment" calls on position that the integer "mid" is

        # Recursive call on each half
        mergesort(left)  # cut the left list in half
        mergesort(right) # cut the right list in half
        # continue this until the len() left & right half is less than 1

        # Two iterators for transversing the two halves
        l = 0
        r = 0

        # Iterator for the main list
        k = 0

        while l < len(left) and r < len(right):  # continue this until both l & r are bigger than len(right) & len(left)
            if left[l] < right[r]:  # l & r represent the position of both lists ( left[] and right[])
                # The value from the left half is being used
                mylist[k] = left[l]  # so if l is smaller than r then move it to position k on mylist[]
                l += 1  # Move the iterator forward.
            else:
                mylist[k] = right[r]  # if its not smaller r should move to position k on mylist[]
                r += 1  # move to the next slot
            k += 1  # once either operation is done move on to the next position of k in mylist[]

        # For all the remaining values
        while l < len(left):  # if the iterator is less than the length of the left half of the list
            mylist[k] = left[l]
            l += 1
            k += 1

        while r < len(right):  # if the iterator is less than the length of the left half of the list
            mylist[k] = right[r]
            r += 1
            k += 1


mylist = [52, 3, 44, 7, 12, 9, 34, 56, 83, 45, 23, 6, 4, 9, 22]

mergesort(mylist)
print(mylist)





