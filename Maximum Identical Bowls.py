'''
Title     : Maximum Identical Bowls
Author    : Asmit Singh
Solved On   : 24 May 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def getMaximum(self, n: int, arr: List[int]) -> int:
        res = sum(arr)
        for i in range(n, 0, -1):
            if res % i == 0:
                return i
