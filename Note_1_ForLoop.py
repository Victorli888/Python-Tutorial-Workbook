# Question: Why can't I use the following for loop to change the indices in my array?
def bad_forloop(ar):
    for i in ar:
        i *= 2
    return ar
# The goal is to change the items in the array in place so that we don't have to create a new array.
# for the above if ar = [2,4,6,8]; the function will result in: [2,4,6,8] --- Read Why?


def good_forloop(box):
    for i in range(len(box)):
        box[i] *= 2
    return box


""" WHY?!?!?!?!
for i in box:
    i *= 2

vs

for i in range(len(box)):
    box[i] *= 2

we designate variable (i) with value of each index in array box But that doesn't mean we change any of the index in
the array.
HOWEVER,
if we use for i in range(len(box)) and state that we're changing box[i] then we ask the python interpreter to 
specifically change the index in that array.
"""
box = [2, 4, 6, 8, 10]  # Expected [4,8,16,20]
print(f"Before: {box}")
box = good_forloop(box)
print(f"After: {box}")  # show expected result
