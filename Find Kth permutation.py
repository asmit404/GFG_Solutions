'''
Title     : Find Kth permutation
Author    : Asmit Singh
Solved On   : 08 Jun 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def kthPermutation(self, n: int, k: int) -> str:
        k -= 1
        pool = []
        fact = 1
        for i in range(1, n + 1):
            pool.append(str(i))
            fact *= i
        perm = ""
        for i in reversed(range(1, n + 1)):
            fact //= i
            perm += pool.pop(k // fact)
            k %= fact
        return perm
