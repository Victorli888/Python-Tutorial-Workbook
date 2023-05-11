#https://leetcode.com/problems/container-with-most-water/

"""
Define the problem:
Given a list, determine the largest area possible, elements = height; index is the length of the container along the
x-axis
We should return the largest area.
Time: O(n^2)
Space: O(1)
"""
def brute_force(height):
    ans = 0
    for left_idx in range(len(height)):
        for right_idx in range(left_idx + 1, len(height)):
            container_width = right_idx - left_idx
            container_height = min(height[left_idx], height[right_idx])
            area = container_width * container_height
            if area > ans:
                ans = area
    return ans

def two_pointer(height):
    """
    Two - pointer approach to find a containers height, The shorter height is the one that limits the containers ability
    to hold water, increment left of decrement right to find the next best height to contain water. save the best answer
    only.

    Time Complexity: O(N)
    Space: O(1)
    :param height:
    :return:
    """
    ans  = 0
    left = 0
    right = len(height) - 1

    while left < right:
        # Calculate Area
        container_width = right - left
        container_height = min(height[left], height[right])
        container_area = container_width * container_height
        ans = max(ans, container_area)

        if height[left] > height[right]:
            # right is smaller
            right -= 1
        else:
            left += 1
    return ans
