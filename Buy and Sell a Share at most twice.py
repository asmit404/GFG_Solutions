"""
Title     : Buy and Sell a Share at most twice
Author    : Asmit Singh
Solved On   : 23 Feb 2024
Solved Using   : Python3
"""

from typing import List
class Solution:
    def maxProfit(self, n: int, price: List[int]) -> int:
        min_price, max_profit = price[0], -price[0]
        var1 = var2 = 0
        for i in range(1, n):
            var1 = max(var1, price[i] - min_price)
            max_profit = max(max_profit, var1 - price[i])
            var2 = max(var2, max_profit + price[i])
            min_price = min(min_price, price[i])
        return var2

# Time Complexity: O(n)
# Space Complexity: O(1)