# https://leetcode.com/problems/product-of-array-except-self/
def using_division(nums):
    """
    To solve Product Of Array Except Itself (Given that we can use division)

    Multiply each number in nums by the whole array and divide by itself to exclude itself
    Not an efficient solution:
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    :param nums:
    :return: [] containing product of array except itself for each number in nums
    """
    ans = [1] * len(nums)

    for idx in range(len(nums)):
        # Multiply all numbers in num
        for num in nums:
            ans[idx] *= num
        # Divide by itself, to exclude itself
        ans[idx] //= nums[idx]

    return ans


def brute_force(nums):
    """
    Instead of using division, Use a nested for loop to multiply each element with the array across the array except
    for itself.
    :param nums:
    :return:
    """
    ans = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                ans[i] *= nums[j]
    return ans

def pre_post_algo(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    Find the product of what is "left" and "right" of the itself and store it in their own arrays, then find product of
    array except itself
    :param nums:
    :return:
    """
    ans = [1] * len(nums)
    pre = [1] * len(nums)
    post = [1] * len(nums)
    # Prefix Array
    for i in range(1, len(nums)):
        pre[i] = pre[i-1] * nums[i-1]
    # Postfix Array
    for i in range(len(nums)-2,-1,-1):
        post[i] = post[i+1] * nums[i+1]
    # Find the product of both sides of "itself"
    for i in range(len(ans)):
        ans[i] = pre[i] * post[i]

    return ans

def pre_post_algo_in_place(nums):
    """
    Solves in the same way as pre_post_algo() but solves in place instead of creating O(n) arrays in memory
    nums = [1,2,3,4]
    prefix = [1,2,6,24]    (Continuously multiply starting at idx 0 and ending at 3)
    postfix = [24,24,12,4] (Continuously multiply starting at idx 3 and ending at 0)
    To find the product of all but itself at idx = i, use the left and right of i
    i = 1  ans = prefix[0] * postfix[2] ans = 1 * 12 = 12

    We do this in place by storing these calculations in the ans array
    Time: O(n)
    Space: O(1)
    :param nums:
    :return:
    """

    ans = [1] * len(nums)

    pre = 1
    for i in range(len(nums)):
        ans[i] *= pre
        pre *= nums[i]

    post = 1
    for i in range(len(nums)-1,-1,-1):
        ans[i] *= post
        post *= nums[i]

    return ans





