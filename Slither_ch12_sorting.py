def insertiton_sort(lst):
    i = 1
    while i < len(lst):
        v = lst[i]
        p = i
        while p > 0 and v < lst[p - 1]:
            lst[p] = lst[p - 1]
            p -= 1
        lst[p] = v
        i += 1
    return lst


def selection_sort(lst):
    i = 0
    while i < len(lst):
        p = i
        j = i + 1
        while j < len(lst):
            if lst[j] < lst[p]:
                p = j
            j += 1

        tmp = lst[p]
        lst[p] = lst[i]
        lst[i] = tmp
        i += 1
    return lst


def main():
    test_list = [5, 2, 4, 7, 3, 6, 22, 12]
    
    print(f"Please sort: {test_list}")
    print(f"Selection sort: {selection_sort(test_list)}")
    print(" ")
    print(f"Please sort: {test_list}")
    print(f"Insertion sort: {insertiton_sort(test_list)}")


"""
Normally we would need to leave out main() so that I can import this file without executing the functions in main() BUT
using Top Level Script Enviorment (Python) we can run our main() from the command line, and ignore main() if the script
is being imported.
"""
if __name__ == "__main__":
    print("Running script as main\n")
    main()
else:
    print("practice.py imported to module...\n")
