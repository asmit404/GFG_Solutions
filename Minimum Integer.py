"""
Title     : Minimum Integer
Domain    : Mathematical, Arrays
Author    : Asmit Singh
Solved On   : 30 Mar 2023
Solved Using   : Python3
"""

from typing import List
class Solution:
    def minimumInteger(self, N: int, A: List[int]) -> int:
        s = sum(A)
        a = float('inf')
        for i in range(N):
            if A[i] >= s/N:
                a = min(a, A[i])
        return a
