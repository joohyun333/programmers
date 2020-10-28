# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List
import sys
def maxProfit(prices: List[int]) -> int:
    profit, min_price = 0, sys.maxsize
    for price in prices:
        min_price = min(price, min_price)
        profit = max(profit, price - min_price)
    return profit
if __name__ == "__main__":
    prices = [1]
    prices = [7,6,4,3,1]
    print(maxProfit(prices))