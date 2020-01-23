def mergesort(mylist):
    if len(mylist) > 1:
        mid = len(mylist) // 2  # floor division -- The entire
        left = mylist[:mid]
        right = mylist[mid:]  # "slice assignment"

        # Recursive call on each half
        mergesort(left)
        mergesort(right)

        # Two iterators for transversing the two halves
        l = 0
        r = 0

        # Iterator for the main list
        k = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                # The value from the left half is being used
                mylist[k] = left[l]
                # Move the iterator forward.
                l += 1
            else:
                mylist[k] = right[r]
                r += 1
            # move to the next slot
            k += 1

        # For all the remaining values
        while l < len(left):
            mylist[k] = left[l]
            l += 1
            k += 1

        while r < len(right):
            mylist[k] = right[r]
            r += 1
            k += 1


mylist = [52, 3, 44, 7, 12, 9, 34, 56, 83, 45, 23, 6, 4, 9, 22]

mergesort(mylist)
print(mylist)





