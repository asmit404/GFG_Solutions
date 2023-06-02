'''
Title     : Find Maximum Equal sum of Three Stacks
Author    : Asmit Singh
Solved On   : 03 Jun 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def maxEqualSum(self, N1: int, N2: int, N3: int, S1: List[int], S2: List[int], S3: List[int]) -> int:
        t1 = sum(S1)
        t2 = sum(S2)
        t3 = sum(S3)
        i, j, k = 0, 0, 0

        while (i < N1 and j < N2 and k < N3):
            minm = min(t1, t2, t3)
            if (t1 == t2 == t3):
                return t1
            if t1 > minm:
                t1 -= S1[i]
                i += 1
            if t2 > minm:
                t2 -= S2[j]
                j += 1
            if t3 > minm:
                t3 -= S3[k]
                k += 1
        return 0
