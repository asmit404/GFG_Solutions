'''
Title     : Total Cuts
Author    : Asmit Singh
Solved On   : 10 May 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def totalCuts(self, N: int, K: int, A: List[int]) -> int:
        count = 0
        left = [A[0]]
        for i in range(1, N):
            left.append(max(A[i], left[-1]))
        right = [A[-1]]
        for i in range(N-2, -1, -1):
            right.append(min(A[i], right[-1]))
        right = right[::-1]
        for i in range(1, N):
            if left[i-1]+right[i] >= K:
                count += 1
        return count
