'''
Title     : Max Coins
Author    : Asmit Singh
Solved On   : 4 May 2023
Solved Using   : Python3
'''

from typing import List
from bisect import bisect_left
from math import inf

class Solution:
    def maxCoins(self, n: int, ranges: List[List[int]]) -> int:
        ranges.sort(key=lambda x: (x[1], x[0], x[2]))
        end = [(0, 0)]
        ans = 0
        for si, ei, ci in ranges:
            j = bisect_left(end, (si, inf)) - 1
            ej, cj = end[j]
            ans = max(ans, ci + cj)
            end.append((ei, max(ci, end[-1][1])))
        return ans
