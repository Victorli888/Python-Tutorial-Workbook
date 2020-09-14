"""
Hacker Rank Question Link: https://www.hackerrank.com/challenges/apple-and-orange/problem
s - starting location of house
t - ending location of house
a - location of apple tree
b - location of orange tree
apples - array with locations of dropped apples
oranges - array with locations of dropped oranges
My solution: Space Complexity: O(1)  Time Complexity: O(n)
"""

def countApplesAndOranges(s, t, a, b, apples, oranges):
    a_count = 0
    b_count = 0
    for i in range(len(apples)):
        if apples[i] + a >= s and apples[i] + a <= t:  # Locate apples within house range (s,t)
            a_count += 1
    for i in range(len(oranges)):
        if oranges[i] + b >= s and oranges[i] + b <= t:  # locate oranges within house range (s,t)
            b_count

    print(a_count)
    print(b_count)


countApplesAndOranges(7,11,5,15,[-2,2,1],[5,6])  # ans: 1,0
