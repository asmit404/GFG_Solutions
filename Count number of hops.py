"""
Title     : Count number of hops
Author    : Asmit Singh
Solved On   : 16 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def countWays(self, N):
        MOD = 1000000007
        ways = [1] + [0] * N
        for i in range(1, N + 1):
            for j in range(1, 4):
                if i - j >= 0:
                    ways[i] += ways[i - j]
        return ways[N] % MOD

# Time Complexity: O(N)
# Space Complexity: O(N)