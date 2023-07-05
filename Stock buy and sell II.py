'''
Title     : Stock buy and sell II
Author    : Asmit Singh
Solved On   : 5 Jul 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def stockBuyAndSell(self, n: int, prices: List[int]) -> int:
        res = 0
        for i in range(n-1):
            if prices[i+1] > prices[i]:
                res += prices[i+1]-prices[i]
        return res
