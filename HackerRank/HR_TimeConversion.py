"""
Hacker Rank Question Link: https://www.hackerrank.com/challenges/time-conversion/problem
input: 10:10:10PM
output: 22:10:10
12 to 24 hour conversion!
My solution: Space Complexity: O(1)  Time Complexity: O(1)
"""


def time_convert(a_string):  # Where n is the number of staircases high
    time = a_string.split(":")  # split the string into an array! ( by where you find ":")
    if time[-1][-2:] == "PM":  # The last index in the new array, and the 2 last chars in the index.
        if time[0] != "12":  # A clock will never say 24:00:00 it will tick over to 00:00:01
            time[0] = str(int(time[0])+12) # Convert to int, add 12, convert back to string

    else:  # the else case is any time other than PM which is AM
        if time[0] == "12":  # for AM cases after 12 the clock should say 00:12 AM
            time[0] = "00"

    time = ":".join(time)
    return str(time[:-2])  # Remove the AM/PM at the end.


# Test input and output
if __name__ == '__main__':
    x = time_convert("12:10:10PM")
    print(x)