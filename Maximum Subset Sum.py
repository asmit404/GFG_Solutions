'''
Title     : Maximum Subset Sum
Author    : Asmit Singh
Solved On   : 14 May 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def findMaxSubsetSum(self, N: int, A: List[int]) -> int:
        a, b = A[0], 0
        for i in range(1, N):
            b = max(a, b)+A[i]
            a, b = b, a
        return max(a, b)
