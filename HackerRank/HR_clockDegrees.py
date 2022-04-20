"""
Given two integers, an hour and a minute, write a function to calculate the angle between
the two hands on a clock representing that time.

Givens: Hour & Minute
Find: the smaller angle thats made between both of those hands
"""


def findAngle(hour, minute):
    """
    1. Find the ange in  degrees from location of each hand
    2. subtract the total degrees of each hand and keep the absolute value
        a. depending on where the location of minute hand is the hour hand is slighty moved away from where it is
    3. Return the angle.
    :param hour: Hour hand Location
    :param minute: Minute Hand Location
    :return: Total Degrees between each hand on the clock
    """
    dMinute = minute * (360/60)
    dHour = hour * (360/12) + (minute/60)*(360/12)
    angleBetween = abs(dMinute-dHour)

    if angleBetween > 180:  # Check and return smallest Angle
        return(360-angleBetween)
    return(angleBetween)

print(findAngle(9, 15))

"""
This is a single operation without any loops so Time Complexity and Space Complexity is O(1)
"""