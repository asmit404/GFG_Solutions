"""
Title     : Painting the Fence
Author    : Asmit Singh
Solved On   : 14 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def countWays(self, n, k):
        MOD = 1000000007
        if n == 0:
            return 0
        elif n == 1:
            return k
        same, diff = k, k * k
        for _ in range(3, n + 1):
            cnt = ((k - 1) * (diff + same)) % MOD
            same, diff = diff, cnt
        return diff

# Time Complexity  : O(n)
# Space Complexity : O(1)