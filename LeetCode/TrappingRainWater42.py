#https://leetcode.com/problems/trapping-rain-water/

def trap(height):
    """
    Finding the total amount of water trapped using two-pointer strategy
    :param height: Height of mounds
    :return: Total amount of water trapped per unit

    O(n) time complexity O(1) Space
    """
    left_idx = 0
    right_idx = len(height) - 1
    left_max = height[left_idx]
    right_max = height[right_idx]
    ans = 0

    while left_idx < right_idx:
        if left_max < right_max:
            left_idx += 1
            left_max = max(left_max, height[left_idx])
            ans += left_max - height[left_idx]
        else:
            right_idx -= 1
            right_max = max(right_max, height[right_idx])
            ans += right_max - height[right_idx]
    return ans

