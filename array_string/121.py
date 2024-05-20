"""
LeetCode #121. Best time to Buy and Sell Stock

Author: Jose Renteria
"""
from typing import List

def maxProfit(prices: List[int]) -> int:
    # Sliding Window
    left, right = 0, 1 # left is buy, right is sell
    maxprofit = 0
    lt = lambda x, y: x < y
    sub = lambda x, y : x - y
    inc = lambda x: x + 1
    while lt(right, len(prices)):
        # check if it is a profitable transaction
        if lt(prices[left], prices[right]):
            maxprofit = max(maxprofit, sub(prices[right], prices[left]))
        else:
            left = right
        right = inc(right)
    return maxprofit



prices = [7,1,5,3,6,4]
sol = maxProfit(prices)
print(sol)