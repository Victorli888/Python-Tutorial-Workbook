"""
Hacker Rank Question Link: https://www.hackerrank.com/challenges/time-conversion/problem
input: 10:10:10PM
output: 22:10:10
12 to 24 hour conversion!
My solution: Space Complexity: O(1)  Time Complexity: O(1)
"""


def time_convert(a_string):  # Where n is the number of staircases high
    time = a_string.split(":")
    if time[-1][-2:] == "PM":
        if time[0] != "12":
            time[0] = str(int(time[0])+12)

    else:
        if time[0] == "12":
            time[0] = "00"

    n_time = ":".join(time)
    return str(n_time[:-2])


# Test input and output
if __name__ == '__main__':
    x = time_convert("10:10:10PM")
    print(x)