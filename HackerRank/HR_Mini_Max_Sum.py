"""
HackerRank Question Link : https://www.hackerrank.com/challenges/mini-max-sum/problem

OUTPUT:
Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated
by summing exactly four of the five integers.

Time = O(n) Space = O(1) Worst case scenarios
"""""


def minmaxsum(arr):
    arr.sort()  # arr.sort() is an inplace method that returns NONE so, new_arr = arr.sort() new_arr would = NONE
    # You can also use arr = sorted(arr)

    min_arr = arr[0:4]
    max_arr = arr[:0:-1]

    ans1 = sum(min_arr)
    ans2 = sum(max_arr)

    print(ans1, ans2)


test_arr = [1, 2, 3, 4, 5]
minmaxsum(test_arr)  # expected: 10 14 output 10 14  ----- ok!
