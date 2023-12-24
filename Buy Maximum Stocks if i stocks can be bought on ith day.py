"""
Title     : Buy Maximum Stocks if i stocks can be bought on ith day
Author    : Asmit Singh
Solved On   : 24 Dec 2023
Solved Using   : Python3
"""

from typing import List
class Solution:
    def buyMaximumProducts(self, n: int, k: int, price: List[int]) -> int:
        arr = ((price[i], i+1) for i in range(n))
        arr = sorted(arr, key=lambda x: x[0])
        res = 0
        for today, stocks in arr:
            can_buy = min(stocks, k // today)
            res += can_buy
            k -= today * can_buy
        return res

# Time Complexity  : O(nlogn)
# Space Complexity : O(n)