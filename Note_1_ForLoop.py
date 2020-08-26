# Array Manipulation

box = [2, 4, 6, 8, 10]
print(f"Before: {box}")

for i in range(len(box)):
    box[i] *= 2

"""
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

print(f"After: {box}")
