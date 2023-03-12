'''
Title     : Yet another query problem
Domain    : Prefix-Sum, Arrays, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 11 Mar 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def solveQueries(self, N: int, num: int, A: List[int], Q: List[List[int]]) -> List[int]:
        res = []
        for q in Q:
            l, r, k = list(map(int, q))
            d = {}
            c = 0
            for i in range(l, N):
                if A[i] not in d:
                    d[A[i]] = 1
                else:
                    d[A[i]] += 1
            for i in range(l, r+1):
                if d[A[i]] == k:
                    c += 1
                d[A[i]] -= 1
            res.append(c)
        return res
