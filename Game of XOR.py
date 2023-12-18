"""
Title     : Game of XOR
Author    : Asmit Singh
Solved On   : 18 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def gameOfXor(self, N, A):
        if N % 2 == 0: return 0
        res = 0
        for i in range(0, N, 2):
            res ^= A[i]
        return res

# Time Complexity  : O(n)
# Space Complexity : O(1)