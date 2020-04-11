def Reverse(lista):

    # Create Pointers
    start = 0
    end = len(lista)-1

    # Begin swapping
    while start < end:
        temp = lista[start]
        lista[start] = lista[end]
        lista[end] = temp

        # Increment and decrement pointers
        start += 1
        end -= 1

    return lista

def Reverse2(lista):
    # initialize pointers
    left = 0
    right = len(lista)-1

    #begin swapping
    while left < right:
        lista[left], lista[right] = lista[right], lista[left]

    # Increment & decrement your pointers
        left += 1
        right -= 1

    return lista


list1 = [1,2,3,4,5,6]

print(f"Method 1: {Reverse(list1)} \nNow lets reverse it back!")
# Since we already reveresed once
print(f"Method 2: {Reverse2(list1)}")  # this would Reverse it back to its original answer



