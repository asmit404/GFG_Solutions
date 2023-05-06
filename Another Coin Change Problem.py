'''
Title     : Another Coin Change Problem
Author    : Asmit Singh
Solved On   : 6 May 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def makeChanges(self, N: int, k: int, target: int, coins: List[int]) -> bool:
        res = [[False] * (target + 1) for _ in range(k + 1)]
        res[0][0] = True
        for i in range(1, k + 1):
            for j in range(1, target + 1):
                for l in coins:
                    if j < l:
                        continue
                    res[i][j] |= res[i - 1][j - l]
        return res[k][target]
