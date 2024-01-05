"""
Title     : Count possible ways to construct buildings
Author    : Asmit Singh
Solved On   : 5 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def TotalWays(self, N):
        MOD = 1000000007
        prev = curr = 1
        for _ in range(N):
            prev, curr = curr, (prev + curr) % MOD
        return (curr * curr) % MOD

# Time Complexity  : O(n)
# Space Complexity : O(1)