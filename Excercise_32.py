the_count = [1, 2, 3, 4, 5]  # a list of integers
fruits = ['apples', 'oranges', 'pears', 'apricots']  # a list of just strings
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']  # a list of strings and integers

# this first kind of for loop goes through a list
for number in the_count:
    print(f'This is count {number}')

# same as above
for fruit in fruits:
    print(f'A fruit of type: {fruit}')

# also we can go through mixed lists too
# Also notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I've got {i}")  # for loop printing with integers and strings are A okay with Python

# we can also build lists, first start with an empty one
elements = []  # create a list called "elements"

# then use the range function to do 0 - 5 counts

for i in range(0, 6):  # this creates a list of numbers from 0 to 5  in python lists are read as (x,y-1)
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)  # append means to add to the list "elements"

for i in elements:
    print(f"Element was: {i}")
