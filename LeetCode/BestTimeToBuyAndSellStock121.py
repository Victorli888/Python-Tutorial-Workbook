#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""
We can't sell on the first day, and we can't go back in time to sell.
"""

def two_pointer_solution(prices):
    """

    :param prices: List of prices for each day
    :return: the largest profit margin given you need to buy before you sell.
    """
    buy_idx = 0
    sell_idx = 1
    max_profit = 0

    while sell_idx < len(prices):
        if prices[buy_idx] < prices[sell_idx]:
            # Profitable.
            profit = prices[sell_idx] - prices[buy_idx]
            max_profit = max(profit, max_profit)
        else:
            buy_idx = sell_idx
        sell_idx += 1
    return max_profit
