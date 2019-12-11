ten_things = "Apples Oranges Crows Telephone Light Sugar"  # this is a single string
print("Wait there are not 10 things in that list. Let's fix that.")
# split a string into a list ... split("where you want to split")

stuff = ten_things.split(' ')  # This means to split things at every space


more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]


while len(stuff) != 10:  # len() returns the length
    # "While the list "stuff" has not equal to 10 do the following:
    next_one = more_stuff.pop()  # remove by poping the last thing from the "more_stuff" list
    print("Adding: ", next_one)  # add the the recently popped item
    stuff.append(next_one)       # add it to "stuff" list
    print(f"There are {len(stuff)} items now.")  # tells me how many items are in list "stuff"
# Go back to the top and see if the while statement is fulfilled.

print("There we go: ", stuff)  # print the list

print("Let's do some things with stuff.")
#  0,1,2,3,4,5,6,7,8,9   apples, oranges, crows, telephone, light, sugar, boy, girl, banana, corn
print(stuff[1])
print(stuff[-1])  # 9, Corn
print(stuff.pop())  # Print Corn
print(' '.join(stuff))  # returns a list into a single sequence (single String)
print('#'.join(stuff[3:9]))   # (n, n-1)

# in other words if you want to join the entire list you would need to use
