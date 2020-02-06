# This chapter is on "Set" data structures, They act as like list that can't contain duplicate values.
# set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (unchangeable)
# However, the set itself is mutable. We can add or remove items from it.

print("Example 1: Check for duplicates in a list")
# In this first example we can use a for loop to solve this problem.
list_1 = [2, 2, 3, 3, 0]
duplicates_1 = []

for value_1 in list_1:
    if list_1.count(value_1) > 1:  # count() searches the substring and returns how many times that its present
        # string.count(substring, start=..., end=...)
        if value_1 not in duplicates_1:  # runs a check for duplicates_1, if its not already listed in it APPEND value_1
            duplicates_1.append(value_1)

print(f"The duplicates in list_1 are {duplicates_1}")

# BUT WE CAN DO BETTER, using "set we can be more elegant with our code.
print("\nExample 2: Using \"set\" to to find duplicates")

duplicates_2 = set([value_2 for value_2 in list_1 if list_1.count(value_2) > 1])
print(f"The duplicates in example 2 are: {duplicates_2}")

print("\nExample 3: Set method 1 Intersection")
# try to intersect two sets
valid_3 = set([8, 72, 60, 95, 34, 6, 100, 5, 37, 96, 72, 35, 45, 8, 6])
input_set_3 = set([9, 60, 3, 4, 87, 6])
print(f"The intersections happen at {input_set_3.intersection(valid_3)}")
print(valid_3)  # I don't understand why this shuffles my list around (only shuffles strings)

print("\nExample 4: Set method 2 Difference")
print(f"the difference between the sets are {input_set_3.difference(valid_3)}")
# This outputs the numbers in input_set_3 that are different from valid_3
# In set1 find the items that are different from set2 `set1.difference(set2)`
